#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path

TRACKS = [
    ("minimal", "Minimal", "docs/minimal-outputs", "minimal-outputs"),
    ("best-case", "Best Practice", "docs/best-case-outputs", "best-case-outputs"),
    ("persona", "Best Practice With Persona", "docs/persona-outputs", "persona-outputs"),
]

OPEN_FENCE = re.compile(r"^\s*```[a-zA-Z0-9_-]*\s*\n")
CLOSE_FENCE = re.compile(r"\n\s*```\s*$")


def slugify_component(title: str) -> str:
    s = title.strip().lower()
    out = []
    prev_hyphen = False
    for ch in s:
        if ch.isalnum():
            out.append(ch)
            prev_hyphen = False
        else:
            if not prev_hyphen:
                out.append("-")
                prev_hyphen = True
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "untitled"


def slugify_model(model_id: str) -> str:
    return model_id.strip().lower().replace("/", "-").replace(":", "-")


def sanitize_html(raw: str) -> str:
    if not raw:
        return ""
    s = raw.strip()
    s = OPEN_FENCE.sub("", s)
    s = CLOSE_FENCE.sub("", s)
    return s.strip()


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception:
        return ""


def indent_yaml(s: str) -> str:
    s = s.replace("\r\n", "\n")
    return "\n".join(("  " + line) for line in s.split("\n"))


def clean_intro_md(md: str) -> str:
    md = re.sub(r"^\s*</details>\s*$", "", md, flags=re.MULTILINE)
    return md.strip() + "\n"


# -----------------------------
# 1) Generate components/<track>/*.md
# -----------------------------
def generate_component_tables(repo_root: Path, base_url: str):
    comps_path = repo_root / "components.json"
    models_path = repo_root / "models.json"
    if not comps_path.exists():
        raise SystemExit("Missing components.json in repo root")
    if not models_path.exists():
        raise SystemExit("Missing models.json in repo root")

    comps = json.loads(comps_path.read_text(encoding="utf-8"))["tests"]
    models = json.loads(models_path.read_text(encoding="utf-8"))["data"]
    model_id_by_slug = {slugify_model(m["id"]): m["id"] for m in models}

    out_root = repo_root / "components"
    out_root.mkdir(parents=True, exist_ok=True)

    for track_slug, _track_title, html_root_rel, url_prefix in TRACKS:
        html_root = repo_root / html_root_rel
        track_out_dir = out_root / track_slug
        track_out_dir.mkdir(parents=True, exist_ok=True)

        wrote = 0
        skipped = 0

        for test in comps:
            title = test["title"]
            comp_slug = slugify_component(title)
            prompts = test.get("prompts", [])

            comp_dir = html_root / comp_slug
            if not comp_dir.exists():
                skipped += 1
                continue

            model_dirs = sorted([p for p in comp_dir.iterdir() if p.is_dir()])
            if not model_dirs:
                skipped += 1
                continue

            lines: list[str] = []
            lines.append("<details>\n")
            lines.append(f'  <summary><strong>{html.escape(title)}</strong></summary>\n')
            lines.append("  <table>\n")
            lines.append("    <thead>\n")
            lines.append("      <tr>\n")
            lines.append("        <th>Model</th>\n")
            lines.append("        <th>Variant</th>\n")
            lines.append("        <th>Prompt</th>\n")
            lines.append("        <th>Output</th>\n")
            lines.append("        <th>File Link</th>\n")
            lines.append("      </tr>\n")
            lines.append("    </thead>\n")
            lines.append("    <tbody>\n")

            for model_dir in model_dirs:
                model_slug = model_dir.name
                model_id = model_id_by_slug.get(model_slug, model_slug)
                model_printed = False

                for i in range(1, 6):
                    html_path = model_dir / f"g{i}.html"
                    clean = sanitize_html(read_text(html_path))
                    escaped_code = html.escape(clean)

                    deployed_url = f"{base_url}/{url_prefix}/{comp_slug}/{model_slug}/g{i}.html"
                    prompt_text = prompts[i - 1] if i - 1 < len(prompts) else ""

                    lines.append("      <tr>\n")
                    if not model_printed:
                        lines.append(f"        <td><strong>{html.escape(model_id)}</strong></td>\n")
                        model_printed = True
                    else:
                        lines.append("        <td></td>\n")

                    lines.append(f"        <td>G{i}</td>\n")
                    lines.append(f"        <td>{html.escape(prompt_text)}</td>\n")

                    lines.append("        <td>\n")
                    lines.append("          <details>\n")
                    lines.append("            <summary>View code</summary>\n")
                    lines.append(f'            <pre><code class="language-html">{escaped_code}</code></pre>\n')
                    lines.append("          </details>\n")
                    lines.append("        </td>\n")

                    lines.append(f'        <td><a href="{html.escape(deployed_url)}">Open HTML</a></td>\n')
                    lines.append("      </tr>\n")

            lines.append("    </tbody>\n")
            lines.append("  </table>\n")
            lines.append("</details>\n")

            (track_out_dir / f"{comp_slug}.md").write_text("".join(lines), encoding="utf-8")
            wrote += 1

        print(f"[{track_slug}] wrote {wrote} component md files (skipped {skipped})")


