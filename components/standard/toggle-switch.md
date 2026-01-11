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
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 16px; max-width: 400px; font-family: Arial, sans-serif;&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; style=&quot;font-size: 16px; color: #333;&quot;&gt;Notifications&lt;/label&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;&lt;/span&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label style=&quot;display: inline-flex; align-items: center; cursor: pointer; gap: 10px;&quot;&gt;
  &lt;span style=&quot;font-family: Arial, sans-serif; font-size: 16px; color: #333;&quot;&gt;Notifications&lt;/span&gt;
  &lt;input type=&quot;checkbox&quot; style=&quot;display: none;&quot; id=&quot;notificationToggle&quot;&gt;
  &lt;div style=&quot;width: 50px; height: 26px; background-color: #ccc; border-radius: 13px; position: relative; transition: background-color 0.3s;&quot; onclick=&quot;this.previousElementSibling.checked = !this.previousElementSibling.checked; this.style.backgroundColor = this.previousElementSibling.checked ? &#x27;#4CAF50&#x27; : &#x27;#ccc&#x27;; this.firstElementChild.style.transform = this.previousElementSibling.checked ? &#x27;translateX(24px)&#x27; : &#x27;translateX(0)&#x27;;&quot;&gt;
    &lt;div style=&quot;width: 22px; height: 22px; background-color: white; border-radius: 50%; position: absolute; top: 2px; left: 2px; transition: transform 0.3s;&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label style=&quot;display: inline-flex; align-items: center; cursor: pointer; gap: 10px;&quot;&gt;
  &lt;span style=&quot;font-size: 16px; font-family: Arial, sans-serif;&quot;&gt;Notifications&lt;/span&gt;
  &lt;input type=&quot;checkbox&quot; style=&quot;display: none;&quot; class=&quot;toggle-input&quot;&gt;
  &lt;span style=&quot;position: relative; width: 50px; height: 26px; background-color: #ccc; border-radius: 13px; transition: background-color 0.3s;&quot;&gt;
    &lt;span style=&quot;position: absolute; top: 3px; left: 3px; width: 20px; height: 20px; background-color: white; border-radius: 50%; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
  &lt;/span&gt;
&lt;/label&gt;

