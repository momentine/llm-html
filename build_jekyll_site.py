#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

TRACKS = [
  ("minimal", "Minimal"),
  ("best-case", "Best Practice"),
  ("persona", "Best Practice With Persona"),
]

def slugify(name: str) -> str:
  s = name.strip().lower()
  s = re.sub(r"[^\w\s-]", "", s)
  s = re.sub(r"[\s_-]+", "-", s)
  return s.strip("-") or "component"

def extract_title(md_text: str, fallback: str) -> str:
  for line in md_text.splitlines():
    if line.startswith("# "):
      return line[2:].strip()
  return fallback

def indent_yaml(s: str) -> str:
  s = s.replace("\r\n", "\n")
  return "\n".join(("  " + line) for line in s.split("\n"))

def write_site_scaffold(site_dir: Path):
  (site_dir / "_layouts").mkdir(parents=True, exist_ok=True)
  (site_dir / "_includes").mkdir(parents=True, exist_ok=True)
  (site_dir / "_data").mkdir(parents=True, exist_ok=True)

  # config
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
    "      layout: default\n",
    encoding="utf-8",
  )

  # default layout
  (site_dir / "_layouts" / "default.html").write_text(
    "<!doctype html>\n"
    "<html lang=\"en\">\n"
    "<head>\n"
    "  <meta charset=\"utf-8\" />\n"
    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n"
    "  <title>{{ page.title }} · {{ site.title }}</title>\n"
    "  <style>\n"
    "    body{font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;margin:0;background:#fff;color:#111;}\n"
    "    header{border-bottom:1px solid #eee;padding:14px 18px;position:sticky;top:0;background:#fff;z-index:5;}\n"
    "    header a{color:#111;text-decoration:none;font-weight:700;}\n"
    "    .wrap{max-width:1200px;margin:0 auto;padding:18px;}\n"
    "    .tabs a{display:inline-block;margin-right:12px;padding:6px 10px;border-radius:10px;text-decoration:none;color:#111;border:1px solid #eee;}\n"
    "    .tabs a.active{border-color:#111;}\n"
    "    .grid{display:grid;grid-template-columns:320px 1fr;gap:20px;}\n"
    "    .panel{border:1px solid #eee;border-radius:14px;padding:14px;}\n"
    "    .sidebar a{display:block;padding:8px 10px;border-radius:10px;text-decoration:none;color:#111;}\n"
    "    .sidebar a:hover{background:#f7f7f7;}\n"
    "    .muted{color:#666;font-size:14px;}\n"
    "    details{border:1px solid #eee;border-radius:12px;padding:10px 12px;margin:12px 0;}\n"
    "    details > summary{cursor:pointer;font-weight:700;}\n"
    "    table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px;}\n"
    "    th,td{border:1px solid #e6e6e6;padding:8px;vertical-align:top;}\n"
    "    th{background:#fafafa;text-align:left;}\n"
    "    pre{overflow:auto;background:#0b0b0b;color:#f4f4f4;padding:12px;border-radius:12px;}\n"
    "    code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace;}\n"
    "  </style>\n"
    "</head>\n"
    "<body>\n"
    "  <header>\n"
    "    <div class=\"wrap\">\n"
    "      <a href=\"{{ '/' | relative_url }}\">{{ site.title }}</a>\n"
    "      <div class=\"tabs\" style=\"margin-top:10px;\">\n"
    "        <a href=\"{{ '/minimal' | relative_url }}\" class=\"{% if page.track == 'minimal' %}active{% endif %}\">Minimal</a>\n"
    "        <a href=\"{{ '/best-case' | relative_url }}\" class=\"{% if page.track == 'best-case' %}active{% endif %}\">Best Practice</a>\n"
    "        <a href=\"{{ '/persona' | relative_url }}\" class=\"{% if page.track == 'persona' %}active{% endif %}\">With Persona</a>\n"
    "      </div>\n"
    "    </div>\n"
    "  </header>\n"
    "  <main class=\"wrap\">\n"
    "    {{ content }}\n"
    "  </main>\n"
    "</body>\n"
    "</html>\n",
    encoding="utf-8",
  )

  # track layout (two-column like your screenshot)
  (site_dir / "_layouts" / "track.html").write_text(
    "<div class=\"grid\">\n"
    "  <aside class=\"panel sidebar\">\n"
    "    <div class=\"muted\" style=\"margin-bottom:10px;\">Components</div>\n"
    "    {% include sidebar.html %}\n"
    "  </aside>\n"
    "  <section class=\"panel\">\n"
    "    {{ content }}\n"
    "  </section>\n"
    "</div>\n",
    encoding="utf-8",
  )

  # sidebar include
  (site_dir / "_includes" / "sidebar.html").write_text(
    "{% assign items = site.pages | where: 'track', page.track | where: 'kind', 'component' | sort: 'order' %}\n"
    "{% for it in items %}\n"
    "  <a href=\"#{{ it.slug }}\">{{ it.title }}</a>\n"
    "{% endfor %}\n",
    encoding="utf-8",
  )