# -----------------------------
# 2) Build site/ (Jekyll)
# -----------------------------
def write_scaffold(site_dir: Path):
    (site_dir / "_layouts").mkdir(parents=True, exist_ok=True)
    (site_dir / "_includes").mkdir(parents=True, exist_ok=True)
    (site_dir / "_data").mkdir(parents=True, exist_ok=True)
    (site_dir / "assets").mkdir(parents=True, exist_ok=True)

    (site_dir / "_config.yml").write_text(
        "title: LLM HTML Component Benchmark\n"
        "markdown: kramdown\n"
        "kramdown:\n"
        "  input: GFM\n"
        "  syntax_highlighter: rouge\n"
        "defaults:\n"
        "  - scope:\n"
        "      path: \"\"\n"
        "    values:\n"
        "      layout: base\n",
        encoding="utf-8",
    )

    (site_dir / "_layouts" / "base.html").write_text(
        "<!doctype html>\n"
        "<html lang=\"en\">\n"
        "<head>\n"
        "  <meta charset=\"utf-8\" />\n"
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
        "  <title>{{ page.title }} · {{ site.title }}</title>\n"
        "  <link rel=\"stylesheet\" href=\"{{ '/assets/site.css' | relative_url }}\" />\n"
        "</head>\n"
        "<body>\n"
        "  <header class=\"top\">\n"
        "    <div class=\"wrap\">\n"
        "      <a class=\"brand\" href=\"{{ '/' | relative_url }}\">{{ site.title }}</a>\n"
        "      {% if page.show_tabs %}\n"
        "        <nav class=\"tabs\" aria-label=\"Tracks\">\n"
        "          <a href=\"{{ '/minimal' | relative_url }}\" class=\"{% if page.track == 'minimal' %}active{% endif %}\">Minimal</a>\n"
        "          <a href=\"{{ '/best-case' | relative_url }}\" class=\"{% if page.track == 'best-case' %}active{% endif %}\">Best Practice</a>\n"
        "          <a href=\"{{ '/persona' | relative_url }}\" class=\"{% if page.track == 'persona' %}active{% endif %}\">With Persona</a>\n"
        "        </nav>\n"
        "      {% endif %}\n"
        "    </div>\n"
        "  </header>\n"
        "  <main class=\"wrap\">\n"
        "    {{ content }}\n"
        "  </main>\n"
        "  <script src=\"{{ '/assets/site.js' | relative_url }}\"></script>\n"
        "</body>\n"
        "</html>\n",
        encoding="utf-8",
    )

    (site_dir / "_layouts" / "track.html").write_text(
        "---\n"
        "layout: base\n"
        "show_tabs: true\n"
        "---\n"
        "<div class=\"grid\">\n"
        "  <aside class=\"card sidebar\">\n"
        "    <div class=\"sidebar-title\">Components</div>\n"
        "    {% include sidebar.html %}\n"
        "  </aside>\n"
        "  <section class=\"card content\">\n"
        "    {{ content }}\n"
        "  </section>\n"
        "</div>\n",
        encoding="utf-8",
    )

    (site_dir / "_includes" / "sidebar.html").write_text(
        "{% assign items = site.pages | where: 'track', page.track | where: 'kind', 'component' | sort: 'order' %}\n"
        "{% for it in items %}\n"
        "  <a class=\"side-link\" href=\"#{{ it.slug }}\">{{ it.title }}</a>\n"
        "{% endfor %}\n",
        encoding="utf-8",
    )

    (site_dir / "assets" / "site.css").write_text(
        ":root{--bg:#ffffff;--text:#1a1a1a;--muted:#666;--line:#e9e9e9;--card:#fff;}\n"
        "*{box-sizing:border-box}\n"
        "body{margin:0;font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;background:var(--bg);color:var(--text);}\n"
        "a{color:inherit}\n"
        ".wrap{max-width:1080px;margin:0 auto;padding:18px 18px 40px;}\n"
        ".top{position:sticky;top:0;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line);z-index:10;}\n"
        ".brand{text-decoration:none;font-weight:800;letter-spacing:.2px;}\n"
        ".tabs{margin-top:10px;display:flex;gap:10px;flex-wrap:wrap}\n"
        ".tabs a{text-decoration:none;color:var(--muted);border:1px solid var(--line);padding:6px 10px;border-radius:999px;}\n"
        ".tabs a.active{color:var(--text);border-color:var(--text);}\n"
        ".card{background:var(--card);border:1px solid var(--line);border-radius:18px;box-shadow:0 12px 28px rgba(0,0,0,.06);}\n"
        ".card.pad{padding:18px;}\n"
        ".grid{display:grid;grid-template-columns:300px 1fr;gap:16px;align-items:start}\n"
        "@media (max-width: 940px){.grid{grid-template-columns:1fr}}\n"
        ".sidebar{padding:14px;position:sticky;top:84px}\n"
        "@media (max-width: 940px){.sidebar{position:static;top:auto}}\n"
        ".sidebar-title{font-size:13px;color:var(--muted);margin:2px 8px 10px;}\n"
        ".side-link{display:block;text-decoration:none;color:var(--muted);padding:8px 10px;border-radius:12px;}\n"
        ".side-link:hover{background:#f6f6f6;color:var(--text)}\n"
        ".content{padding:18px;}\n"
        "h1{font-size:28px;letter-spacing:-.02em;margin:0 0 10px}\n"
        "h2{font-size:18px;margin:22px 0 10px}\n"
        "p,li{color:var(--muted);line-height:1.55}\n"
        "details{border:1px solid var(--line);border-radius:14px;padding:10px 12px;margin:14px 0;background:#fff;}\n"
        "details>summary{cursor:pointer;font-weight:800}\n"
        "table{border-collapse:separate;border-spacing:0;width:100%;margin:12px 0;font-size:14px;border:1px solid var(--line);border-radius:14px;overflow:hidden}\n"
        "th,td{padding:10px;vertical-align:top;border-bottom:1px solid var(--line)}\n"
        "th{background:#fafafa;text-align:left;font-weight:800}\n"
        "tr:last-child td{border-bottom:none}\n"
        "pre{position:relative;margin:10px 0 0;overflow:auto;background:#0f0f10;color:#f2f2f2;padding:14px;border-radius:14px}\n"
        "code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;font-size:13px}\n"
        ".copy-btn{position:absolute;top:10px;right:10px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.10);color:#fff;padding:6px 10px;border-radius:10px;cursor:pointer;font-size:12px}\n"
        ".copy-btn:hover{background:rgba(255,255,255,.18)}\n"
        ".cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}\n"
        "@media (max-width: 940px){.cards{grid-template-columns:1fr}}\n"
        ".cardlink{text-decoration:none;border:1px solid var(--line);border-radius:18px;padding:16px;display:block;box-shadow:0 10px 24px rgba(0,0,0,.05)}\n"
        ".cardlink:hover{border-color:#d9d9d9;background:#fcfcfc}\n",
        encoding="utf-8",
    )

    (site_dir / "assets" / "site.js").write_text(
        "(function(){\n"
        "  function add(pre){\n"
        "    if(pre.dataset.copyReady) return;\n"
        "    const code = pre.querySelector('code');\n"
        "    if(!code) return;\n"
        "    const btn = document.createElement('button');\n"
        "    btn.className='copy-btn';\n"
        "    btn.type='button';\n"
        "    btn.textContent='Copy';\n"
        "    btn.addEventListener('click', async ()=>{\n"
        "      try{ await navigator.clipboard.writeText(code.innerText); btn.textContent='Copied'; }\n"
        "      catch(e){ btn.textContent='Failed'; }\n"
        "      setTimeout(()=>btn.textContent='Copy', 900);\n"
        "    });\n"
        "    pre.appendChild(btn);\n"
        "    pre.dataset.copyReady='1';\n"
        "  }\n"
        "  document.querySelectorAll('pre').forEach(add);\n"
        "  document.addEventListener('toggle', (e)=>{\n"
        "    if(e.target && e.target.tagName==='DETAILS') e.target.querySelectorAll('pre').forEach(add);\n"
        "  }, true);\n"
        "})();\n",
        encoding="utf-8",
    )


