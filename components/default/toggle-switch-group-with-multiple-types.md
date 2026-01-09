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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
      &lt;span&gt;Email&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
      &lt;span&gt;SMS&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
      &lt;span&gt;Push&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Notification Types&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;Notification Types&lt;/legend&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; name=&quot;email&quot; id=&quot;email&quot;&gt;
                Email
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; name=&quot;sms&quot; id=&quot;sms&quot;&gt;
                SMS
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; name=&quot;push&quot; id=&quot;push&quot;&gt;
                Push
            &lt;/label&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; checked&gt;
      &lt;span&gt;Email&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; checked&gt;
      &lt;span&gt;SMS&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; checked&gt;
      &lt;span&gt;Push&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Notification Types&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;Notification Types&lt;/legend&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;email&quot; id=&quot;email&quot;&gt;
                Email
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;sms&quot; id=&quot;sms&quot;&gt;
                SMS
            &lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label&gt;
                &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;push&quot; id=&quot;push&quot;&gt;
                Push
            &lt;/label&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Notification Types&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;Notification Types&lt;/legend&gt;
        
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;email-toggle&quot; name=&quot;email&quot; aria-checked=&quot;false&quot;&gt;
            &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
        &lt;/div&gt;
        
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;sms-toggle&quot; name=&quot;sms&quot; aria-checked=&quot;false&quot;&gt;
            &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
        &lt;/div&gt;
        
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;push-toggle&quot; name=&quot;push&quot; aria-checked=&quot;false&quot;&gt;
            &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-group&quot;&gt;
  &lt;label class=&quot;toggle-label&quot;&gt;
    &lt;input type=&quot;checkbox&quot; class=&quot;toggle-input&quot; checked&gt;
    &lt;span class=&quot;toggle-slider&quot;&gt;&lt;/span&gt;
    Email
  &lt;/label&gt;
  &lt;label class=&quot;toggle-label&quot;&gt;
    &lt;input type=&quot;checkbox&quot; class=&quot;toggle-input&quot; checked&gt;
    &lt;span class=&quot;toggle-slider&quot;&gt;&lt;/span&gt;
    SMS
  &lt;/label&gt;
  &lt;label class=&quot;toggle-label&quot;&gt;
    &lt;input type=&quot;checkbox&quot; class=&quot;toggle-input&quot; checked&gt;
    &lt;span class=&quot;toggle-slider&quot;&gt;&lt;/span&gt;
    Push
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-group&quot;&gt;
  &lt;label class=&quot;toggle-item&quot;&gt;
    &lt;input type=&quot;checkbox&quot; checked&gt;
    &lt;span class=&quot;toggle-label&quot;&gt;Email&lt;/span&gt;
  &lt;/label&gt;
  &lt;label class=&quot;toggle-item&quot;&gt;
    &lt;input type=&quot;checkbox&quot; checked&gt;
    &lt;span class=&quot;toggle-label&quot;&gt;SMS&lt;/span&gt;
  &lt;/label&gt;
  &lt;label class=&quot;toggle-item&quot;&gt;
    &lt;input type=&quot;checkbox&quot; checked&gt;
    &lt;span class=&quot;toggle-label&quot;&gt;Push&lt;/span&gt;
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-group&quot;&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;span&gt;Email&lt;/span&gt;
    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot;&gt;
      &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;span&gt;SMS&lt;/span&gt;
    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot;&gt;
      &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;span&gt;Push&lt;/span&gt;
    &lt;label class=&quot;switch&quot;&gt;
      &lt;input type=&quot;checkbox&quot;&gt;
      &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    Email
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    SMS
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot;&gt;
    Push
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div role=&quot;group&quot; aria-labelledby=&quot;notification-types-label&quot;&gt;
  &lt;h3 id=&quot;notification-types-label&quot;&gt;Notification Types&lt;/h3&gt;
  &lt;ul&gt;
    &lt;li&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;email&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
      &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
    &lt;/li&gt;
    &lt;li&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; name=&quot;sms&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
      &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
    &lt;/li&gt;
    &lt;li&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; name=&quot;push&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
      &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
    &lt;/li&gt;
  &lt;/ul&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;email_notification&quot; role=&quot;switch&quot;&gt;
      Email
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
    &lt;title&gt;Toggle Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Toggle Switches&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;notification-type&quot; value=&quot;email&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Notification Settings&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;Notification Types&lt;/legend&gt;
        &lt;div&gt;
            &lt;label for=&quot;email-switch&quot;&gt;Email&lt;/label&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;email-switch&quot; role=&quot;switch&quot; checked&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label for=&quot;sms-switch&quot;&gt;SMS&lt;/label&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;sms-switch&quot; role=&quot;switch&quot;&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;label for=&quot;push-switch&quot;&gt;Push&lt;/label&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;push-switch&quot; role=&quot;switch&quot; checked&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types Toggles&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.4; padding: 24px; }
    fieldset { border: 1px solid #d0d7de; border-radius: 10px; padding: 16px 16px 12px; max-width: 420px; }
    legend { font-weight: 600; padding: 0 6px; }

    .toggles { list-style: none; margin: 8px 0 0; padding: 0; display: grid; gap: 12px; }

    /* Visually hidden but accessible checkbox */
    .toggle-input {
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

    /* Switch */
    .switch {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      user-select: none;
    }
    .slider {
      position: relative;
      width: 44px;
      height: 24px;
      background: #c7cdd4;
      border-radius: 999px;
      transition: background-color .2s ease;
      box-shadow: inset 0 0 0 1px rgba(0,0,0,.06);
    }
    .slider::before {
      content: &quot;&quot;;
      position: absolute;
      top: 2px;
      left: 2px;
      width: 20px;
      height: 20px;
      background: #fff;
      border-radius: 50%;
      transition: transform .2s ease;
      box-shadow: 0 1px 2px rgba(0,0,0,.2);
    }

    /* Checked state */
    .toggle-input:checked +</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types Toggle Group&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #1f2937;
      --muted: #6b7280;
      --track: #e5e7eb;
      --track-hover: #d1d5db;
      --thumb: #ffffff;
      --on: #2563eb;
      --on-hover: #1d4ed8;
      --focus: #93c5fd;
      --border: #e5e7eb;
      --shadow: 0 1px 2px rgba(0,0,0,0.06);
      --radius: 12px;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      color: var(--text);
      background: var(--bg);
      line-height: 1.5;
    }
    .container {
      max-width: 560px;
      margin: 48px auto;
      padding: 0 16px;
    }
    h1 {
      font-size: 1.25rem;
      margin: 0 0 16px;
    }
    .card {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      box-shadow: var(--shadow);
      background: #fff;
    }
    fieldset {
      border: 0;
      margin: 0;
      padding: 0;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Notification Types Toggle Group&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --fg: #1f2937;
      --muted: #6b7280;
      --border: #e5e7eb;
      --track-off: #d1d5db;
      --track-on: #10b981;
      --thumb: #ffffff;
      --focus: #2563eb;
    }
    @media (prefers-color-scheme: dark) {
      :root {
        --bg: #0b0f14;
        --fg: #e5e7eb;
        --muted: #9ca3af;
        --border: #1f2937;
        --track-off: #374151;
        --track-on: #059669;
        --thumb: #f9fafb;
        --focus: #60a5fa;
      }
    }

    html, body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--fg);
      font: 16px/1.5 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, &quot;Helvetica Neue&quot;, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
    }

    .container {
      max-width: 520px;
      margin: 48px auto;
      padding: 24px;
      border: 1px solid var(--border);
      border-radius: 12px;
      background: var(--bg);
    }

    h1 {
      font-size: 1.25rem;
      margin: 0 0 16px;
    }

    fieldset {</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;title&gt;Notification Types Toggle Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;Notification Types&lt;/legend&gt;

      &lt;label for=&quot;notify-email&quot;&gt;
        &lt;input id=&quot;notify-email&quot; name=&quot;notification_types&quot; type=&quot;checkbox&quot; value=&quot;email&quot; /&gt;
        Email
      &lt;/label&gt;

      &lt;label for=&quot;notify-sms&quot;&gt;
        &lt;input id=&quot;notify-sms&quot; name=&quot;notification_types&quot; type=&quot;checkbox&quot; value=&quot;sms&quot; /&gt;
        SMS
      &lt;/label&gt;

      &lt;label for=&quot;notify-push&quot;&gt;
        &lt;input id=&quot;notify-push&quot; name=&quot;notification_types&quot; type=&quot;checkbox&quot; value=&quot;push&quot; /&gt;
        Push
      &lt;/label&gt;
    &lt;/fieldset&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Notification Type Toggles&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #1f2937;
      --muted: #6b7280;
      --border: #d1d5db;
      --focus: #2563eb;
      --track-off: #e5e7eb;
      --track-on: #10b981;
      --thumb: #ffffff;
      --shadow: rgba(0, 0, 0, 0.18);
      --radius: 9999px;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
      color: var(--text);
      background: var(--bg);
      padding: 2rem;
    }

    fieldset {
      border: 1px solid var(--border);
      border-radius: 0.5rem;
      padding: 1rem 1.25rem;
      max-width: 28rem;
    }

    legend {
      font-weight: 600;
      padding: 0 0.25rem;
    }

    .help {
      color: var(--muted);
      font-size: 0.9375rem;
      margin: 0.25rem 0 0.75rem;
    }

    .switch {
      display: flex;
      align-items: center;
      gap: 0.75rem;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Notification Types&lt;/legend&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notif-email&quot; name=&quot;notification-types&quot; value=&quot;email&quot;&gt;
&lt;label for=&quot;notif-email&quot;&gt;Email&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notif-sms&quot; name=&quot;notification-types&quot; value=&quot;sms&quot;&gt;
&lt;label for=&quot;notif-sms&quot;&gt;SMS&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notif-push&quot; name=&quot;notification-types&quot; value=&quot;push&quot;&gt;
&lt;label for=&quot;notif-push&quot;&gt;Push&lt;/label&gt;
&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;section&gt;
  &lt;h2&gt;Notification Types&lt;/h2&gt;
  &lt;div role=&quot;group&quot; aria-label=&quot;Notification Types&quot;&gt;
    &lt;label&gt;
      &lt;span&gt;Email&lt;/span&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification-email&quot;&gt;
    &lt;/label&gt;
    &lt;label&gt;
      &lt;span&gt;SMS&lt;/span&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification-sms&quot;&gt;
    &lt;/label&gt;
    &lt;label&gt;
      &lt;span&gt;Push&lt;/span&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification-push&quot;&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/section&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;span&gt;Notification Types&lt;/span&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;notification-email&quot;&gt;
    Email
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;notification-sms&quot;&gt;
    SMS
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;notification-push&quot;&gt;
    Push
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Notification Types&lt;/legend&gt;
&lt;label&gt;Email &lt;input type=&quot;checkbox&quot; /&gt;&lt;/label&gt;
&lt;label&gt;SMS &lt;input type=&quot;checkbox&quot; /&gt;&lt;/label&gt;
&lt;label&gt;Push &lt;input type=&quot;checkbox&quot; /&gt;&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Notification Types&lt;/legend&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notify-email&quot; role=&quot;switch&quot; aria-checked=&quot;true&quot; checked&gt;
&lt;label for=&quot;notify-email&quot;&gt;Email&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notify-sms&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot;&gt;
&lt;label for=&quot;notify-sms&quot;&gt;SMS&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;notify-push&quot; role=&quot;switch&quot; aria-checked=&quot;true&quot; checked&gt;
&lt;label for=&quot;notify-push&quot;&gt;Push&lt;/label&gt;
&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; /&gt;
      Email
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; /&gt;
      SMS
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; /&gt;
      Push
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-group&quot;&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;email-toggle&quot;&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; name=&quot;sms-toggle&quot;&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; name=&quot;push-toggle&quot;&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot;&gt;
      Email
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot;&gt;
      SMS
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot;&gt;
      Push
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
    &lt;label for=&quot;email&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms&quot; name=&quot;sms&quot;&gt;
    &lt;label for=&quot;sms&quot;&gt;SMS&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push&quot; name=&quot;push&quot;&gt;
    &lt;label for=&quot;push&quot;&gt;Push&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; checked&gt;
    &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; checked&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Notification Types&lt;/legend&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;email&quot;&gt; Email&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;sms&quot;&gt; SMS&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;push&quot;&gt; Push&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;Notification Types&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;email&quot;&gt; Email&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;sms&quot;&gt; SMS&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;push&quot;&gt; Push&lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Notification Types&lt;/legend&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Email&lt;/label&gt;&lt;br&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; SMS&lt;/label&gt;&lt;br&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Push&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a group and legend of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Email&lt;/label&gt;&lt;br&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; SMS&lt;/label&gt;&lt;br&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Push&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; aria-describedby=&quot;email-desc&quot;&gt;
    Email
  &lt;/label&gt;
  &lt;span id=&quot;email-desc&quot;&gt;Receive notifications via email&lt;/span&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; aria-describedby=&quot;sms-desc&quot;&gt;
    SMS
  &lt;/label&gt;
  &lt;span id=&quot;sms-desc&quot;&gt;Receive notifications via SMS&lt;/span&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; aria-describedby=&quot;push-desc&quot;&gt;
    Push
  &lt;/label&gt;
  &lt;span id=&quot;push-desc&quot;&gt;Receive push notifications&lt;/span&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
