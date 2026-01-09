<details>
  <summary><strong>Password Field with Validation Error</strong></summary>
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
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;new-password-error&quot;&gt;
  &lt;span id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
        &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot; value=&quot;&quot;&gt;
        &lt;span id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input 
    type=&quot;password&quot; 
    id=&quot;new-password&quot; 
    name=&quot;new-password&quot; 
    aria-invalid=&quot;true&quot; 
    aria-describedby=&quot;password-error&quot;
  &gt;
  &lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;span id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
        &lt;input 
            type=&quot;password&quot; 
            id=&quot;new-password&quot; 
            name=&quot;new-password&quot;
            aria-invalid=&quot;true&quot;
            aria-describedby=&quot;password-error&quot;
        &gt;
        &lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; name=&quot;new_password&quot; placeholder=&quot;New password&quot; required minlength=&quot;8&quot;&gt;
&lt;span style=&quot;color: red; display: block;&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; name=&quot;password&quot; placeholder=&quot;New password&quot; required minlength=&quot;8&quot;&gt;
&lt;div style=&quot;color: red; font-size: 0.875rem;&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;password&quot; name=&quot;password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;span id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;p id=&quot;password-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;New Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
        &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
  &lt;title&gt;Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Accessible Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Password Validation&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;passwordForm&quot; novalidate&gt;
    &lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
    &lt;input
      type=&quot;password&quot;
      id=&quot;newPassword&quot;
      name=&quot;newPassword&quot;
      required
      aria-describedby=&quot;newPasswordError&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;p id=&quot;newPasswordError&quot; hidden&gt;&lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;passwordForm&#x27;);
      const input = document.getElementById(&#x27;newPassword&#x27;);
      const errorEl = document.getElementById(&#x27;newPasswordError&#x27;);
      const MIN_LENGTH = 8;
      const ERROR_MESSAGE = &#x27;Too short. Must be at least 8 characters.&#x27;;

      function validate() {
        const value = input.value;
        const isValid = value.length &gt;= MIN_LENGTH;

        if (!isValid &amp;&amp; value.length &gt; 0) {
          errorEl.textContent = ERROR_MESSAGE;
          errorEl.hidden = false;
          input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
          return false;
        }

        errorEl.hidden = true;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
        return true;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validate()) {
          e.preventDefault();
          input.focus();
        }
      });
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Password Field with Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;passwordForm&quot;&gt;
    &lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
    &lt;input
      type=&quot;password&quot;
      id=&quot;newPassword&quot;
      name=&quot;newPassword&quot;
      required
      aria-describedby=&quot;passwordError&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;div id=&quot;passwordError&quot; role=&quot;alert&quot; style=&quot;color: #b00020; margin-top: 4px; display: none;&quot;&gt;
      Too short. Must be at least 8 characters.
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot; style=&quot;margin-top: 8px;&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;newPassword&#x27;);
      const errorEl = document.getElementById(&#x27;passwordError&#x27;);

      function validate() {
        const value = input.value;
        const isValid = value.length &gt;= 8;
        errorEl.style.display = isValid ? &#x27;none&#x27; : &#x27;block&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, String(!isValid));
        return isValid;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      input.addEventListener(&#x27;blur&#x27;, validate);

      document.getElementById(&#x27;passwordForm&#x27;).addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validate()) {
          e.preventDefault();
          input.focus();
        }
      });
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;New password validation error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input
      id=&quot;new-password&quot;
      name=&quot;new_password&quot;
      type=&quot;password&quot;
      required
      minlength=&quot;8&quot;
      aria-invalid=&quot;true&quot;
      aria-describedby=&quot;password-error&quot;
      placeholder=&quot;Enter new password&quot;
    &gt;
    &lt;p id=&quot;password-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;div&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input
      id=&quot;new-password&quot;
      name=&quot;new-password&quot;
      type=&quot;password&quot;
      inputmode=&quot;text&quot;
      autocomplete=&quot;new-password&quot;
      required
      minlength=&quot;8&quot;
      aria-describedby=&quot;new-password-error&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;

  &lt;button type=&quot;button&quot; id=&quot;toggle-password&quot; aria-controls=&quot;new-password&quot; aria-pressed=&quot;false&quot;&gt;Show password&lt;/button&gt;

  &lt;button type=&quot;submit&quot;&gt;Create password&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;new-password&#x27;);
      const error = document.getElementById(&#x27;new-password-error&#x27;);
      const toggle = document.getElementById(&#x27;toggle-password&#x27;);

      function showError(message) {
        error.textContent = message;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function clearError() {
        error.textContent = &#x27;&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }

      function validate() {
        const value = input.value;
        if (value.length === 0) {
          clearError();
          return true;
        }
        if (value.length &lt; 8) {
          showError(&#x27;Too short. Must be at least 8 characters.&#x27;);
          return false;
        }
        clearError();
        return true;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      input.addEventListener(&#x27;blur&#x27;, validate);

      toggle.addEventListener(&#x27;click&#x27;, () =&gt; {
        const isHidden = input.type === &#x27;password&#x27;;
        input.type = isHidden ? &#x27;text&#x27; : &#x27;password&#x27;;
        toggle.setAttribute(&#x27;aria-pressed&#x27;, String(isHidden));
        toggle.textContent = isHidden ? &#x27;Hide password&#x27; : &#x27;Show password&#x27;;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;new-password&quot; type=&quot;password&quot; aria-describedby=&quot;new-password-error&quot;&gt;
&lt;div id=&quot;new-password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input id=&quot;new-password&quot; name=&quot;new-password&quot; type=&quot;password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;new-password&quot; type=&quot;password&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;div id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
  &lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;new-password-error&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; name=&quot;new_password&quot; required minlength=&quot;8&quot;&gt;
&lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; minlength=&quot;8&quot; required&gt;
&lt;div class=&quot;error-message&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
  &lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
  &lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; minlength=&quot;8&quot; required&gt;
&lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;newpassword&quot;&gt;New password:&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;newpassword&quot; name=&quot;newpassword&quot;&gt;
  &lt;p&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;newPassword&quot; name=&quot;newPassword&quot;&gt;
&lt;p&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newpassword&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;newpassword&quot;&gt;
&lt;p&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot;&gt;
&lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;error-message&quot;&gt;
&lt;div id=&quot;error-message&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
