<details>
  <summary><strong>Textarea Field with Validation Error</strong></summary>
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
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot;&gt;&lt;/textarea&gt;
  &lt;span class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot;&gt;&lt;/textarea&gt;
&lt;span style=&quot;color: red; font-size: 14px;&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea 
    id=&quot;message&quot; 
    name=&quot;message&quot; 
    rows=&quot;5&quot; 
    aria-invalid=&quot;true&quot; 
    aria-describedby=&quot;message-error&quot;
    required
  &gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;
    Your message should be at least 20 words long. Please describe your problem in as much detail as possible.
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot; required&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Textarea Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot;&gt;&lt;/textarea&gt;
    &lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Textarea Field Example&lt;/title&gt;
  &lt;meta</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Textarea Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Message Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;message-field&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message-field&quot; name=&quot;message&quot; rows=&quot;8&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
        &lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Accessible Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
    &lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;contactForm&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;8&quot; placeholder=&quot;Describe your problem in as much detail as possible...&quot; required aria-describedby=&quot;messageError messageCounter&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;messageCounter&quot; aria-live=&quot;polite&quot;&gt;0 words (minimum 20)&lt;/div&gt;
  &lt;p id=&quot;messageError&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; hidden&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;

  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const errorEl = document.getElementById(&#x27;messageError&#x27;);
      const counterEl = document.getElementById(&#x27;messageCounter&#x27;);
      const MIN_WORDS = 20;

      function countWords(text) {
        const matches = text.trim().match(/\b[\p{L}\p{N}’&#x27;-]+\b/gu);
        return matches ? matches.length : 0;
      }

      function updateState() {
        const count = countWords(textarea.value);
        counterEl.textContent = count + &#x27; word&#x27; + (count === 1 ? &#x27;&#x27; : &#x27;s&#x27;) + &#x27; (minimum &#x27; + MIN_WORDS + &#x27;)&#x27;;

        const isValid = count &gt;= MIN_WORDS;
        textarea.setAttribute(&#x27;aria-invalid&#x27;, String(!isValid));

        if (!isValid) {
          errorEl.hidden = false;
          errorEl.textContent = &#x27;Your message should be at least &#x27; + MIN_WORDS + &#x27; words long. Please describe your problem in as much detail as possible.&#x27;;
        } else {
          errorEl.hidden = true;
          errorEl.textContent = &#x27;&#x27;;
        }
      }

      textarea.addEventListener(&#x27;input&#x27;, updateState);
      textarea.addEventListener(&#x27;blur&#x27;, updateState);

      document.getElementById(&#x27;contactForm&#x27;).addEventListener(&#x27;submit&#x27;, function (e) {
        updateState();
        const isValid = countWords(textarea.value) &gt;= MIN_WORDS;
        if (!isValid) {
          e.preventDefault();
          textarea.focus();
        }
      });

      updateState();
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Message Validation&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;contactForm&quot; novalidate&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; required aria-describedby=&quot;messageError&quot; aria-invalid=&quot;false&quot;&gt;&lt;/textarea&gt;
    &lt;p id=&quot;messageError&quot; role=&quot;alert&quot; style=&quot;display:none;color:#b00020;margin-top:4px;&quot;&gt;
      Your message should be at least 20 words long. Please describe your problem in as much detail as possible.
    &lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    const form = document.getElementById(&#x27;contactForm&#x27;);
    const textarea = document.getElementById(&#x27;message&#x27;);
    const errorEl = document.getElementById(&#x27;messageError&#x27;);

    function countWords(text) {
      const matches</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message Validation&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.5; padding: 2rem; }
    .field { margin-bottom: 1rem; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    textarea { width: 100%; min-height: 140px; padding: 0.75rem; border: 1px solid #c7c7c7; border-radius: 6px; resize: vertical; }
    textarea:focus { outline: none; border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,.2); }
    textarea:invalid { border-color: #dc2626; }
    .error { color: #dc2626; margin-top: 0.5rem; font-size: 0.95rem; }
    .error[hidden] { display: none; }
    .actions { margin-top: 1rem; }
    button { background: #111827; color: #fff; border: 0; border-radius: 6px; padding: 0.6rem 1rem; cursor: pointer; }
    button:hover { background: #0b1220; }
    .success { color: #059669; margin-top: 0.75rem; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Message Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;main&gt;
    &lt;form id=&quot;contactForm&quot; novalidate&gt;
      &lt;div&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;8&quot; aria-describedby=&quot;messageHelp&quot;&gt;&lt;/textarea&gt;
        &lt;div id=&quot;messageHelp&quot; style=&quot;margin-top:4px;color:#555;&quot;&gt;Please include as much detail as possible.&lt;/div&gt;
        &lt;div id=&quot;messageError&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; style=&quot;margin-top:6px;color:#b00020;&quot;&gt;&lt;/div&gt;
      &lt;/div&gt;
      &lt;button type=&quot;submit&quot; style=&quot;margin-top:12px;&quot;&gt;Send&lt;/button&gt;
    &lt;/form&gt;
  &lt;/main&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;contactForm&#x27;);
      const textarea = document.getElementById(&#x27;message&#x27;);
      const errorBox = document.getElementById(&#x27;messageError&#x27;);
      const help = document.getElementById(&#x27;messageHelp&#x27;);

      const ERROR_TEXT = &#x27;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&#x27;;

      function countWords(text) {
        const trimmed = text.trim();
        if (!trimmed) return 0;
        return trimmed.split(/\s+/).filter(Boolean).length;
      }

      function showError() {
        errorBox.textContent = ERROR_TEXT;
        textarea.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        // Ensure assistive tech announces the error in addition to the help text
        textarea</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; cols=&quot;40&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;p id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Contact Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; cols=&quot;50&quot; placeholder=&quot;Please describe your problem in as much detail as possible...&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;span style=&quot;color: red; font-size: 14px;&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;&lt;br&gt;&lt;br&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; cols=&quot;40&quot;&gt;&lt;/textarea&gt;
  &lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; cols=&quot;40&quot;&gt;&lt;/textarea&gt;
        &lt;div class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; cols=&quot;40&quot;&gt;&lt;/textarea&gt;
        &lt;div class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
&lt;p style=&quot;color: red;&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
  &lt;p class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; required&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
