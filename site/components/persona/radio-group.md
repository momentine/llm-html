---
title: "radio-group"
slug: radio-group
track: persona
kind: component
order: 31
---

<details>
  <summary><strong>Radio Group</strong></summary>
<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Variant</th>
      <th>Prompt</th>
      <th>Output</th>
      <th>File Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    Light
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    Dark
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    High Contrast
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    light
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    dark
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    high contrast
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    Light
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    Dark
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    High Contrast
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div role=&quot;radiogroup&quot; aria-labelledby=&quot;theme-legend&quot;&gt;
    &lt;span id=&quot;theme-legend&quot; hidden&gt;Theme&lt;/span&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High Contrast
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;Light&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;Dark&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt;High Contrast&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt; Light&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt;
    &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High contrast&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;theme-high-contrast&quot;&gt;High contrast&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt;
    &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; id=&quot;theme-light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; id=&quot;theme-dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; id=&quot;theme-high-contrast&quot;&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot; data-theme=&quot;light&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Theme Selector&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --surface: #f3f4f6;
      --border: #e5e7eb;
      --accent: #2563eb;
      --accent-contrast: #ffffff;
      --focus: #f59e0b;
    }

    html[data-theme=&quot;dark&quot;] {
      --bg: #0b0f14;
      --text: #e5e7eb;
      --muted: #9ca3af;
      --surface: #111827;
      --border: #374151;
      --accent: #60a5fa;
      --accent-contrast: #0b0f14;
      --focus: #f59e0b;
    }

    html[data-theme=&quot;hc&quot;] {
      --bg: #000000;
      --text: #ffffff;
      --muted: #ffffff;
      --surface: #000000;
      --border: #ffffff;
      --accent: #ffff00;
      --accent-contrast: #000000;
      --focus: #00ff00;
    }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; id=&quot;theme-light&quot; checked&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; id=&quot;theme-dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; id=&quot;theme-hc&quot;&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; checked /&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; /&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; /&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot; data-theme=&quot;light&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;meta name=&quot;color-scheme&quot; content=&quot;light dark&quot; /&gt;
  &lt;title&gt;Accessible Theme Radio Group&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --border: #d1d5db;
      --focus: #2563eb;
      --radio-bg: #ffffff;
      --radio-border: #374151;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0b0f14;
        --text: #e5e7eb;
        --muted: #9ca3af;
        --border: #374151;
        --focus: #60a5fa;
        --radio-bg: #0b0f14;
        --radio-border: #9ca3af;
      }
    }
    html[data-theme=&quot;light&quot;] {
      color-scheme: light;
      --bg: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --border: #d1d5db;
      --focus: #2563eb;
      --radio-bg: #ffffff;
      --radio-border: #374151;
    }
    html[data</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; /&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; /&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; /&gt;
      High Contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High Contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Theme
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High Contrast
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; checked&gt;
      &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  
  &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  
  &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;high contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label for=&quot;light&quot;&gt;&lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light&lt;/label&gt;
  &lt;label for=&quot;dark&quot;&gt;&lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;&lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

