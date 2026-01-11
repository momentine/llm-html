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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; max-width: 400px;&quot;&gt;
  &lt;div&gt;
    &lt;div style=&quot;font-weight: 600; font-size: 16px; margin-bottom: 4px;&quot;&gt;Notifications&lt;/div&gt;
    &lt;div style=&quot;font-size: 14px; color: #666;&quot;&gt;Turn alerts on or off.&lt;/div&gt;
  &lt;/div&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 24px; transition: 0.4s;&quot;&gt;&lt;/span&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.4s;&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
input:checked + span {
  background-color: #2196F3;
}

input:checked + span + span {
  transform: translateX(26px);
}
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 16px; max-width: 400px;&quot;&gt;
  &lt;div&gt;
    &lt;div style=&quot;font-weight: 600; margin-bottom: 4px;&quot;&gt;Notifications&lt;/div&gt;
    &lt;div style=&quot;font-size: 14px; color: #666;&quot;&gt;Turn alerts on or off.&lt;/div&gt;
  &lt;/div&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;
      &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
  input[type=&quot;checkbox&quot;]:checked + span {
    background-color: #2196F3;
  }
  input[type=&quot;checkbox&quot;]:checked + span span {
    transform: translateX(26px);
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label style=&quot;display: flex; align-items: center; justify-content: space-between; max-width: 400px; padding: 16px; border: 1px solid #e0e0e0; border-radius: 8px; font-family: Arial, sans-serif;&quot;&gt;
    &lt;div&gt;
      &lt;div style=&quot;font-weight: 600; font-size: 16px; margin-bottom: 4px;&quot;&gt;Notifications&lt;/div&gt;
      &lt;div style=&quot;font-size: 14px; color: #666;&quot;&gt;Turn alerts on or off.&lt;/div&gt;
    &lt;/div&gt;
    &lt;input type=&quot;checkbox&quot; style=&quot;appearance: none; width: 50px; height: 26px; background-color: #ccc; border-radius: 13px; position: relative; cursor: pointer; transition: background-color 0.3s; outline: none;&quot; onchange=&quot;this.style.backgroundColor = this.checked ? &#x27;#4CAF50&#x27; : &#x27;#ccc&#x27;; this.nextElementSibling.style.transform = this.checked ? &#x27;translateX(24px)&#x27; : &#x27;translateX(0)&#x27;;&quot;&gt;
    &lt;span style=&quot;position: absolute; width: 22px; height: 22px; background-color: white; border-radius: 50%; top: 2px; left: 2px; transition: transform 0.3s; pointer-events: none; box-shadow: 0 2px 4px rgba(0,0,0,0.2);&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; max-width: 400px; padding: 16px; font-family: Arial, sans-serif;&quot;&gt;
  &lt;div&gt;
    &lt;div style=&quot;font-size: 16px; font-weight: 600; color: #333; margin-bottom: 4px;&quot;&gt;
      Notifications
    &lt;/div&gt;
    &lt;div style=&quot;font-size: 14px; color: #666;&quot;&gt;
      Turn alerts on or off.
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 26px; cursor: pointer;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 26px; transition: 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;span style=&quot;position: absolute; height: 20px; width: 20px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.3s;&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
input:checked + span {
  background-color: #4CAF50;
}

input:checked + span + span {
  transform: translateX(24px);
}
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div role=&quot;region&quot; aria-labelledby=&quot;toggle-label&quot;&gt;
  &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; max-width: 400px; padding: 16px; border: 1px solid #ccc; border-radius: 8px;&quot;&gt;
    &lt;div&gt;
      &lt;label id=&quot;toggle-label&quot; for=&quot;notifications-toggle&quot; style=&quot;display: block; font-weight: bold; margin-bottom: 4px;&quot;&gt;
        Notifications
      &lt;/label&gt;
      &lt;p id=&quot;toggle-description&quot; style=&quot;margin: 0; font-size: 14px; color: #666;&quot;&gt;
        Turn alerts on or off.
      &lt;/p&gt;
    &lt;/div&gt;
    &lt;button
      id=&quot;notifications-toggle&quot;
      role=&quot;switch&quot;
      aria-checked=&quot;false&quot;
      aria-describedby=&quot;toggle-description&quot;
      style=&quot;position: relative; width: 50px; height: 26px; background-color: #ccc; border: none; border-radius: 13px; cursor: pointer; transition: background-color 0.3s;&quot;
      onclick=&quot;this.setAttribute(&#x27;aria-checked&#x27;, this.getAttribute(&#x27;aria-checked&#x27;) === &#x27;false&#x27; ? &#x27;true&#x27; : &#x27;false&#x27;); this.style.backgroundColor = this.getAttribute(&#x27;aria-checked&#x27;) === &#x27;true&#x27; ? &#x27;#4CAF50&#x27; : &#x27;#ccc&#x27;; this.querySelector(&#x27;span&#x27;).style.transform = this.getAttribute(&#x27;aria-checked&#x27;) === &#x27;true&#x27; ? &#x27;translateX(24px)&#x27; : &#x27;translateX(0)&#x27;;&quot;&gt;
      &lt;span style=&quot;position: absolute; top: 3px; left: 3px; width: 20px; height: 20px; background-color: white; border-radius: 50%; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;/button&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider round&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;span&gt;Turn alerts on or off.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;toggle-switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
  &lt;span class=&quot;toggle-note&quot;&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
  Notifications
&lt;/label&gt;
&lt;small&gt;Turn alerts on or off.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
&lt;span&gt;Turn alerts on or off.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot; class=&quot;toggle-switch&quot;&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
  &lt;span class=&quot;toggle-slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;p class=&quot;toggle-note&quot;&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-switch&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-switch&quot; role=&quot;switch&quot; aria-described</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Toggle Switch&lt;/title&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-switch&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;notifications-switch&quot; aria-</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;toggle&quot;&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
  &lt;input type=&quot;checkbox&quot; class=&quot;toggle-input&quot; aria-describedby=&quot;notifications-note&quot; checked&gt;
  &lt;span class=&quot;toggle-slider&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;p id=&quot;notifications-note&quot; class=&quot;toggle-note&quot;&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Toggle Switch - Notifications&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg-off: #e5e7eb;
      --bg-on: #2563eb;
      --thumb: #ffffff;
      --text: #111827;
      --note: #6b7280;
      --focus: #3b82f6;
    }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
      color: var(--text);
      margin: 0;
      padding: 2rem;
      background: #fafafa;
    }
    .toggle-wrap {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      max-width: 28rem;
    }
    .toggle {
      position: relative;
      display: inline-block;
      width: 44px;
      height: 24px;
      flex: 0 0 auto;
    }
    .toggle input[type=&quot;checkbox&quot;] {
      position: absolute;
      opacity: 0;
      width: 1px;
      height: 1px;
      margin: 0;
      padding: 0;
      border: 0;
    }
    .toggle .track {
      position: absolute;
      inset: 0;
      background: var(--bg-off);
      border-radius: 9999px;
      transition:</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #111827;
      --muted: #6</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 44px;
      --switch-height: 24px;
      --switch-padding: 3px;
      --knob-size: 18px;
      --track-off: #c8c8c8;
      --track-on: #2d7dff;
      --knob: #ffffff;
      --focus: #5b9dff;
      --text: #1f2937;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 24px;
      color: var(--text);
      background: #f7fafc;
    }

    .field {
      display: grid;
      gap: 8px;
      max-width: 360px;
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }

    .label-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .label-row label {
      font-weight: 600;
    }

    /* Visually hidden but accessible checkbox */
    .visually-hidden {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0 0 0 0</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Notifications Switch&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 48px;
      --switch-height: 28px;
      --switch-padding: 3px;
      --knob-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --on-color: #2563eb;   /* blue-600 */
      --off-color: #cbd5e1;  /* slate-300 */
      --knob-color: #ffffff;
      --text-color: #0f172a; /* slate-900 */
      --focus-color: #1d4ed8; /* blue-700 */
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;,</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Notifications &lt;input type=&quot;checkbox&quot;&gt;&lt;span&gt;Toggle switch&lt;/span&gt;&lt;/label&gt;&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Notifications &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;&lt;/label&gt;&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;div id=&quot;note&quot;&gt;Turn alerts on or off.&lt;/div&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-describedby=&quot;note&quot; aria-checked=&quot;false&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; name=&quot;notifications-toggle&quot;&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot; /&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;div&gt;
    &lt;span id=&quot;notifications-description&quot;&gt;Turn alerts on or off.&lt;/span&gt;
    &lt;button 
      role=&quot;switch&quot; 
      aria-checked=&quot;false&quot; 
      aria-labelledby=&quot;notifications-label&quot; 
      aria-describedby=&quot;notifications-description&quot;
      id=&quot;notifications-toggle&quot;
    &gt;
      &lt;span&gt;Off&lt;/span&gt;
      &lt;span&gt;On&lt;/span&gt;
    &lt;/button&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot;&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;span&gt;Turn alerts on or off.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-describedby=&quot;note&quot;&gt;
  &lt;span id=&quot;note&quot;&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
