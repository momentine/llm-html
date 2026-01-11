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
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;email-toggle&quot; checked&gt;
      &lt;span&gt;Email&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;sms-toggle&quot;&gt;
      &lt;span&gt;SMS&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;push-toggle&quot; checked&gt;
      &lt;span&gt;Push&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;div style=&quot;margin-bottom: 16px; font-weight: 600; font-size: 14px; color: #333;&quot;&gt;Notification Types&lt;/div&gt;
  
  &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #e5e5e5;&quot;&gt;
    &lt;label for=&quot;toggle-email&quot; style=&quot;font-size: 14px; color: #555; cursor: pointer;&quot;&gt;Email&lt;/label&gt;
    &lt;label style=&quot;position: relative; display: inline-block; width: 44px; height: 24px; cursor: pointer;&quot;&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-email&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
      &lt;span style=&quot;position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 24px; transition: 0.3s;&quot;&gt;&lt;/span&gt;
      &lt;span style=&quot;position: absolute; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;

  &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 12px 0; border-bottom: 1px solid #e5e5e5;&quot;&gt;
    &lt;label for=&quot;toggle-sms&quot; style=&quot;font-size: 14px; color: #555; cursor: pointer;&quot;&gt;SMS&lt;/label&gt;
    &lt;label style=&quot;position: relative; display: inline-block; width: 44px; height: 24px; cursor: pointer;&quot;&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-sms&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
      &lt;span style=&quot;position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 24px; transition: 0.3s;&quot;&gt;&lt;/span&gt;
      &lt;span style=&quot;position: absolute; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;

  &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 12px 0;&quot;&gt;
    &lt;label for=&quot;toggle-push&quot; style=&quot;font-size: 14px; color: #555; cursor: pointer;&quot;&gt;Push&lt;/label&gt;
    &lt;label style=&quot;position: relative; display: inline-block; width: 44px; height: 24px; cursor: pointer;&quot;&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-push&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
      &lt;span style=&quot;position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 24px; transition: 0.3s;&quot;&gt;&lt;/span&gt;
      &lt;span style=&quot;position: absolute; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; border-radius: 50%; transition: 0.3s;&quot;&gt;&lt;/span&gt;
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;

