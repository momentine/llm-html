---
title: "password-field-with-validation-error"
slug: password-field-with-validation-error
track: persona
kind: component
order: 25
---

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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
  &lt;span id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
  &lt;span id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;new-password-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;span id=&quot;new-password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
  &lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;
    Too short. Must be at least 8 characters.
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; placeholder=&quot;New password&quot; required minlength=&quot;8&quot;&gt;
&lt;span style=&quot;color: red; display: block;&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
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
    &lt;form&gt;
        &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
        &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required minlength=&quot;8&quot;&gt;
        &lt;div style=&quot;color: red; font-size: 0.875rem; margin-top: 0.25rem;&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;p id=&quot;password-error&quot; style=&quot;color: red;&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;p id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; minlength=&quot;8&quot; required aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot; required minlength=&quot;8&quot;&gt;
  &lt;p id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot; required minlength=&quot;8&quot; autocomplete=&quot;new-password&quot;&gt;
  &lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; minlength=&quot;8&quot; required aria-invalid=&quot;true&quot; aria-describedby=&quot;password-error&quot;&gt;
&lt;p id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
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
  &lt;title&gt;Password Field with Validation&lt;/title&gt;
  &lt;style&gt;
    .field { margin-bottom: 1rem; }
    .error { color: #b00020; font-size: 0.9rem; margin-top: 0.25rem; }
    .invalid { border-color: #b00020; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;passwordForm&quot; novalidate&gt;
    &lt;div class=&quot;field&quot;&gt;
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
      &lt;div id=&quot;passwordError&quot; class=&quot;error&quot; role=&quot;alert&quot; hidden&gt;Too short. Must be at least 8 characters.&lt;/div&gt;
    &lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Save&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;newPassword&#x27;);
      const errorEl = document.getElementById(&#x27;passwordError&#x27;);
      const errorId = &#x27;passwordError&#x27;;

      function showError() {
        errorEl.hidden = false;
        input.classList.add(&#x27;invalid&#x27;);
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function hideError() {
        errorEl.hidden = true;
        input.classList.remove(&#x27;invalid&#x27;);
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }

      function validate() {
        const value = input.value;
        if (value.length === 0) {
          hideError();
          return true;
        }
        if (value.length &lt; 8) {
          showError();
          return false;
        }
        hideError();
        return true;
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
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
  &lt;p id=&quot;passwordError&quot; role=&quot;alert&quot; style=&quot;color:#b00020; display:none; margin:4px 0 0;&quot;&gt;
    Too short. Must be at least 8 characters.
  &lt;/p&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  const input = document.getElementById(&#x27;newPassword&#x27;);
  const errorEl = document.getElementById(&#x27;passwordError&#x27;);

  function updateError() {
    const tooShort = input.value.length &gt; 0 &amp;&amp; input.value.length &lt; 8;
    if (tooShort) {
      errorEl.style.display = &#x27;block&#x27;;
      input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
    } else {
      errorEl.style.display = &#x27;none&#x27;;
      input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
    }
  }

  input.addEventListener(&#x27;input&#x27;, updateError);
  input.addEventListener(&#x27;blur&#x27;, updateError);

  document.getElementById(&#x27;passwordForm&#x27;).addEventListener(&#x27;submit&#x27;, (e) =&gt; {
    updateError();
    if (input.value.length &lt; 8) {
      e.preventDefault();
      input.focus();
    }
  });
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;passwordForm&quot;&gt;
  &lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
  &lt;input id=&quot;newPassword&quot; name=&quot;newPassword&quot; type=&quot;password&quot; required aria-describedby=&quot;newPasswordError&quot; /&gt;
  &lt;div id=&quot;newPasswordError&quot; role=&quot;alert&quot; style=&quot;color: #b00020; margin-top: 4px;&quot;&gt;&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;newPassword&#x27;);
      const error = document.getElementById(&#x27;newPasswordError&#x27;);

      function validate() {
        const value = input.value;
        if (value.length === 0) {
          error.textContent = &#x27;&#x27;;
          input.setCustomValidity(&#x27;&#x27;);
          return;
        }
        if (value.length &lt; 8) {
          const msg = &#x27;Too short. Must be at least 8 characters.&#x27;;
          error.textContent = msg;
          input.setCustomValidity(msg);
        } else {
          error.textContent = &#x27;&#x27;;
          input.setCustomValidity(&#x27;&#x27;);
        }
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      document.getElementById(&#x27;passwordForm&#x27;).addEventListener(&#x27;submit&#x27;, function (e) {
        validate();
        if (!input.validity.valid) {
          e.preventDefault();
          input.reportValidity();
        }
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Password Field with Validation&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form novalidate&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input id=&quot;new-password&quot; name=&quot;new-password&quot; type=&quot;password&quot; minlength=&quot;8&quot; required aria-describedby=&quot;password-error&quot;&gt;
    &lt;p id=&quot;password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;new-password&#x27;);
      const error = document.getElementById(&#x27;password-error&#x27;);

      function update() {
        if (input.value.length ===</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
    &lt;div style=&quot;position:relative;display:flex;align-items:center;&quot;&gt;
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
      &lt;button
        type=&quot;button&quot;
        id=&quot;toggle-password&quot;
        aria-label=&quot;Show password&quot;
        aria-controls=&quot;new-password&quot;
        aria-expanded=&quot;false&quot;
        style=&quot;margin-left:8px;&quot;
      &gt;
        Show
      &lt;/button&gt;
    &lt;/div&gt;
    &lt;p id=&quot;new-password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;
      Too short. Must be at least 8 characters.
    &lt;/p&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Create account&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;new-password&#x27;);
      const error = document.getElementById(&#x27;new-password-error&#x27;);
      const toggle = document.getElementById(&#x27;toggle-password&#x27;);

      function validate() {
        const valid = input.value.length &gt;= 8;
        error.hidden = valid;
        input.setAttribute(&#x27;aria-invalid&#x27;, String(!valid));
        return valid;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      input.addEventListener(&#x27;blur&#x27;, validate);

      toggle.addEventListener(&#x27;click&#x27;, () =&gt; {
        const isHidden = input.type === &#x27;password&#x27;;
        input.type = isHidden ? &#x27;text&#x27; : &#x27;password&#x27;;
        toggle.textContent = isHidden ? &#x27;Hide&#x27;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;new-password-error&quot;&gt;
&lt;p id=&quot;new-password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
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
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;p id=&quot;password-error&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
&lt;div&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;p id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
&lt;div class=&quot;error&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-error&quot; aria-invalid=&quot;true&quot; minlength=&quot;8&quot; required&gt;
&lt;div id=&quot;password-error&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; required minlength=&quot;8&quot;&gt;
  &lt;span id=&quot;error-message&quot; style=&quot;color: red;&quot;&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with error message “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newpassword&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;newpassword&quot; name=&quot;newpassword&quot;&gt;
&lt;p&gt;Too short. Must be at least 8 characters.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot;&gt;
  &lt;span&gt;Too short. Must be at least 8 characters.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with a validation error “Too short. Must be at least 8 characters.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;error-message&quot;&gt;
&lt;div id=&quot;error-message&quot; role=&quot;alert&quot;&gt;Too short. Must be at least 8 characters.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/password-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