def write_intro_data(repo_root: Path, site_dir: Path):
  table_md = repo_root / "table.md"
  if not table_md.exists():
    return
  text = table_md.read_text(encoding="utf-8")
  (site_dir / "_data" / "intro.yml").write_text(
    "html: |\n" + indent_yaml(text) + "\n",
    encoding="utf-8",
  )

def build_track(repo_root: Path, site_dir: Path, track_slug: str, track_title: str):
  fragments_dir = repo_root / "components" / track_slug
  out_dir = site_dir / "components" / track_slug
  out_dir.mkdir(parents=True, exist_ok=True)

  # A top-level track page
  (site_dir / f"{track_slug}.md").write_text(
    "---\n"
    f"title: \"{track_title}\"\n"
    f"track: {track_slug}\n"
    "layout: track\n"
    "---\n\n"
    "{% if site.data.intro.html %}\n"
    "{{ site.data.intro.html | markdownify }}\n"
    "{% endif %}\n\n"
    "{% assign comps = site.pages | where: 'track', page.track | where: 'kind', 'component' | sort: 'order' %}\n"
    "{% for c in comps %}\n"
    "<a id=\"{{ c.slug }}\"></a>\n"
    "{{ c.content }}\n"
    "{% endfor %}\n",
    encoding="utf-8",
  )

  if not fragments_dir.exists():
    return

  md_files = sorted([p for p in fragments_dir.rglob("*.md") if p.is_file()])
  order = 1

  for p in md_files:
    raw = p.read_text(encoding="utf-8")
    title = extract_title(raw, p.stem)
    slug = slugify(p.stem)

    # drop leading H1 if present
    lines = raw.splitlines()
    if lines and lines[0].startswith("# "):
      raw = "\n".join(lines[1:]).lstrip("\n")

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

def write_index(site_dir: Path):
  (site_dir / "index.md").write_text(
    "---\n"
    "title: \"LLM HTML Component Benchmark\"\n"
    "layout: default\n"
    "---\n\n"
    "<div class=\"panel\">\n\n"
    "Pick a track:\n\n"
    "- [Minimal]({{ '/minimal' | relative_url }})\n"
    "- [Best Practice]({{ '/best-case' | relative_url }})\n"
    "- [Best Practice With Persona]({{ '/persona' | relative_url }})\n"
    "\n</div>\n",
    encoding="utf-8",
  )

def main():
  ap = argparse.ArgumentParser()
  ap.add_argument("--repo-root", default=".", help="Path to repo root")
  ap.add_argument("--out", default="site", help="Output Jekyll site dir")
  args = ap.parse_args()

  repo_root = Path(args.repo_root).resolve()
  site_dir = Path(args.out).resolve()

  write_site_scaffold(site_dir)
  write_intro_data(repo_root, site_dir)
  write_index(site_dir)

  for slug, title in TRACKS:
    build_track(repo_root, site_dir, slug, title)

if __name__ == "__main__":
  main()
