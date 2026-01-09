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
    &lt;title&gt;Notifications Toggle&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label&gt;
        &lt;span&gt;Notifications&lt;/span&gt;
        &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    &lt;/label&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Toggle Switch: Notifications&lt;/title&gt;
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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }

        .container {
            background: white;
            padding: 3rem;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .toggle-wrapper {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .toggle-label {
            font-size: 1.25rem;
            font-weight: 600;
            color: #333;
            cursor: pointer;
            user-select: none;
        }

        .toggle-switch {
            position: relative;
            width: 60px;
            height: 30px;
            cursor: pointer;
        }

        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .slider {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: #ccc;
            border-radius: 30px;
            transition: 0.3s;
        }

        .slider:before {
            position: absolute;
            content: &quot;&quot;;
            height: 22px;
            width: 22px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            border-radius: 50%;
            transition: 0.3s;
        }

        input:checked + .slider {
            background-color: #667eea;
        }

        input:checked + .slider:before {
            transform: translateX(30px);
        }

        .status-text {
            margin-top: 1rem;
            font-size: 0.95rem;
            color: #666;
            text-align: center;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class=&quot;container&quot;&gt;
        &lt;div class=&quot;toggle-wrapper&quot;&gt;
            &lt;label class=&quot;toggle-label&quot; for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
            &lt;label class=&quot;toggle-switch&quot;&gt;
                &lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot;&gt;
                &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div class=&quot;status-text&quot; id=&quot;status&quot;&gt;Notifications are off&lt;/div&gt;
    &lt;/div&gt;

    &lt;script&gt;
        const toggle = document.getElementById(&#x27;notifications&#x27;);
        const status = document.getElementById(&#x27;status&#x27;);

        toggle.addEventListener(&#x27;change&#x27;, function() {
            if (this.checked) {
                status.textContent = &#x27;Notifications are on&#x27;;
            } else {
                status.textContent = &#x27;Notifications are off&#x27;;
            }
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
    &lt;span&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;

&lt;style&gt;
label {
  display: inline-block;
  position: relative;
  width: 50px;
  height: 24px;
  margin-left: 10px;
}

label input {
  opacity: 0;
  width: 0;
  height: 0;
}

label span {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: 0.3s;
  border-radius: 24px;
}

label span:before {
  position: absolute;
  content: &quot;&quot;;
  height: 18px;
  width: 18px;
  left: 3px;
  bottom: 3px;
  background-color: white;
  transition: 0.3s;
  border-radius: 50%;
}

label input:checked + span {
  background-color: #2196F3;
}

label input:checked + span:before {
  transform: translateX(26px);
}
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;notifications-toggle&quot;&gt;
        &lt;span&gt;Notifications&lt;/span&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
    &lt;/label&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
&lt;/label&gt;
&lt;span&gt;Notifications&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;span&gt;Notifications&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; gap: 12px;&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; style=&quot;font-family: Arial, sans-serif; font-size: 16px; color: #333;&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;display: none;&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; style=&quot;width: 50px; height: 24px; background-color: #ccc; border-radius: 12px; position: relative; cursor: pointer; transition: background-color 0.3s;&quot;&gt;
    &lt;span style=&quot;width: 20px; height: 20px; background-color: white; border-radius: 50%; position: absolute; top: 2px; left: 2px; transition: left 0.3s;&quot;&gt;&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;span&gt;Notifications&lt;/span&gt;

&lt;style&gt;
.switch {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.switch input {
  opacity: 0;
  width: 0;
  height: 0;
}

.slider {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: #ccc;
  transition: .4s;
  border-radius: 34px;
}

.slider:before {
  position: absolute;
  content: &quot;&quot;;
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #2196F3;
}

input:checked + .slider:before {
  transform: translateX(26px);
}
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; tabindex=&quot;0&quot;&gt;
  &lt;span class=&quot;toggle-label&quot;&gt;Notifications&lt;/span&gt;
  &lt;div class=&quot;toggle-track&quot;&gt;
    &lt;div class=&quot;toggle-thumb&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
&lt;/label&gt;

&lt;style&gt;
  label[role=&quot;switch&quot;] {
    display: flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
    font-family: sans-serif;
    font-size: 16px;
    color: #333;
  }
  
  .toggle-track {
    position: relative;
    width: 52px;
    height: 28px;
    background-color: #ccc;
    border-radius: 14px;
    transition: background-color 0.2s ease;
  }
  
  .toggle-thumb {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 24px;
    height: 24px;
    background-color: white;
    border-radius: 50%;
    transition: transform 0.2s ease;
  }
  
  label[role=&quot;switch&quot;][aria-checked=&quot;true&quot;] .toggle-track {
    background-color: #007bff;
  }
  
  label[role=&quot;switch&quot;][aria-checked=&quot;true&quot;] .toggle-thumb {
    transform: translateX(24px);
  }
  
  label[role=&quot;switch&quot;]:focus .toggle-track {
    outline: 2px solid #007bff;
    outline-offset: 2px;
  }
&lt;/style&gt;

&lt;script&gt;
  document.querySelector(&#x27;label[role=&quot;switch&quot;]&#x27;).addEventListener(&#x27;click&#x27;, function() {
    const isChecked = this.getAttribute(&#x27;aria-checked&#x27;) === &#x27;true&#x27;;
    this.setAttribute(&#x27;aria-checked&#x27;, !isChecked);
  });
  
  document.querySelector(&#x27;label[role=&quot;switch&quot;]&#x27;).addEventListener(&#x27;keydown&#x27;, function(e) {
    if (e.key === &#x27; &#x27; || e.key === &#x27;Enter&#x27;) {
      e.preventDefault();
      const isChecked = this.getAttribute(&#x27;aria-checked&#x27;) === &#x27;true&#x27;;
      this.setAttribute(&#x27;aria-checked&#x27;, !isChecked);
    }
  });
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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

    &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  Notifications
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;title&gt;Toggle Switch&lt;/title&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
  &lt;title&gt;Accessible Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications&quot; style=&quot;display:flex;align-items:center;gap:.5rem;cursor:pointer;user-select:none;&quot;&gt;
  &lt;input id=&quot;notifications&quot; type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; style=&quot;position:absolute;opacity:0;width:1px;height:1px;overflow:hidden;&quot;&gt;
  &lt;span style=&quot;position:relative;display:inline-block;width:44px;height:24px;background:#ccc;border-radius:9999px;transition:background .2s;&quot;&gt;
    &lt;span style=&quot;content:&#x27;&#x27;;position:absolute;top:2px;left:2px;width:20px;height:20px;background:#fff;border-radius:50%;transition:transform .2s;box-shadow:0 1px 2px rgba(0,0,0,.2);&quot;&gt;&lt;/span&gt;
  &lt;/span&gt;
  &lt;span style=&quot;font:14px/1.2 system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#222;&quot;&gt;Notifications&lt;/span&gt;
&lt;/label&gt;
&lt;script&gt;
  (function(){
    var input=document.getElementById(&#x27;notifications&#x27;);
    var track=input.nextElementSibling;
    var thumb=track&amp;&amp;track.firstElementChild;
    function apply(){
      var on=input.checked;
      track.style.background=on?&#x27;#16a34a&#x27;:&#x27;#ccc&#x27;;
      thumb.style.transform=on?&#x27;translateX(20px)&#x27;:&#x27;translateX(0)&#x27;;
      input.setAttribute(&#x27;aria-check</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;style&gt;
    :root {
      --switch-width: 48px;
      --switch-height: 28px;
      --knob-size: 22px;
      --knob-gap: 3px;
      --on-color: #2563eb; /* blue-600 */
      --off-color: #cbd5e1; /* slate-300 */
      --knob-color: #ffffff;
      --focus-ring: 2px solid #93c5fd; /* blue-300 */
      --text-color: #0f172a; /* slate-900 */
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      margin: 0;
      padding: 24px;
      color: var(--text-color);
      background: #f8fafc; /* slate-50 */
    }

    .field {
      display: grid;
      grid-template-columns: auto 1fr;
      align-items: center;
      gap: 12px 16px;
      max-width: 420px;
      background: #ffffff;
      border: 1px solid #e2e8f0; /* slate-200 */
      border-radius: 12px;
      padding: 16px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
      --switch-padding: 3px;
      --switch-on: #2563eb;
      --switch-off: #d1d5db;
      --knob: #ffffff;
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.4;
      padding: 2rem;
    }

    .switch {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
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
    }

    .slider {
      position: relative;
      display: inline-block;
      width: var(--switch-width);
      height: var(--switch-height);
      background: var(--switch-off);
      border-radius: 9999px;
      transition: background-color 150ms ease;
      box-shadow: inset 0 0 0 1px rgba(0,0,0,0.06);
    }

    .slider::after {
      content: &quot;&quot;;
      position: absolute;
      top: var(--switch-padding);
      left: var(--switch-padding);
      width: calc(var(--switch-height) - var(--switch-padding) * 2);
      height: calc(var(--switch-height) - var(--switch-padding) * 2);
      background: var(--knob);
      border-radius: 50%;
      transition: transform 150ms ease;
      box-shadow: 0 1px 2px rgba(0,0,0,0.15);
    }

    .switch input[type=&quot;checkbox&quot;]:checked + .slider {
      background: var(--switch-on);
    }

    .switch input[type=&quot;checkbox</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/minimax-minimax-m2/g5.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; /&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  &lt;input type=&quot;checkbox&quot; name=&quot;notifications&quot;&gt;
  Notifications
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
  &lt;span&gt;Notifications&lt;/span&gt;
  &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; /&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input id=&quot;notifications-toggle&quot; type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
    &lt;legend&gt;Notification Settings&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;notifications&quot; name=&quot;notifications&quot; aria-describedby=&quot;notifications-desc&quot;&gt;
      &lt;label for=&quot;notifications&quot;&gt;Notifications&lt;/label&gt;
    &lt;/div&gt;
    &lt;p id=&quot;notifications-desc&quot;&gt;Enable this option to receive alerts about account activity.&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
        Notifications
    &lt;/label&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
        Notifications
    &lt;/label&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-container&quot;&gt;
  &lt;label for=&quot;notification-toggle&quot; class=&quot;toggle-label&quot;&gt;
    Notifications
  &lt;/label&gt;
  &lt;button
    type=&quot;button&quot;
    id=&quot;notification-toggle&quot;
    role=&quot;switch&quot;
    aria-checked=&quot;false&quot;
    class=&quot;toggle-switch&quot;
  &gt;
    &lt;span class=&quot;toggle-track&quot;&gt;
      &lt;span class=&quot;toggle-thumb&quot;&gt;&lt;/span&gt;
    &lt;/span&gt;
  &lt;/button&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;
&lt;input type=&quot;checkbox&quot;&gt;
Notifications
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-label=&quot;Toggle notifications on or off&quot;&gt;
  Notifications
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
