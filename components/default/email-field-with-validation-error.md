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
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Email Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
        &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
        &lt;span id=&quot;email-error&quot;&gt;Your email address is invalid.&lt;/span&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
  &lt;input 
    type=&quot;email&quot; 
    id=&quot;email-address&quot; 
    name=&quot;email&quot; 
    aria-invalid=&quot;true&quot; 
    aria-describedby=&quot;email-error&quot;
    value=&quot;&quot;
  &gt;
  &lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;p id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;span id=&quot;email-error&quot; style=&quot;color: red;&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;p style=&quot;color: red; margin: 0.5rem 0; font-size: 0.875rem;&quot;&gt;Your email address is invalid.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot; required&gt;
  &lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
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
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot; aria-invalid=&quot;true&quot; required&gt;
  &lt;div id=&quot;email-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
        &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required pattern=&quot;[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$&quot; title=&quot;Your email address is invalid.&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Email Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;email_address&quot;&gt;Email Address&lt;/label&gt;
        &lt;input type=&quot;email&quot; id=&quot;email_address&quot; name=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email_error&quot;&gt;
        &lt;p id=&quot;email_error&quot;&gt;Your email address is invalid.&lt;/p&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Email Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
  &lt;span&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Accessible Email Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;emailForm&quot; novalidate&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required aria-describedby=&quot;emailError&quot; aria-invalid=&quot;false&quot; /&gt;
  &lt;p id=&quot;emailError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #b00020; margin: 4px 0 0; min-height: 1.2em;&quot;&gt;&lt;/p&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;emailForm&#x27;);
      const email = document.getElementById(&#x27;email&#x27;);
      const error = document.getElementById(&#x27;emailError&#x27;);

      function showError() {
        error.textContent = &#x27;Your email address is invalid.&#x27;;
        email.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function clearError() {
        error.textContent = &#x27;&#x27;;
        email.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }

      email.addEventListener(&#x27;input&#x27;, function () {
        if (email.validity.typeMismatch) {
          showError();
        } else {
          clearError();
        }
      });

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (email.validity.typeMismatch) {
          e.preventDefault();
          showError();
        }
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Email Field with Validation&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;emailForm&quot; novalidate&gt;
    &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
    &lt;input
      type=&quot;email&quot;
      id=&quot;email&quot;
      name=&quot;email&quot;
      required
      aria-describedby=&quot;email-error&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;p id=&quot;email-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;
      Your email address is invalid.
    &lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementBy</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;email</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
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
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;div id=&quot;email-error&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;span id=&quot;email-error&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Email Address&lt;input type=&quot;email&quot; aria-invalid=&quot;true&quot;&gt;&lt;/label&gt;
&lt;p&gt;Your email address is invalid.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; value=&quot;&quot;&gt;
&lt;span&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
  &lt;input id=&quot;email&quot; name=&quot;email&quot; type=&quot;email&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;email-error&quot;&gt;
  &lt;p id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
  &lt;div class=&quot;error-message&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field: Email Address with error message “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;email&quot; name=&quot;email&quot; required&gt;
&lt;div class=&quot;error-message&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;span class=&quot;error&quot;&gt;Your email address is invalid.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build an email field and label for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
  &lt;div class=&quot;error&quot;&gt;Your email address is invalid.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
&lt;div id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert an email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot; required&gt;
&lt;div&gt;Your email address is invalid.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
  &lt;p&gt;Your email address is invalid.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>An email field labeled “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
  &lt;input type=&quot;email&quot; id=&quot;email&quot; name=&quot;email&quot;&gt;
  &lt;div&gt;Your email address is invalid.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
&lt;span&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field for “Email Address” with a validation error “Your email address is invalid.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;email&quot;&gt;Email Address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;email&quot; aria-describedby=&quot;email-error&quot;&gt;
&lt;span id=&quot;email-error&quot; role=&quot;alert&quot;&gt;Your email address is invalid.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/email-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
