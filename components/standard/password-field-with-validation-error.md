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
  &lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;new-password-error&quot;&gt;
&lt;span id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
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
    aria-describedby=&quot;new-password-error&quot;
    required
  &gt;
  &lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; name=&quot;new_password&quot; placeholder=&quot;New password&quot; required minlength=&quot;8&quot;&gt;
&lt;div style=&quot;color: red;&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; placeholder=&quot;New password&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;span id=&quot;password-error&quot; style=&quot;color: red;&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
&lt;span id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;new-password-error&quot;&gt;
&lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; /&gt;
&lt;p id=&quot;password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;p id=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; autocomplete=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;passwordForm&quot; novalidate&gt;
  &lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
  &lt;input
    type=&quot;password&quot;
    id=&quot;newPassword&quot;
    name=&quot;newPassword&quot;
    minlength=&quot;8&quot;
    required
    aria-describedby=&quot;passwordError&quot;
    aria-invalid=&quot;false&quot;
  /&gt;
  &lt;p id=&quot;passwordError&quot; role=&quot;alert&quot; style=&quot;color:#b00020; display:none;&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;newPassword&#x27;);
      const error = document.getElementById(&#x27;passwordError&#x27;);

      function updateError() {
        const v = input.validity;
        if (v.tooShort) {
          input.setCustomValidity(&#x27;Too short. Must be at least 8 characters.&#x27;);
          error.style.display = &#x27;block&#x27;;
          input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        } else {
          input.setCustomValidity(&#x27;&#x27;);
          error.style.display = &#x27;none&#x27;;
          input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
        }
      }

      input.addEventListener(&#x27;input&#x27;, updateError);
      input.addEventListener(&#x27;blur&#x27;, updateError);

      document.getElementById(&#x27;passwordForm&#x27;).addEventListener(&#x27;submit&#x27;, function (e) {
        updateError();
        if (!input.checkValidity()) {
          e.preventDefault();
          input.reportValidity();
        } else {
          e.preventDefault();
          alert(&#x27;Password is valid.&#x27;);
        }
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;title&gt;Password Field - Length Validation&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.4; padding: 2rem; }
    label { display: block; margin-bottom: 0.5rem; font-weight: 600; }
    input[type=&quot;password&quot;] { width: 100%; max-width: 320px; padding: 0.5rem; font-size: 1rem; }
    .error { color: #b00020; margin-top: 0.5rem; font-size: 0.95rem; }
  &lt;/style</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Password Field with Validation Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;div&gt;
      &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
      &lt;input
        id=&quot;new-password&quot;
        name=&quot;new-password&quot;
        type=&quot;password&quot;
        required
        minlength=&quot;8&quot;
        aria-describedby=&quot;new-password-error&quot;
        aria-invalid=&quot;true&quot;
        value=&quot;123&quot;
      /&gt;
      &lt;p id=&quot;new-password-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;
        Too short. Must be at least 8 characters.
      &lt;/p&gt;
    &lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;newPassword&quot; name=&quot;newPassword&quot; type=&quot;password&quot; required aria-describedby=&quot;newPasswordError newPasswordHelp&quot; /&gt;
&lt;small id=&quot;newPasswordError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color:#b00020;&quot;&gt;Too short. Must be at least 8 characters.&lt;/small&gt;
&lt;script&gt;
  (function () {
    const input = document.getElementById(&#x27;newPassword&#x27;);
    const error = document.getElementById(&#x27;newPasswordError&#x27;);

    function validate() {
      const isValid = input.value.length &gt;= 8;
      input.setCustomValidity(isValid ? &#x27;&#x27; : &#x27;Too short. Must be at least 8 characters.&#x27;);
      input.setAttribute(&#x27;aria-invalid&#x27;, String(!isValid));
      error.style.visibility = isValid ? &#x27;hidden&#x27; : &#x27;visible&#x27;;
    }

    input.addEventListener(&#x27;input&#x27;, validate);
    validate();
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;passwordForm&quot; novalidate&gt;
  &lt;div&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input
      id=&quot;new-password&quot;
      name=&quot;new-password&quot;
      type=&quot;password&quot;
      inputmode=&quot;text&quot;
      autocomplete=&quot;new-password&quot;
      aria-describedby=&quot;password-error&quot;
      required
    /&gt;
    &lt;p id=&quot;password-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; aria-atomic=&quot;true&quot;&gt;
      Too short. Must be at least 8 characters.
    &lt;/p&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Create password&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;new-password&#x27;);
      const error = document.getElementById(&#x27;password-error&#x27;);

      function validate() {
        const value = input.value;
        const isValid = value.length &gt;= 8;
        input.setAttribute(&#x27;aria-invalid&#x27;, String(!isValid));
        error.style.display = isValid ? &#x27;none&#x27; : &#x27;block&#x27;;
        return isValid;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      document.getElementById(&#x27;passwordForm&#x27;).addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validate()) {
          e.preventDefault();
          input.focus();
        }
      });

      // Initialize state
      validate();
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;new-password-error&quot;&gt;
  &lt;span id=&quot;new-password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input id=&quot;new-password&quot; type=&quot;password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;New password&lt;input type=&quot;password&quot; name=&quot;new-password&quot;&gt;&lt;/label&gt;&lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;&lt;input type=&quot;password&quot; id=&quot;new-password&quot; /&gt;&lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;new-password-error&quot;&gt;
&lt;span id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; minlength=&quot;8&quot; required&gt;
&lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
  &lt;div class=&quot;error-message&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; minlength=&quot;8&quot; required&gt;
  &lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; minlength=&quot;8&quot; required&gt;
&lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot;&gt;
  &lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot;&gt;
&lt;span class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; minlength=&quot;8&quot;&gt;
&lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;error-msg&quot;&gt;
&lt;div id=&quot;error-msg&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
