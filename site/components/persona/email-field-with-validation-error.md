---
title: "email-field-with-validation-error"
slug: email-field-with-validation-error
track: persona
kind: component
order: 17
---

<details>
  <summary><strong>Email Field with Validation Error</strong></summary>
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
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;span style=&quot;color: red; font-size: 14px;&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email-input&quot;&gt;Email Address&lt;/label&gt;
  &lt;input 
    type=&quot;email&quot; 
    id=&quot;email-input&quot; 
    name=&quot;email&quot; 
    aria-invalid=&quot;true&quot; 
    aria-describedby=&quot;email-error&quot;
    value=&quot;&quot;
  /&gt;
  &lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;email&quot; name=&quot;email&quot; placeholder=&quot;Email Address&quot; required oninvalid=&quot;this.setCustomValidity(&#x27;Your email address is invalid.&#x27;)&quot; oninput=&quot;this.setCustomValidity(&#x27;&#x27;)&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;email&quot; placeholder=&quot;Email Address&quot; required&gt;
&lt;div class=&quot;error&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
&lt;span style=&quot;color: red; display: none;&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Email Field&lt;/title&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email-address&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email-address&quot; name=&quot;email&quot; value=&quot;invalid-email@&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;
    Your email address is invalid.
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email-address&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email-address&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot; value=&quot;not-an-email&quot;&gt;
  &lt;div id=&quot;email-error&quot; role=&quot;alert&quot; style=&quot;color: red; font-size: 0.8em;&quot;&gt;
    Your email address is invalid.
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email-address&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email-address&quot; name=&quot;email-address&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;div id=&quot;email-error&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email-address&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email-address&quot; name=&quot;email&quot; autocomplete=&quot;email&quot; required aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;p id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Email Field with Validation&lt;/title&gt;
  &lt;style&gt;
    .field { margin-bottom: 1rem; }
    label { display:block; margin-bottom: .25rem; font-weight: 600; }
    input[type=&quot;email&quot;] { width: 100%; padding: .5rem; font-size: 1rem; }
    .error { color: #b00020; margin-top: .25rem; font-size: .95rem; }
    .hidden { display: none; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;emailForm&quot; novalidate&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
      &lt;input
        id=&quot;email&quot;
        name=&quot;email&quot;
        type=&quot;email&quot;
        required
        aria-describedby=&quot;emailError&quot;
        aria-invalid=&quot;false&quot;
      /&gt;
      &lt;p id=&quot;emailError&quot; class=&quot;error hidden&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/p&gt;
    &lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;emailForm&#x27;);
      const email = document.getElementById(&#x27;email&#x27;);
      const error = document.getElementById(&#x27;emailError&#x27;);
      const errorMessage = &#x27;Your email address is invalid.&#x27;;

      function showError() {
        error.textContent = errorMessage;
        error.classList.remove(&#x27;hidden&#x27;);
        email.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function clearError() {
        error.textContent = &#x27;&#x27;;
        error.classList.add(&#x27;hidden&#x27;);
        email.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }

      email.addEventListener(&#x27;input&#x27;, () =&gt; {</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input
    id=&quot;email&quot;
    name=&quot;email&quot;
    type=&quot;email&quot;
    required
    title=&quot;Your email address is invalid.&quot;
  /&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Email Validation Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
    &lt;input id=&quot;email&quot; name=&quot;email&quot; type=&quot;email&quot; required aria-describedby=&quot;email-error&quot; aria-invalid=&quot;true&quot;&gt;
    &lt;p id=&quot;email-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;Your email address is invalid.&lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;emailForm&quot; novalidate&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input
    id=&quot;email&quot;
    name=&quot;email&quot;
    type=&quot;email&quot;
    required
    aria-describedby=&quot;emailError&quot;
    aria-invalid=&quot;false&quot;
  /&gt;
  &lt;p id=&quot;emailError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/p&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const emailInput = document.getElementById(&#x27;email&#x27;);
      const emailError = document.getElementById(&#x27;emailError&#x27;);
      const form = document.getElementById(&#x27;emailForm&#x27;);

      function updateError() {
        if (emailInput.validity.valid) {
          emailError.textContent = &#x27;&#x27;;
          emailInput.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
        } else {
          emailError.textContent = &#x27;Your email address is invalid.&#x27;;
          emailInput.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        }
      }

      emailInput.addEventListener(&#x27;input&#x27;, updateError);
      emailInput.addEventListener(&#x27;blur&#x27;, updateError);

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        updateError();
        if (!emailInput.validity.valid) {
          e.preventDefault();
          emailInput.focus();
        }
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input
    id=&quot;email&quot;
    name=&quot;email&quot;
    type=&quot;email&quot;
    required
    aria-describedby=&quot;email-error&quot;
    aria-invalid=&quot;true&quot;
    inputmode=&quot;email&quot;
    autocomplete=&quot;email&quot;
    placeholder=&quot;name@example.com&quot;
  /&gt;
  &lt;div id=&quot;email-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;
    Your email address is invalid.
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input id=&quot;email&quot; name=&quot;email&quot; type=&quot;email&quot; required&gt;
  &lt;p&gt;Your email address is invalid.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; value=&quot;invalid@example&quot; aria-invalid=&quot;true&quot;&gt;
  &lt;p&gt;Your email address is invalid.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot;&gt;
&lt;p&gt;Your email address is invalid.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot; required&gt;
&lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input id=&quot;email&quot; type=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot; value=&quot;&quot;&gt;
&lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;span class=&quot;error&quot; id=&quot;email-error&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;span class=&quot;error-message&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
&lt;span class=&quot;error&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
&lt;div class=&quot;error&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot; required&gt;
&lt;div id=&quot;email-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address:&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;&lt;br&gt;
  &lt;span&gt;Your email address is invalid.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
&lt;span class=&quot;error&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
&lt;span&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot;&gt;
&lt;div class=&quot;error&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; aria-describedby=&quot;email-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

