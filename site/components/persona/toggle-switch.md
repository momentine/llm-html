---
title: "toggle-switch"
slug: toggle-switch
track: persona
kind: component
order: 57
---

<details>
  <summary><strong>Toggle Switch</strong></summary>
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
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;notifications-toggle&quot;&gt;
        Notifications
        &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
    &lt;/label&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label style=&quot;display: inline-flex; align-items: center; cursor: pointer;&quot;&gt;
  &lt;input type=&quot;checkbox&quot; style=&quot;appearance: none; width: 50px; height: 26px; background-color: #ccc; border-radius: 13px; position: relative; cursor: pointer; transition: background-color 0.3s;&quot; onchange=&quot;this.style.backgroundColor = this.checked ? &#x27;#4CAF50&#x27; : &#x27;#ccc&#x27;;&quot;&gt;
  &lt;style&gt;
    input[type=&quot;checkbox&quot;]:checked::before {
      transform: translateX(24px);
    }
    input[type=&quot;checkbox&quot;]::before {
      content: &#x27;&#x27;;
      position: absolute;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background-color: white;
      top: 2px;
      left: 2px;
      transition: transform 0.3s;
    }
  &lt;/style&gt;
  &lt;span style=&quot;margin-left: 10px; font-family: Arial, sans-serif; font-size: 16px;&quot;&gt;Notifications&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  &lt;input type=&quot;checkbox&quot; /&gt;
  &lt;span&gt;Notifications&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;
      &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
  input:checked + span {
    background-color: #2196F3;
  }
  
  input:checked + span span {
    transform: translateX(26px);
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div role=&quot;region&quot; aria-labelledby=&quot;notifications-label&quot;&gt;
  &lt;label id=&quot;notifications-label&quot; for=&quot;notifications-toggle&quot;&gt;
    &lt;span&gt;Notifications&lt;/span&gt;
  &lt;/label&gt;
  &lt;button
    id=&quot;notifications-toggle&quot;
    role=&quot;switch&quot;
    aria-checked=&quot;false&quot;
    aria-labelledby=&quot;notifications-label&quot;
    type=&quot;button&quot;
  &gt;
    &lt;span aria-hidden=&quot;true&quot;&gt;OFF&lt;/span&gt;
  &lt;/button&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider round&quot;&gt;&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;toggle-switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
    &lt;input type=&quot;checkbox&quot;&gt;
    &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
    Notifications
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot; aria-label=&quot;Toggle notifications&quot;&gt;
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; font-family: sans-serif;&quot;&gt;
  &lt;label for=&quot;notification-switch&quot; style=&quot;margin</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-switch&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-switch&quot; role=&quot;switch&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; aria-label=&quot;Notifications&quot;&gt;
  &lt;span class=&quot;slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
  &lt;span class=&quot;label-text&quot;&gt;Notifications&lt;/span&gt;
&lt;/label&gt;

&lt;style&gt;
  .switch {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    cursor: pointer;
    user-select: none;
    font: 14px/1.2 system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    color: #111827;
  }

  .switch input[type=&quot;checkbox&quot;] {
    position: absolute;
    opacity: 0;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
  }

  .slider {
    position: relative;
    width: 44px;
    height: 24px;
    background: #d1d5db;
    border-radius: 999px;
    transition: background-color .2s ease;
    box-shadow: inset 0 0 0 1px rgba(0,0,0,.06);
  }

  .slider::after {
    content: &quot;&quot;;
    position: absolute;
    top: 3px;
    left: 3px;
    width: 18px;
    height: 18px;
    background: #ffffff;
    border-radius: 50%;
    box-shadow: 0 1px 2px rgba(0,0,0,.2);
    transition: transform .2s ease;
  }

  .switch input[type=&quot;checkbox&quot;]:checked + .slider {
    background: #2563eb;
    box-shadow: inset 0 0 0 1px rgba(0,0,0,.04);
  }

  .switch input[type=&quot;checkbox&quot;]:checked + .slider::after {
    transform: translateX(20px);
  }

  .switch input[type=&quot;checkbox&quot;]:focus-visible + .slider {
    outline: 2px solid #2563eb;
    outline-offset: 2px;
  }

  .label-text {
    color: #111827;
  }
&lt;/style&gt;

&lt;script&gt;
  (function () {
    const toggle = document.getElementById(&#x27;notifications-toggle&#x27;);
    if (!toggle) return;

    // Keep ARIA in sync</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Toggle switch: Notifications&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;toggle-notifications&quot;&gt;
      &lt;input
        type=&quot;checkbox&quot;
        id=&quot;toggle-notifications&quot;
        name=&quot;notifications&quot;
        value=&quot;enabled&quot;
        aria-label=&quot;Notifications&quot;
      /&gt;
      Notifications
    &lt;/label&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 48px;
      --switch-height: 28px;
      --switch-padding: 3px;
      --knob-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --on-color: #2563eb;
      --off-color: #cbd5e1;
      --text-color: #0f172a;
    }

    body {
      margin: 0;
      padding: 24px;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      color: var(--text-color);
      background: #f8fafc;
    }

    .switch {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      user-select: none;
    }

    /* Visually hidden but accessible */
    .switch input[type=&quot;checkbox&quot;] {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0 0 0 0);
      white-space: nowrap;
      border: 0;
    }

    .slider {
      position: relative;
      width: var(--switch-width);
      height: var(--switch-height);
      background: var(--off-color);
      border-radius: var(--switch-height);
      transition: background-color .2s ease;
      outline: none;
      cursor: pointer;
      box-shadow: inset 0 0 0 1px rgba(15, 23, 42, 0.06);
    }

    .slider::after {
      content: &quot;&quot;;
      position: absolute;
      top: var(--switch</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 46px;
      --switch-height: 26px;
      --switch-padding: 3px;
      --knob-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --switch-off: #c9ced6;
      --switch-on: #2563eb; /* blue-600 */
      --switch-on-hover: #1d4ed8; /* blue-700 */
      --text-color: #111827; /* gray-900 */
      --focus-color: #2563eb;
    }

    * { box-sizing: border-box; }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      margin: 0;
      padding: 24px;
      color: var(--text-color);
      background: #f9fafb;
    }

    .field {
      display: flex;
      align-items: center;
      gap: 12px;
      user-select: none;
      cursor: pointer;
    }

    .visually-hidden {
      position: absolute !important;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0 0 0 0);
      white-space: nowrap;
      border: 0;
    }

    .switch {
      position: relative;
      width: var(--switch-width);
      height: var(--switch-height);
      background: var(--switch-off);
      border-radius: 9999</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root{
      --switch-width: 52px;
      --switch-height: 32px;
      --switch-padding: 3px;
      --thumb-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --track-on: #1d9bf0;
      --track-off: #d0d7de;
      --thumb: #ffffff;
      --thumb-border: rgba(0,0,0,.15);
      --focus-ring: 2px solid #005fcc;
      --text: #111827;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      margin: 0;
      padding: 2rem;
      color: var(--text);
      background: #fff;
    }

    .field {
      display: inline-flex;
      align-items: center;
      gap: .75rem;
    }

    .label {
      font-weight: 600;
      user-select: none;
    }

    /* Visually hidden helper */
    .sr-only {
      position: absolute !important;
      width: 1px !important;
      height: 1px !important;
      padding: 0 !important;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; /&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; name=&quot;notifications&quot; /&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Notification Preferences&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; name=&quot;notifications&quot; aria-describedby=&quot;notifications-toggle-description&quot;&gt;
      &lt;span&gt;Notifications</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; class=&quot;toggle-switch&quot;&gt;
&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-container&quot;&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
  &lt;label class=&quot;toggle-switch&quot;&gt;
    &lt;input type=&quot;checkbox&quot;&gt;
    &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-container&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; class=&quot;toggle-label&quot;&gt;
    Notifications
  &lt;/label&gt;
  &lt;button
    type=&quot;button&quot;
    role=&quot;switch&quot;
    aria-checked=&quot;false&quot;
    aria-labelledby=&quot;notifications-label&quot;
    id=&quot;notifications-toggle&quot;
    class=&quot;toggle-switch&quot;
  &gt;
    &lt;span class=&quot;toggle-track&quot;&gt;
      &lt;span class=&quot;toggle-thumb&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
  &lt;/button&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot; name=&quot;notifications&quot;&gt;
&lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

