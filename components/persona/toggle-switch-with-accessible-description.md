<details>
  <summary><strong>Toggle Switch with Accessible Description</strong></summary>
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
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;fieldset style=&quot;border:0;padding:0;margin:0;&quot;&gt;
    &lt;legend style=&quot;position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden;&quot;&gt;Notifications&lt;/legend&gt;

    &lt;div role=&quot;switch&quot; aria-checked=&quot;false&quot; tabindex=&quot;0&quot; data-switch class=&quot;switch&quot; id=&quot;notifications-switch&quot; aria-describedby=&quot;notifications-note&quot;&gt;
      &lt;span class=&quot;label&quot;&gt;Notifications&lt;/span&gt;
      &lt;span class=&quot;note&quot; id=&quot;notifications-note&quot;&gt;Turn alerts on or off.&lt;/span&gt;
      &lt;span class=&quot;slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notifications&quot; value=&quot;on&quot; hidden /&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;

&lt;style&gt;
  .switch {
    --w: 52px;
    --h: 28px;
    --p: 3px;
    --knob: 22px;
    --accent: #2563eb;
    --track-off: #d1d5db;
    --track-on: #93c5fd;
    --text: #111827;
    --muted: #6b7280;

    display: inline-flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
    user-select: none;
    font: 14px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    color: var(--text);
  }
  .switch .label {
    font-weight: 600;
  }
  .switch .note {
    color: var(--muted);
  }
  .switch .slider {
    width: var(--w);
    height: var(--h);
    background: var(--track-off);
    border-radius: var(--h);
    position: relative;
    transition: background .2s ease;
    box-shadow: inset 0 0</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
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
      --bg-off: #e5e7eb;
      --bg-on: #16a34a;
      --knob: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --focus: #2563eb;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      color: var(--text);
      padding: 24px;
      line-height: 1.5;
    }

    .field {
      display: grid;
      gap: 8px;
      max-width: 420px;
    }

    .row {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* Visually hidden but accessible checkbox */
    .visually-hidden {
      position: absolute !important;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #f6f7f9;
      --text: #111827;
      --muted: #6b7280;
      --border: #d1d5db;
      --track-off: #e5e7eb;
      --track-on: #10b981;
      --knob: #ffffff;
      --focus: #2563eb;
    }
    body {
      margin: 0;
      min-height: 100vh;
      display: grid;
      place-items: center;
      background: var(--bg);
      color: var(--text);
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.4;
    }
    .field {
      display: grid;
      gap: 0.5rem;
      width: min(520px, 92vw);
    }
    .label-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .label-row label {
      font-weight: 600;
    }
    .note {
      color: var(--muted);
      font-size: 0.925rem;
      margin: 0;
    }
    .switch {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      user-select: none;
      cursor: pointer;
    }
    .switch input[type=&quot;checkbox&quot;] {
      appearance: none</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
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
      --bg: #f3f4f6;
      --border: #d1d5db;
      --knob: #ffffff;
      --on: #2563eb;
      --text: #111827;
      --muted: #6b7280;
      --focus: #93c5fd;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 2rem;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      background: #ffffff;
      color: var(--text);
      line-height: 1.5;
    }
    .field {
      display: grid;
      gap: 0.5rem;
      max-width: 28rem;
    }
    .label-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }
    label {
      font-weight: 600;
    }
    .hint {
      color: var(--muted);
      font-size: 0.9375rem;
    }

    /* Accessible visually-hidden utility */
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    /* Switch */
    .switch {
      position: relative;
      display: inline-block;
      width: 46px;
      height: 26px;
      flex: 0 0 auto;
    }
    .switch input {
      position: absolute;
      opacity: 0;
      width: 0;
      height: 0;
    }
    .slider {
      position: absolute;
      inset: 0;
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 9999px;
      transition: background-color .15s ease, border-color .15s ease, box-shadow .15s ease;
    }
    .slider::before {
      content: &quot;&quot;;
      position: absolute;
      height: 20px;
      width: 20px;
      left: 3px;
      top: 50%;
      transform: translateY(-50%);
      background:</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;body&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; aria-describedby=&quot;notifications-note&quot;&gt;
    &lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
    &lt;p id=&quot;notifications-note&quot;&gt;Turn alerts on or off.&lt;/p&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
