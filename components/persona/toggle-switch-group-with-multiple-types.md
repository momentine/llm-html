<details>
  <summary><strong>Toggle Switch Group with Multiple Types</strong></summary>
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
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Notification Types&lt;/legend&gt;

    &lt;label class=&quot;toggle&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notifications&quot; value=&quot;email&quot; checked&gt;
      &lt;span class=&quot;switch&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label-text&quot;&gt;Email&lt;/span&gt;
    &lt;/label&gt;

    &lt;label class=&quot;toggle&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notifications&quot; value=&quot;sms&quot;&gt;
      &lt;span class=&quot;switch&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label-text&quot;&gt;SMS&lt;/span&gt;
    &lt;/label&gt;

    &lt;label class=&quot;toggle&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notifications&quot; value=&quot;push&quot; checked&gt;
      &lt;span class=&quot;switch&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label-text&quot;&gt;Push&lt;/span&gt;
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;

&lt;style&gt;
  fieldset { border: 0; margin: 0; padding: 0; }
  legend { font-weight: 600; margin-bottom: .5rem; }
  .toggle {
    display: inline-flex;
    align-items: center;
    gap: .5rem;
    margin-right: 1rem;
    cursor: pointer;
    user-select: none;
  }
  .toggle input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
  }
  .switch {
    width: 42px;
    height: 24px;
    background: #c9ced6;
    border-radius: 999px;
    position: relative;
    transition: background .2s ease;
    flex-shrink: 0;
  }
  .switch::after {
    content: &quot;&quot;;
    width: 18px;
    height: 18px;
    background: #fff;
    border-radius: 50%;
    position: absolute;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types Toggle Group&lt;/title&gt;
  &lt;style&gt;
    /* Optional visual styling for the toggle switches */
    .toggle {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      cursor: pointer;
      user-select: none;
    }
    .toggle input[type=&quot;checkbox&quot;] {
      appearance: none;
      width: 44px;
      height: 24px;
      border-radius: 999px;
      position: relative;
      outline: none;
      background: #c7c7c7;
      transition: background 0.2s ease;
    }
    .toggle input[type=&quot;checkbox&quot;]::before {
      content: &quot;&quot;;
      position: absolute;
      top: 3px;
      left: 3px;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #fff;
      transition: transform 0.2s ease;
      box-shadow: 0 1px 2px rgba(0,0,0,0.25);
    }
    .toggle input[type=&quot;checkbox&quot;]:checked {
      background: #2563eb; /* blue */
    }
    .toggle input[type=&quot;checkbox&quot;]:checked::before {
      transform: translateX(20px);
    }
    .toggle input[type=&quot;checkbox&quot;]:focus-visible {
      box-shadow: 0 0 0 3px rgba(37,99,235,0.35);
    }
    fieldset {
      border: 1px solid #d1d5db;
      border-radius: 8px;
      padding: 1rem;
      max</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Notification Types&lt;/legend&gt;

    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_types&quot; value=&quot;email&quot; checked aria-label=&quot;Email&quot;&gt;
      &lt;span class=&quot;slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label&quot;&gt;Email&lt;/span&gt;
    &lt;/label&gt;

    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_types&quot; value=&quot;sms&quot; aria-label=&quot;SMS&quot;&gt;
      &lt;span class=&quot;slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label&quot;&gt;SMS&lt;/span&gt;
    &lt;/label&gt;

    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_types&quot; value=&quot;push&quot; aria-label=&quot;Push&quot;&gt;
      &lt;span class=&quot;slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;span class=&quot;label&quot;&gt;Push&lt;/span&gt;
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;

&lt;style&gt;
  fieldset {
    border: 0;
    padding: 0;
    margin: 0;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
  }

  legend {
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  .switch {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    margin: 0.4rem 0;
    cursor: pointer;
    user-select: none;
  }

  .switch input[type=&quot;checkbox&quot;] {
    position: absolute;
    opacity: 0;
    width: 1px;
    height: 1px;
    overflow: hidden;
    clip: rect(0 0 0 0);
    white-space: nowrap;
    clip-path: inset(50%);
  }</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types - Toggle Switches&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --border: #d0d7de;
      --text: #0f172a;
      --muted: #64748b;
      --track-off: #cbd5e1;
      --track-on: #22c55e;
      --knob: #ffffff;
      --focus: #2563eb;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 2rem;
      background: var(--bg);
      color: var(--text);
      font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.4;
    }

    fieldset {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem 1.25rem 1.25rem;
      max-width: 480px;
    }

    legend {
      padding: 0 .5rem;
      font-weight: 600;
    }

    .hint {
      margin: .25rem 0 1rem;
      color: var(--muted);
      font-size: .95rem;
    }

    .toggle {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: .75rem;
      padding: .5rem 0;
    }

    .toggle + .toggle</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types - Accessible Toggle Switches&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --fg: #0b1324;
      --muted: #5b6472;
      --border: #c8ced6;
      --track-off: #d7dce2;
      --track-on: #1e7a46;
      --thumb: #ffffff;
      --focus: #005fcc;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0f1216;
        --fg: #e7e9ee;
        --muted: #a9b0bc;
        --border: #2a313a;
        --track-off: #3a424e;
        --track-on: #2ea86b;
        --thumb: #f3f5f9;
        --focus: #7db3ff;
      }
    }

    body {
      margin: 0;
      background: var(--bg);
      color: var(--fg);
      font: 16px/1.5 system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      padding: 2rem;
    }

    fieldset {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem 1rem 0.75rem;
      max-width: 28rem;
    }</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