&lt;style&gt;
  input[type=&quot;checkbox&quot;]:checked + span {
    background-color: #4CAF50;
  }
  input[type=&quot;checkbox&quot;]:checked + span + span {
    transform: translateX(20px);
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A group of toggle switches labeled “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset style=&quot;border: 1px solid #ddd; border-radius: 8px; padding: 20px; max-width: 400px; font-family: Arial, sans-serif;&quot;&gt;
  &lt;legend style=&quot;font-size: 18px; font-weight: bold; padding: 0 10px;&quot;&gt;Notification Types&lt;/legend&gt;
  
  &lt;div style=&quot;display: flex; flex-direction: column; gap: 16px;&quot;&gt;
    &lt;div style=&quot;display: flex; justify-content: space-between; align-items: center;&quot;&gt;
      &lt;label for=&quot;email-toggle&quot; style=&quot;font-size: 16px; cursor: pointer;&quot;&gt;Email&lt;/label&gt;
      &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
        &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;
          &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
        &lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;

    &lt;div style=&quot;display: flex; justify-content: space-between; align-items: center;&quot;&gt;
      &lt;label for=&quot;sms-toggle&quot; style=&quot;font-size: 16px; cursor: pointer;&quot;&gt;SMS&lt;/label&gt;
      &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
        &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;
          &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
        &lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;

    &lt;div style=&quot;display: flex; justify-content: space-between; align-items: center;&quot;&gt;
      &lt;label for=&quot;push-toggle&quot; style=&quot;font-size: 16px; cursor: pointer;&quot;&gt;Push&lt;/label&gt;
      &lt;label style=&quot;position: relative; display: inline-block; width: 50px; height: 24px;&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; style=&quot;opacity: 0; width: 0; height: 0;&quot;&gt;
        &lt;span style=&quot;position: absolute; cursor: pointer; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; transition: 0.4s; border-radius: 24px;&quot;&gt;
          &lt;span style=&quot;position: absolute; content: &#x27;&#x27;; height: 18px; width: 18px; left: 3px; bottom: 3px; background-color: white; transition: 0.4s; border-radius: 50%;&quot;&gt;&lt;/span&gt;
        &lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;

&lt;style&gt;
  input[type=&quot;checkbox&quot;]:checked + span {
    background-color: #2196F3;
  }
  input[type=&quot;checkbox&quot;]:checked + span span {
    transform: translateX(26px);
  }
  input[type=&quot;checkbox&quot;]:focus + span {
    box-shadow: 0 0 1px #2196F3;
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;notification-email&quot; id=&quot;notification-email&quot;&gt;
      Email
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;notification-sms&quot; id=&quot;notification-sms&quot;&gt;
      SMS
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; name=&quot;notification-push&quot; id=&quot;notification-push&quot;&gt;
      Push
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
        
        &lt;div role=&quot;group&quot; aria-labelledby=&quot;notification-types-heading&quot;&gt;
            &lt;h2 id=&quot;notification-types-heading&quot; style=&quot;font-size: 1.25rem; margin: 0 0 1rem 0;&quot;&gt;Choose your notification preferences&lt;/h2&gt;
            
            &lt;div style=&quot;display: flex; flex-direction: column; gap: 1rem;&quot;&gt;
                &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 0.75rem; border: 1px solid #ccc; border-radius: 4px;&quot;&gt;
                    &lt;label for=&quot;email-toggle&quot; style=&quot;font-weight: 500; cursor: pointer;&quot;&gt;Email Notifications&lt;/label&gt;
                    &lt;button id=&quot;email-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; style=&quot;width: 50px; height: 26px; border-radius: 13px; border: 2px solid #ccc; background-color: #ccc; position: relative; cursor: pointer; transition: background-color 0.3s;&quot;&gt;
                        &lt;span style=&quot;position: absolute; top: 2px; left: 2px; width: 18px; height: 18px; border-radius: 50%; background-color: white; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
                        &lt;span class=&quot;sr-only&quot;&gt;Toggle email notifications&lt;/span&gt;
                    &lt;/button&gt;
                &lt;/div&gt;

                &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 0.75rem; border: 1px solid #ccc; border-radius: 4px;&quot;&gt;
                    &lt;label for=&quot;sms-toggle&quot; style=&quot;font-weight: 500; cursor: pointer;&quot;&gt;SMS Notifications&lt;/label&gt;
                    &lt;button id=&quot;sms-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; style=&quot;width: 50px; height: 26px; border-radius: 13px; border: 2px solid #ccc; background-color: #ccc; position: relative; cursor: pointer; transition: background-color 0.3s;&quot;&gt;
                        &lt;span style=&quot;position: absolute; top: 2px; left: 2px; width: 18px; height: 18px; border-radius: 50%; background-color: white; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
                        &lt;span class=&quot;sr-only&quot;&gt;Toggle SMS notifications&lt;/span&gt;
                    &lt;/button&gt;
                &lt;/div&gt;

                &lt;div style=&quot;display: flex; align-items: center; justify-content: space-between; padding: 0.75rem; border: 1px solid #ccc; border-radius: 4px;&quot;&gt;
                    &lt;label for=&quot;push-toggle&quot; style=&quot;font-weight: 500; cursor: pointer;&quot;&gt;Push Notifications&lt;/label&gt;
                    &lt;button id=&quot;push-toggle&quot; role=&quot;switch&quot; aria-checked=&quot;false&quot; style=&quot;width: 50px; height: 26px; border-radius: 13px; border: 2px solid #ccc; background-color: #ccc; position: relative; cursor: pointer; transition: background-color 0.3s;&quot;&gt;
                        &lt;span style=&quot;position: absolute; top: 2px; left: 2px; width: 18px; height: 18px; border-radius: 50%; background-color: white; transition: transform 0.3s;&quot;&gt;&lt;/span&gt;
                        &lt;span class=&quot;sr-only&quot;&gt;Toggle push notifications&lt;/span&gt;
                    &lt;/button&gt;
                &lt;/div&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;

    &lt;style&gt;
        .sr-only {
            position: absolute;
            width: 1px;
            height: 1px;
            padding: 0;
            margin: -1px;
            overflow: hidden;
            clip</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;notification-types&quot;&gt;
    &lt;label class=&quot;toggle-switch&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;email-notifications&quot; name=&quot;notification-types&quot; value=&quot;email&quot;&gt;
        &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
        Email
    &lt;/label&gt;
    &lt;label class=&quot;toggle-switch&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;sms-notifications&quot; name=&quot;notification-types&quot; value=&quot;sms&quot;&gt;
        &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
        SMS
    &lt;/label&gt;
    &lt;label class=&quot;toggle-switch&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;push-notifications&quot; name=&quot;notification-types&quot; value=&quot;push&quot;&gt;
        &lt;span class=&quot;slider&quot;&gt;&lt;/span&gt;
        Push
    &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div class=&quot;toggle-group&quot;&gt;
    &lt;button class=&quot;toggle-btn active&quot; data-type=&quot;email&quot;&gt;Email&lt;/button&gt;
    &lt;button class=&quot;toggle-btn&quot; data-type=&quot;sms&quot;&gt;SMS&lt;/button&gt;
    &lt;button class=&quot;toggle-btn&quot; data-type=&quot;push&quot;&gt;Push&lt;/button&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
        &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; class=&quot;toggle-switch&quot;&gt;
    &lt;/div&gt;
    &lt;div class=&quot;toggle-item&quot;&gt;
        &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; class=&quot;toggle-switch&quot;&gt;
    &lt;/div&gt;
    &lt;div class=&quot;toggle-item&quot;&gt;
        &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; class=&quot;toggle-switch&quot;&gt;
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email&quot; name=&quot;notifications&quot; aria-describedby=&quot;email-desc&quot;&gt;
    &lt;label for=&quot;email&quot;&gt;Email&lt;/label&gt;
    &lt;span id=&quot;email-desc&quot; class=&quot;sr-only&quot;&gt;Toggle email notifications&lt;/span&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms&quot; name=&quot;notifications&quot; aria-describedby=&quot;sms-desc&quot;&gt;
    &lt;label for=&quot;sms&quot;&gt;SMS&lt;/label&gt;
    &lt;span id=&quot;sms-desc&quot; class=&quot;sr-only&quot;&gt;Toggle SMS notifications&lt;/span&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push&quot; name=&quot;notifications&quot; aria-describedby=&quot;push-desc&quot;&gt;
    &lt;label for=&quot;push&quot;&gt;Push&lt;/label&gt;
    &lt;span id=&quot;push-desc&quot; class=&quot;sr-only&quot;&gt;Toggle push notifications&lt;/span&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;

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
&lt;/style&gt;

&lt;script&gt;
document.querySelectorAll(&#x27;input[type=&quot;checkbox&quot;]&#x27;).forEach(checkbox =&gt; {
  checkbox.addEventListener(&#x27;change&#x27;, function() {
    const label = this.nextElementSibling;
    if (this.checked) {
      label.setAttribute(&#x27;aria-pressed&#x27;, &#x27;true&#x27;);
    } else {
      label.setAttribute(&#x27;aria-pressed&#x27;, &#x27;false&#x27;);
    }
  });
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-notification&quot; name=&quot;email-notification&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Notification Types&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;toggle-email&quot; name=&quot;notification&quot; value=&quot;email&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email&quot; name=&quot;email&quot; role=&quot;switch&quot;&gt;
    &lt;label for=&quot;email&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; role=&quot;switch&quot;&gt;
    &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; role=&quot;switch&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; role=&quot;switch&quot;&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;notifications&quot; value=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;notification-settings&quot; aria-labelledby=&quot;notification-types-legend&quot;&gt;
  &lt;fieldset&gt;
    &lt;legend id=&quot;notification-types-legend&quot;&gt;Notification Types&lt;/legend&gt;

    &lt;div class=&quot;switch-group&quot;&gt;
      &lt;input class=&quot;visually-hidden&quot; type=&quot;checkbox&quot; id=&quot;notify-email&quot; name=&quot;notifications&quot; value=&quot;email&quot; checked aria-labelledby=&quot;notify-email-label&quot;&gt;
      &lt;label class=&quot;switch&quot; for=&quot;notify-email&quot; id=&quot;notify-email-label&quot;&gt;
        &lt;span class=&quot;switch__text&quot;&gt;Email&lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;

    &lt;div class=&quot;switch-group&quot;&gt;
      &lt;input class=&quot;visually-hidden&quot; type=&quot;checkbox&quot; id=&quot;notify-sms&quot; name=&quot;notifications&quot; value=&quot;sms&quot; aria-labelledby=&quot;notify-sms-label&quot;&gt;
      &lt;label class=&quot;switch&quot; for=&quot;notify-sms&quot; id=&quot;notify-sms-label&quot;&gt;
        &lt;span class=&quot;switch__text&quot;&gt;SMS&lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;

    &lt;div class=&quot;switch-group&quot;&gt;
      &lt;input class=&quot;visually-hidden&quot; type=&quot;checkbox&quot; id=&quot;notify-push&quot; name=&quot;notifications&quot; value=&quot;push&quot; checked aria-labelledby=&quot;notify-push-label&quot;&gt;
      &lt;label class=&quot;switch&quot; for=&quot;notify-push&quot; id=&quot;notify-push-label&quot;&gt;
        &lt;span class=&quot;switch__text&quot;&gt;Push&lt;/span&gt;
      &lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;

&lt;style&gt;
  :root {
    --bg: #ffffff;
    --fg: #111827;
    --muted: #6b7280;
    --border: #e5e7eb;
    --track-off: #d1d5db;
    --track</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset role=&quot;group&quot; aria-label=&quot;Notification Types&quot;&gt;
  &lt;legend class=&quot;sr-only&quot;&gt;Notification Types&lt;/legend&gt;
  &lt;div class=&quot;toggle-group&quot; data-toggle-group&gt;
    &lt;button type=&quot;button&quot;
            class=&quot;toggle&quot;
            role=&quot;switch&quot;
            aria-checked=&quot;true&quot;
            data-value=&quot;email&quot;
            aria-label=&quot;Email notifications&quot;&gt;Email&lt;/button&gt;

    &lt;button type=&quot;button&quot;
            class=&quot;toggle&quot;
            role=&quot;switch&quot;
            aria-checked=&quot;false&quot;
            data-value=&quot;sms&quot;
            aria-label=&quot;SMS notifications&quot;&gt;SMS&lt;/button&gt;

    &lt;button type=&quot;button&quot;
            class=&quot;toggle&quot;
            role=&quot;switch&quot;
            aria-checked=&quot;false&quot;
            data-value=&quot;push&quot;
            aria-label=&quot;Push notifications&quot;&gt;Push&lt;/button&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;

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

  .toggle-group {
    display: flex;
    gap: 12px;
    align-items: center;
  }

  .toggle {
    --w: 46px;
    --h: 26px;
    --p: 3px;
    position: relative;
    width: var(--w);
    height: var(--h);
    border-radius: var(--h);
    border: 1px solid #c8cdd3;
    background: #e6e9ed;
    color: #111827;
    font: 600 13px/1 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, &quot;Helvetica Neue&quot;, Arial, &quot;Not</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Notification Types Toggle Switches&lt;/title&gt;
  &lt;style&gt;
    :root {
      --accent: #2563eb;
      --accent-pressed: #1d4ed8;
      --track-off: #d1d5db;
      --track-on: #93c5fd;
      --thumb: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --bg: #ffffff;
      --border: #e5e7eb;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      color: var(--text);
      background: var(--bg);
      padding: 24px;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;title&gt;Notification Types Toggle Switches&lt;/title&gt;
  &lt;style&gt;
    :root {
      --bg: #ffffff;
      --text: #111827;
      --muted: #6b7280;
      --border: #d1d5db;
      --track-off: #e5e7eb;
      --track-on: #10b981;
      --knob: #ffffff;
      --focus: #3b82f6;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      padding: 2rem;
      background: var(--bg);
      color: var(--text);
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
    }
    fieldset {
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1rem 1.25rem 1.25rem;
      max-width: 420px;
    }
    legend {
      font-weight: 600;
      padding: 0 .25rem;
    }
    .hint {
      color: var(--muted);
      font-size: .9rem;
      margin: .25rem 0 1rem;
    }
    .switch {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: .75rem;
      padding: .5rem 0;
    }
    .switch .label-text {
      flex: 1;
      font-weight: 500;
    }</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;title&gt;Notification Types - Toggle Switch Group&lt;/title&gt;
  &lt;style&gt;
    :root {
      --switch-width: 44px;
      --switch-height: 24px;
      --switch-radius: 999px;
      --thumb-size: 18px;
      --accent: #2563eb;          /* blue-600 */
      --accent-contrast: #ffffff;
      --border: #d1d5db;          /* gray-300 */
      --bg: #ffffff;
      --text: #111827;            /* gray-900 */
      --muted: #6b7280;           /* gray-500 */
      --focus: #0ea5e9;           /* sky-500 */
    }

    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, &quot;Helvetica Neue&quot;, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
      color: var(--text);
      background: #f9fafb;
      margin: 0;
      padding: 2rem;
    }

    .container {
      max-width</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;section&gt;
  &lt;h2&gt;Notification Types&lt;/h2&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Select notification preferences&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_email&quot; value=&quot;email&quot;&gt;
      Email
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_sms&quot; value=&quot;sms&quot;&gt;
      SMS
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;notification_push&quot; value=&quot;push&quot;&gt;
      Push
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/section&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Notification Types&lt;/legend&gt;
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
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
&lt;label&gt;
&lt;input type=&quot;checkbox&quot; name=&quot;notification_email&quot;&gt;
Email
&lt;/label&gt;
&lt;label&gt;
&lt;input type=&quot;checkbox&quot; name=&quot;notification_sms&quot;&gt;
SMS
&lt;/label&gt;
&lt;label&gt;
&lt;input type=&quot;checkbox&quot; name=&quot;notification_push&quot;&gt;
Push
&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;notification_email&quot;&gt; Email&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;notification_sms&quot;&gt; SMS&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;notification_push&quot;&gt; Push&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Notification Types&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-email&quot; role=&quot;switch&quot; name=&quot;notification-email&quot; aria-checked=&quot;true&quot; checked&gt;
      &lt;label for=&quot;toggle-email&quot;&gt;Email&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-sms&quot; role=&quot;switch&quot; name=&quot;notification-sms&quot; aria-checked=&quot;false&quot;&gt;
      &lt;label for=&quot;toggle-sms&quot;&gt;SMS&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;toggle-push&quot; role=&quot;switch&quot; name=&quot;notification-push&quot; aria-checked=&quot;false&quot;&gt;
      &lt;label for=&quot;toggle-push&quot;&gt;Push&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;notification-types&quot; value=&quot;email&quot;&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; name=&quot;notification-types&quot; value=&quot;sms&quot;&gt;
  &lt;/div&gt;
  &lt;div class=&quot;toggle-item&quot;&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; name=&quot;notification-types&quot; value=&quot;push&quot;&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
      &lt;input type=&quot;checkbox&quot; name=&quot;email&quot; /&gt;
      Email
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;sms&quot; /&gt;
      SMS
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;push&quot; /&gt;
      Push
    &lt;/label&gt;
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;notifications&quot; value=&quot;email&quot;&gt;
    &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; name=&quot;notifications&quot; value=&quot;sms&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; name=&quot;notifications&quot; value=&quot;push&quot;&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
    &lt;input type=&quot;checkbox&quot; id=&quot;email-toggle&quot; name=&quot;notifications&quot; value=&quot;email&quot;&gt;
    &lt;label for=&quot;email-toggle&quot;&gt;Email&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;sms-toggle&quot; name=&quot;notifications&quot; value=&quot;sms&quot;&gt;
    &lt;label for=&quot;sms-toggle&quot;&gt;SMS&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;push-toggle&quot; name=&quot;notifications&quot; value=&quot;push&quot;&gt;
    &lt;label for=&quot;push-toggle&quot;&gt;Push&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a group of toggle switches for “Notification Types” with toggles for Email, SMS, and Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Email&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; SMS&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Push&lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Toggle group: Notification Types with toggles Email, SMS, Push</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;h3&gt;Notification Types&lt;/h3&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;email&quot;&gt; Email
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;sms&quot;&gt; SMS
  &lt;/label&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;push&quot;&gt; Push
  &lt;/label&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Email&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; SMS&lt;/label&gt;
&lt;label&gt;&lt;input type=&quot;checkbox&quot;&gt; Push&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
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
&lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;email&quot; name=&quot;notifications&quot; value=&quot;email&quot;&gt;
&lt;label for=&quot;email&quot;&gt;Email&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;sms&quot; name=&quot;notifications&quot; value=&quot;sms&quot;&gt;
&lt;label for=&quot;sms&quot;&gt;SMS&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; role=&quot;switch&quot; id=&quot;push&quot; name=&quot;notifications&quot; value=&quot;push&quot;&gt;
&lt;label for=&quot;push&quot;&gt;Push&lt;/label&gt;
&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/toggle-switch-group-with-multiple-types/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
