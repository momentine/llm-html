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
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label&gt;
            &lt;span&gt;Notifications&lt;/span&gt;
            &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
        &lt;/label&gt;
        &lt;small&gt;Turn alerts on or off.&lt;/small&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
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
    &lt;div&gt;
        &lt;label&gt;
            &lt;span&gt;Notifications&lt;/span&gt;
            &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
        &lt;/label&gt;
        &lt;small&gt;Turn alerts on or off.&lt;/small&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    &lt;span&gt;Notifications&lt;/span&gt;
  &lt;/label&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Toggle Switch&lt;/title&gt;
    &lt;style&gt;
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .toggle-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            max-width: 400px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .toggle-wrapper {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .toggle-label {
            flex-grow: 1;
        }
        .toggle-label h3 {
            margin: 0 0 5px 0;
            font-size: 16px;
            color: #333;
        }
        .toggle-label p {
            margin: 0;
            font-size: 14px;
            color: #666;
        }
        .toggle-switch {
            position: relative;
            width: 50px;
            height: 26px;
        }
        .toggle-switch input {
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
            transition: 0.3s;
            border-radius: 26px;
        }
        .slider:before {
            position: absolute;
            content: &quot;&quot;;
            height: 20px;
            width: 20px;
            left: 3px;
            bottom: 3px;
            background-color: white;
            transition: 0.3s;
            border-radius: 50%;
        }
        input:checked + .slider {
            background-color: #2196F3;
        }
        input:checked + .slider:before {
            transform: translateX(24px);
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class=&quot;toggle-container&quot;&gt;
        &lt;div class=&quot;toggle-wrapper&quot;&gt;
            &lt;div class=&quot;toggle-label&quot;&gt;
                &lt;h3&gt;Notifications&lt;/h3&gt;
                &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
            &lt;/div&gt;
            &lt;label class=&quot;toggle-switch&quot;&gt;
                &lt;input type=&quot;checkbox&quot;&gt;
                &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
            &lt;/label&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Notifications Toggle&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div role=&quot;group&quot; aria-labelledby=&quot;toggle-label&quot;&gt;
        &lt;label id=&quot;toggle-label&quot; for=&quot;notifications-toggle&quot;&gt;
            Notifications
        &lt;/label&gt;
        &lt;button
            type=&quot;button&quot;
            role=&quot;switch&quot;
            id=&quot;notifications-toggle&quot;
            aria-checked=&quot;false&quot;
            aria-describedby=&quot;toggle-description&quot;&gt;
            &lt;span aria-hidden=&quot;true&quot;&gt;Off&lt;/span&gt;
        &lt;/button&gt;
        &lt;div id=&quot;toggle-description&quot;&gt;
            Turn alerts on or off.
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
&lt;span&gt;Notifications&lt;/span&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-switch&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot;&gt;
  &lt;p class=&quot;note&quot;&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot;&gt;
  &lt;span class=&quot;slider round&quot;&gt;&lt;/span&gt;
&lt;/label&gt;
&lt;span&gt;Notifications&lt;/span&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;

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
  }
  input:checked + .slider {
    background-color: #2196F3;
  }
  input:checked + .slider:before {
    transform: translateX(26px);
  }
  .slider.round {
    border-radius: 34px;
  }
  .slider.round:before {
    border-radius: 50%;
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div style=&quot;display: flex; align-items: center; gap: 10px; font-family: sans-serif;&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot; style=&quot;font-weight: 500;&quot;&gt;Notifications&lt;/label&gt;
  &lt;div style=&quot;position: relative; display: inline-block; width: 50px; height: 26px;&quot;&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0; position: absolute;&quot;&gt;
    &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: .4s; border-radius: 34px; display: block;&quot;&gt;&lt;/span&gt;
    &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 4px; bottom: 4px; background-color: white; transition: .4s; border-radius: 50%; display: block;&quot;&gt;&lt;/span&gt;
  &lt;/div&gt;
  &lt;span style=&quot;font-size: 0.8rem; color: #666;&quot;&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot; class=&quot;sr-only&quot;&gt;Notifications&lt;/label&gt;
&lt;div class=&quot;toggle-switch&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
  &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
&lt;/div&gt;
&lt;span class=&quot;toggle-note&quot;&gt;Turn alerts on or off.&lt;/span&gt;

&lt;style&gt;
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

  .toggle-switch {
    position: relative;
    display: inline-block;
    width: 60px;
    height: 34px;
  }

  .toggle-switch input {
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

  .toggle-note {
    display: block;
    margin-top: 8px;
    font-size: 14px;
    color: #666;
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
    &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
    &lt;title&gt;Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
&lt;head&gt;
  &lt;title&gt;Accessible Toggle Switch&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;form-field&quot;&gt;
  &lt;div class=&quot;row&quot;&gt;
    &lt;input id=&quot;notifications&quot; type=&quot;checkbox&quot; class=&quot;switch&quot; aria-describedby=&quot;notifications-note&quot;&gt;
    &lt;label for=&quot;notifications&quot; class=&quot;switch-label&quot;&gt;Notifications&lt;/label&gt;
  &lt;/div&gt;
  &lt;div id=&quot;notifications-note&quot; class=&quot;note&quot;&gt;Turn alerts on or off.&lt;/div&gt;
&lt;/div&gt;
&lt;style&gt;
  .form-field { margin: 16px 0; }
  .row { display: flex; align-items: center; gap: 12px; }
  .switch-label { font-weight: 600; }
  .note { font-size: 0.9rem; color: #6b7280; margin-top: 6px; }

  .switch {
    position: relative;
    display: inline-block;
    width: 46px;
    height: 26px;
    appearance: none;
    -webkit-appearance: none;
    background: #d1d5db;
    border-radius: 9999px;
    outline: none;
    cursor: pointer;
    transition: background .2s ease;
  }
  .switch::after {
    content: &quot;&quot;;
    position: absolute;
    top: 3px;
    left: 3px;
    width: 20px;
    height: 20px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 1px 2px rgba(0,0,0,.2);
    transition: transform .2s ease;
  }
  .switch:checked { background: #16a34a; }
  .switch:checked::after { transform: translateX(20px); }
  .switch:focus-visible {
    outline: 2px solid #2563eb;
    outline-offset: 2px;
  }
  .switch:disabled { opacity: .6; cursor: not-allowed; }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notifications&lt;/legend&gt;
  &lt;label for=&quot;toggle-notifications&quot;&gt;
    &lt;input id=&quot;toggle-notifications&quot; type=&quot;checkbox&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; /&gt;
    Turn alerts on or off.
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot; style=&quot;display:inline-flex; align-items:center; gap:.75rem; cursor:pointer;&quot;&gt;
  &lt;input id=&quot;notifications-toggle&quot; type=&quot;checkbox&quot; role=&quot;switch&quot; aria-labelledby=&quot;notifications-label&quot; aria-describedby=&quot;notifications-note&quot; style=&quot;position:absolute; opacity:0; width:1px; height:1px; margin:-1px; padding:0; border:0; clip:rect(0 0 0 0); clip-path:inset(50%); overflow:hidden; white-space:nowrap;&quot;&gt;
  &lt;span id=&quot;notifications-label&quot; style=&quot;font-weight:600;&quot;&gt;Notifications&lt;/span&gt;
  &lt;span id=&quot;notifications-note&quot; style=&quot;color:#6b7280;&quot;&gt;Turn alerts on or off.&lt;/span&gt;
  &lt;span aria-hidden=&quot;true&quot; style=&quot;position:relative; display:inline-block; width:48px; height:28px; background:#d1d5db; border-radius:9999px; transition:background-color .2s ease; box-shadow:inset 0 0 0 1px rgba(0,0,0,.06); margin-left:.25rem;&quot;&gt;
    &lt;span style=&quot;position:absolute; top:3px; left:3px; width:22px; height:22px; background:#ffffff; border-radius:50%; transition:transform .2</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset class=&quot;toggle&quot;&gt;
  &lt;legend&gt;Notifications&lt;/legend&gt;
  &lt;label class=&quot;toggle__label&quot;&gt;
    &lt;input class=&quot;toggle__input sr-only&quot; type=&quot;checkbox&quot; aria-describedby=&quot;notifications-note&quot; /&gt;
    &lt;span class=&quot;toggle__switch&quot; aria-hidden=&quot;true&quot;&gt;&lt;/span&gt;
    &lt;span class=&quot;toggle__text&quot;&gt;Notifications&lt;/span&gt;
  &lt;/label&gt;
  &lt;p id=&quot;notifications-note&quot; class=&quot;toggle__note&quot;&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/fieldset&gt;

&lt;style&gt;
  .toggle {
    margin: 0;
    border: 0;
    padding: 0;
    font: 16px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
    color: #0f172a;
  }

  .toggle legend {
    font-weight: 600;
    margin-bottom: 8px;
  }

  .toggle__label {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    cursor: pointer;
    user-select: none;
  }

  .toggle__input.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
      --switch-track-w: 44px;
      --switch-track-h: 24px;
      --switch-thumb: 20px;
      --accent: #2563eb;
      --accent-pressed: #1d4ed8;
      --track-off: #cbd5e1;
      --track-on: #93c5fd;
      --text: #0f172a;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --accent: #60a5fa;
        --accent-pressed: #3b82f6;
        --track-off: #475569;
        --track-on: #1e40af;
        --text: #e5e7eb;
      }
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      color: var(--text);
      padding: 2rem;
      background: Canvas;
    }

    .switch {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      user-select: none;
    }

    /* Visually hidden but accessible */
    .sr-only {
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

    /* The switch control */
    .switch__control {
      position: relative;
      display: inline-flex;
      align-items: center;
      width: var(--switch-track-w);
      height: var(--switch-track-h);
      border-radius: 9999px;
      background: var(--track-off);
      transition: background-color .2</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;section&gt;
  &lt;label&gt;
    Notifications
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-label=&quot;Notifications toggle&quot;&gt;
  &lt;/label&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/section&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle switch: Notifications with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    Notifications
  &lt;/label&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;section&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; /&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/section&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;
    &lt;span&gt;Notifications&lt;/span&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; aria-label=&quot;Notifications&quot;&gt;
  &lt;/label&gt;
  &lt;p&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
  &lt;p id=&quot;notifications-note&quot;&gt;Turn alerts on or off.&lt;/p&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-describedby=&quot;notifications-note&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; /&gt;
  &lt;span&gt;Turn alerts on or off.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-container&quot;&gt;
  &lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
  &lt;div class=&quot;toggle-switch&quot;&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
    &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
  &lt;/div&gt;
  &lt;p id=&quot;notifications-description&quot;&gt;Turn alerts on or off.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  Notifications
&lt;/label&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
&lt;small&gt;Turn alerts on or off.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A toggle switch labeled “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;Notifications&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
&lt;p&gt;Turn alerts on or off.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a toggle switch and label for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;notifications-toggle&quot;&gt;
  Notifications
  &lt;br&gt;
  &lt;small&gt;Turn alerts on or off.&lt;/small&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible toggle switch for “Notifications” with note “Turn alerts on or off.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;notifications-toggle&quot;&gt;
  &lt;input id=&quot;notifications-toggle&quot; type=&quot;checkbox&quot; aria-describedby=&quot;toggle-note&quot;&gt;
  Notifications
&lt;/label&gt;
&lt;span id=&quot;toggle-note&quot;&gt;Turn alerts on or off.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-with-accessible-description/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