def write_home(repo_root: Path, site_dir: Path):
    table_md = repo_root / "table.md"
    intro = ""
    if table_md.exists():
        intro = clean_intro_md(table_md.read_text(encoding="utf-8"))

    (site_dir / "_data" / "intro.yml").write_text("html: |\n" + indent_yaml(intro) + "\n", encoding="utf-8")

    cards = (
        "<h2 style=\"margin-top:22px;\">Choose a track</h2>\n"
        "<div class=\"cards\">\n"
        "  <a class=\"cardlink\" href=\"{{ '/minimal' | relative_url }}\"><h2 style=\"margin:0;\">Minimal</h2><p>Minimal prompting setting.</p></a>\n"
        "  <a class=\"cardlink\" href=\"{{ '/best-case' | relative_url }}\"><h2 style=\"margin:0;\">Best Practice</h2><p>Best practice prompts without persona framing.</p></a>\n"
        "  <a class=\"cardlink\" href=\"{{ '/persona' | relative_url }}\"><h2 style=\"margin:0;\">Best Practice With Persona</h2><p>Best practice prompts with persona framing.</p></a>\n"
        "</div>\n"
    )

    (site_dir / "index.md").write_text(
        "---\n"
        "title: \"LLM Generated HTML Form Components Output\"\n"
        "layout: base\n"
        "show_tabs: false\n"
        "---\n\n"
        "<div class=\"card pad\">\n\n"
        "{% if site.data.intro.html %}\n"
        "{{ site.data.intro.html | markdownify }}\n"
        "{% endif %}\n\n"
        f"{cards}\n"
        "</div>\n",
        encoding="utf-8",
    )