&lt;style&gt;
  .toggle-input:checked + span {
    background-color: #4CAF50;
  }
  .toggle-input:checked + span span {
    transform: translateX(24px);
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; gap: 12px;&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; style=&quot;font-size: 16px; cursor: pointer; user-select: none;&quot;&gt;
    Notifications
  &lt;/label&gt;
  &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px; cursor: pointer;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
    &lt;span style=&quot;position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 24px; transition: 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;span style=&quot;position: absolute; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.3s;&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
  #notifications-toggle:checked + span {
    background-color: #2196F3;
  }
  #notifications-toggle:checked + span + span {
    transform: translateX(26px);
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Notifications Toggle&lt;/title&gt;
    &lt;style&gt;
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, &#x27;Segoe UI&#x27;, Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f5f5f5;
            padding: 20px;
        }

        .toggle-container {
            background: white;
            padding: 32px;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            width: 100%;
        }

        .toggle-wrapper {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 16px;
        }

        .toggle-label {
            font-size: 16px;
            font-weight: 500;
            color: #333;
            cursor: pointer;
            user-select: none;
        }

        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 52px;
            height: 28px;
            flex-shrink: 0;
        }

        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
            position: absolute;
        }

        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            transition: 0.3s;
            border-radius: 28px;
        }

        .slider:before {
            position: absolute;
            content: &quot;&quot;;
            height: 20px;
            width: 20px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: 0.3s;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: #4CAF50;
        }

        input:focus + .slider {
            outline: 2px solid #2196F3;
            outline-offset: 2px;
        }

        input:checked + .slider:before {
            transform: translateX(24px);
        }

        input:disabled + .slider {
            opacity: 0.5;
            cursor: not-allowed;
        }

        .status-text {
            font-size: 14px;
            color: #666;
            margin-top: 12px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class=&quot;toggle-container&quot;&gt;
        &lt;div class=&quot;toggle-wrapper&quot;&gt;
            &lt;label for=&quot;notifications-toggle&quot; class=&quot;toggle-label&quot;&gt;Notifications&lt;/label&gt;
            &lt;label class=&quot;toggle-switch&quot;&gt;
                &lt;input 
                    type=&quot;checkbox&quot; 
                    id=&quot;notifications-toggle&quot; 
                    role=&quot;switch&quot;
                    aria-checked=&quot;false&quot;
                    aria-label=&quot;Toggle notifications&quot;
                &gt;
                &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div class=&quot;status-text&quot; id=&quot;status-text&quot; aria-live=&quot;polite&quot;&gt;Notifications are currently off&lt;/div&gt;
    &lt;/div&gt;

    &lt;script&gt;
        const toggle = document.getElementById(&#x27;notifications-toggle&#x27;);
        const statusText = document.getElementById(&#x27;status-text&#x27;);

        toggle.addEventListener(&#x27;change&#x27;, function() {
            const isChecked = this.checked;
            this</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  &lt;span class=&quot;slider round&quot;&gt;&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot; style=&quot;display: inline-flex; align-items: center; gap: 0.5rem; cursor: pointer;&quot;&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;display: none;&quot;&gt;
  &lt;span style=&quot;width: 3rem; height: 1.5rem; background-color: #ccc; border-radius: 0.75rem; position: relative; transition: background-color 0.3s;&quot;&gt;
    &lt;span style=&quot;width: 1.25rem; height: 1.25rem; background-color: white; border-radius: 50%; position: absolute; top: 0.125rem; left: 0.125rem; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
  &lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;toggle-switch&quot; aria-label=&quot;Toggle Notifications&quot;&gt;
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-switch-container&quot;&gt;
    &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
    &lt;label class=&quot;switch&quot;&gt;
        &lt;input type</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;switch-container&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;title&gt;Notifications Toggle&lt;/title&gt;
&lt;body&gt;
  &lt;label for=&quot;notifications&quot; class=&quot;switch&quot; style=&quot;display:inline-flex;align-items:center;gap:.6rem;cursor:pointer;font:16px system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,&#x27;Noto Sans&#x27;,sans-serif;&quot;&gt;
    &lt;input id=&quot;notifications&quot; type=&quot;checkbox&quot; checked aria-label=&quot;Notifications&quot; style=&quot;position:absolute;opacity:0;width:0;height:0;&quot;&gt;
    &lt;span class=&quot;slider&quot; style=&quot;position:relative;display:inline-block;width:48px;height:28px;background:#d0d7de;border-radius:999px;transition:background .2s ease;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);&quot;&gt;
      &lt;span class=&quot;knob&quot; style=&quot;position:absolute;top:3px;left:3px;width:22px;height:22px;background:#fff;border-radius:50%;box-shadow:0 1px 2px rgba(0,0,0,.25);transition:transform .2s ease;&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
    &lt;span class=&quot;label-text&quot; style=&quot;user-select:none;&quot;&gt;Notifications&lt;/span&gt;
  &lt;/label&gt;
  &lt;script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Toggle switch: Notifications&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg-off: #e5e7eb;
      --bg-on: #16a34a;
      --knob: #ffffff;
      --track-border: #d1d5db;
      --text: #111827;
      --muted: #6b7280;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 24px;
      color: var(--text);
      background: #f9fafb;
    }

    .switch-row {
      display: flex;
      align-items: center;
      gap: 12px;
      max-width: 520px;
      margin: 0 auto;
      padding: 16px;
      background: #ffffff;
      border: 1px solid #e5e7eb;
      border-radius:</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 44px;
      --switch-height: 24px;
      --knob-size: 18px;
      --knob-gap: 3px;
      --track-on: #10b981;   /* emerald-500 */
      --track-off: #d1d5db;  /* gray-300 */
      --knob: #ffffff;
      --focus: #2563eb;      /* blue-600 */
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      margin: 0;
      padding: 24px;
      background: #f9fafb;
      color: #111827;
    }

    .field {
      display: flex;
      align-items: center;
      gap: 12px;
      max-width: 420px;
      margin: 0 auto;
    }

    .label {</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notifications Toggle&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 44px;
      --switch-height: 24px;
      --switch-padding: 3px;
      --knob-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --color-bg: #e5e7eb;
      --color-bg-checked: #2563eb;
      --color-knob: #ffffff;
      --color-text: #111827;
      --focus-ring: 2px solid #2563eb;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --color-bg: #374151;
        --color-bg-checked: #3b82f6;
        --color-knob: #ffffff;
        --color-text: #f9fafb;
        --focus-ring: 2px solid #93c5fd;
      }
    }

    * { box-sizing: border-box; }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      color: var(--color-text);
      margin: 0;
      padding: 24px;
      display: grid;
      place-items: start center;
      background: Canvas;
    }

    .row {
      display: inline-flex;
      align-items: center;
      gap: 12px;
    }

    .switch {
      position: relative;
      display: inline-flex;
      align-items: center;
      width:</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Toggle Switch - Notifications&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 46px;
      --switch-height: 26px;
      --switch-padding: 3px;
      --thumb-size: calc(var(--switch-height) - var(--switch-padding) * 2);
      --track-off: #c8c8c8;
      --track-on: #2563eb;
      --thumb: #ffffff;
      --text: #111827;
      --text-muted: #4b5563;
      --focus: #111827;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
      color: var(--text);
      background: #ffffff;
      margin: 0;
      padding: 2rem;
    }

    .row {
      display: flex;
      align-items: center;
      gap</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;
    Notifications
    &lt;input type=&quot;checkbox&quot;&gt;
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-label=&quot;Notifications&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; aria-label=&quot;Notifications&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
    id=&quot;notifications-toggle&quot;
    role=&quot;switch&quot;
    aria-checked=&quot;false&quot;
    aria-labelledby=&quot;notifications-label&quot;
    class=&quot;toggle-switch&quot;
    onclick=&quot;toggleNotifications()&quot;
  &gt;
    &lt;span class=&quot;toggle-track&quot;&gt;
      &lt;span class=&quot;toggle-thumb&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
    &lt;span class=&quot;sr-only&quot;&gt;Toggle notifications&lt;/span&gt;
  &lt;/button&gt;
&lt;/div&gt;

&lt;script&gt;
  function toggleNotifications() {
    const toggle = document.getElementById(&#x27;notifications-toggle&#x27;);
    const isChecked = toggle.getAttribute(&#x27;aria-checked&#x27;) === &#x27;true&#x27;;
    toggle.setAttribute(&#x27;aria-checked&#x27;, !isChecked);
    toggle.setAttribute(&#x27;aria-label&#x27;, isChecked ? &#x27;Notifications off&#x27; : &#x27;Notifications on&#x27;);
  }
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/qwen-qwen3-coder/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot;&gt;
&lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
  Notifications
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