def build_track_pages(repo_root: Path, site_dir: Path):
    for track_slug, track_title, _html_root_rel, _url_prefix in TRACKS:
        (site_dir / f"{track_slug}.md").write_text(
            "---\n"
            f"title: \"{track_title}\"\n"
            f"track: {track_slug}\n"
            "layout: track\n"
            "kind: track\n"
            "---\n\n"
            "{% assign comps = site.pages | where: 'track', page.track | where: 'kind', 'component' | sort: 'order' %}\n"
            "{% for c in comps %}\n"
            "<a id=\"{{ c.slug }}\"></a>\n"
            "{{ c.content }}\n"
            "{% endfor %}\n",
            encoding="utf-8",
        )

    # component pages from components/<track>/*.md
    for track_slug, _track_title, _html_root_rel, _url_prefix in TRACKS:
        src_dir = repo_root / "components" / track_slug
        if not src_dir.exists():
            continue

        out_dir = site_dir / "components" / track_slug
        out_dir.mkdir(parents=True, exist_ok=True)

        md_files = sorted([p for p in src_dir.rglob("*.md") if p.is_file()])
        order = 1

        for p in md_files:
            raw = p.read_text(encoding="utf-8")
            m = re.search(r"<summary><strong>(.*?)</strong></summary>", raw)
            title = (m.group(1) if m else p.stem).replace("&amp;", "&").strip()
            slug = p.stem

            front = (
                "---\n"
                f"title: \"{title.replace('\"', '\\\"')}\"\n"
                f"slug: {slug}\n"
                f"track: {track_slug}\n"
                "kind: component\n"
                f"order: {order}\n"
                "---\n\n"
            )

            (out_dir / f"{slug}.md").write_text(front + raw + "\n", encoding="utf-8")
            order += 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".", help="repo root")
    ap.add_argument("--base-url", required=True, help="https://momentine.github.io/llm-html")
    ap.add_argument("--out", default="site", help="output jekyll site dir")
    args = ap.parse_args()

    repo_root = Path(args.repo_root).resolve()
    base_url = args.base_url.rstrip("/")
    site_dir = Path(args.out).resolve()

    # step 1: generate components tables
    generate_component_tables(repo_root, base_url)

    # step 2: build site
    write_scaffold(site_dir)
    write_home(repo_root, site_dir)
    build_track_pages(repo_root, site_dir)

    print(f"\nDone. Generated:\n- components/<track>/*.md\n- {site_dir}/ (jekyll site)")


if __name__ == "__main__":
    main()
