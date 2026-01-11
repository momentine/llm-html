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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; required&gt;&lt;/textarea&gt;
  &lt;span class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot;&gt;&lt;/textarea&gt;
  &lt;span style=&quot;color: red; font-size: 14px;&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    aria-required=&quot;true&quot; 
    aria-invalid=&quot;true&quot; 
    aria-describedby=&quot;message-error&quot;
  &gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;
    Your message should be at least 20 words long. Please describe your problem in as much detail as possible.
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot; required minlength=&quot;20&quot;&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea name=&quot;message&quot; placeholder=&quot;Message&quot;&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
&lt;span id=&quot;message-error&quot; style=&quot;color: red;&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot; rows=&quot;5&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot; class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message-input&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message-input&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot; aria-invalid=&quot;true&quot;&gt;&lt;/textarea&gt;
  &lt;p id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;user-message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;user-message&quot; name=&quot;user-message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message-input&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message-input&quot; name=&quot;message&quot; aria-invalid=&quot;true</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;user-message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;user-message&quot; name=&quot;message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Contact Form with Message Validation&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;contact-form&quot; novalidate&gt;
    &lt;div&gt;
      &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
      &lt;textarea
        id=&quot;message&quot;
        name=&quot;message&quot;
        rows=&quot;6&quot;
        required
        aria-describedby=&quot;message-error&quot;
        aria-invalid=&quot;false&quot;
      &gt;&lt;/textarea&gt;
      &lt;div id=&quot;message-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #b00020; margin-top: 4px;&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;contact-form&#x27;);
      const messageEl = document.getElementById(&#x27;message&#x27;);
      const errorEl = document.getElementById(&#x27;message-error&#x27;);
      const MIN_WORDS = 20;

      function countWords(text) {
        const matches = text.trim().match(/[A-Za-z0-9\u00C0-\u017F]+(?:[&#x27;’\-][A-Za-z0-9\u00C0-\u017F]+)*/g);
        return matches ? matches.length : 0;
      }

      function validateMessage() {
        const value = messageEl.value;
        const count = countWords(value);

        if (count &lt; MIN_WORDS) {
          errorEl.textContent = &#x27;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&#x27;;
          messageEl.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
          return false;
        } else {
          errorEl.textContent = &#x27;&#x27;;
          messageEl.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
          return true;
        }
      }

      messageEl.addEventListener(&#x27;input&#x27;, validateMessage);
      messageEl.addEventListener(&#x27;blur&#x27;, validateMessage);

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validateMessage()) {
          e.preventDefault();
          messageEl.focus();</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with error message “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;contactForm&quot; novalidate&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; aria-describedby=&quot;message-error&quot; required&gt;&lt;/textarea&gt;
  &lt;p id=&quot;message-error&quot; class=&quot;error&quot; role=&quot;alert&quot; hidden&gt;
    Your message should be at least 20 words long. Please describe your problem in as much detail as possible.
  &lt;/p&gt;

  &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;contactForm&#x27;);
    const textarea = document.getElementById(&#x27;message&#x27;);
    const errorEl = document.getElementById(&#x27;message-error&#x27;);
    const MIN_WORDS = 20;

    function countWords(text) {
      if (!text) return 0;
      return text.trim().split(/\s+/).filter(Boolean).length;
    }

    function showError() {
      errorEl.hidden = false;
      textarea.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
    }

    function hideError() {
      errorEl.hidden = true;
      textarea.removeAttribute(&#x27;aria-invalid&#x27;);
    }

    function validate() {
      const words = countWords(textarea.value);
      if (words &lt; MIN_WORDS) {
        showError();
        return false;
      }
      hideError();
      return true;
    }

    textarea.addEventListener(&#x27;input&#x27;, validate);
    textarea.addEventListener(&#x27;blur&#x27;, validate);

    form.addEventListener(&#x27;submit&#x27;, function (e) {
      if (!validate()) {
        e.preventDefault();
        textarea.focus();
      }
    });
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;form id=&quot;contactForm&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;div&gt;
      &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
      &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;7&quot; required&gt;&lt;/textarea&gt;
      &lt;div id=&quot;message-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;contactForm&#x27;);
      const textarea = document.getElementById(&#x27;message&#x27;);
      const errorEl = document.getElementById(&#x27;message-error&#x27;);
      const MIN_WORDS = 20;
      const ERROR_MESSAGE = &#x27;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&#x27;;

      function countWords(text) {
        const trimmed = (text || &#x27;&#x27;).trim();
        if (!trimmed) return 0;
        return trimmed.split(/\s+/).filter(Boolean).length;
      }

      function validateMessage() {
        const words = countWords(textarea.value);
        if (words &lt; MIN_WORDS) {
          textarea.setCustomValidity(ERROR_MESSAGE);
          errorEl.textContent = ERROR_MESSAGE;
          textarea.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        } else {
          textarea.setCustomValidity(&#x27;&#x27;);
          errorEl.textContent = &#x27;&#x27;;
          textarea.removeAttribute(&#x27;aria-invalid&#x27;);
        }
      }

      textarea.addEventListener(&#x27;input&#x27;, validateMessage);
      textarea.addEventListener(&#x27;blur&#x27;, validateMessage);

      form.addEventListener(&#x27;submit&#x27;, function (</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;contactForm&quot; novalidate&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; placeholder=&quot;Please describe your problem in as much detail as possible.&quot; aria-describedby=&quot;messageError&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;messageError&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;div class=&quot;hint&quot; id=&quot;messageHint&quot;&gt;Words: &lt;span id=&quot;wordCount&quot;&gt;0&lt;/span&gt;/20&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;contactForm&#x27;);
    const textarea = document.getElementById(&#x27;message&#x27;);
    const errorEl = document.getElementById(&#x27;messageError&#x27;);
    const countEl = document.getElementById(&#x27;wordCount&#x27;);
    const requiredWords = 20;
    const errorMessage = &#x27;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&#x27;;

    function countWords(text) {
      const matches = text.trim().match(/[A-Za-z0-9\u00C0-\u017F]+(?:[&#x27;’-][A-Za-z0-9\u00C0-\u017F]+)*/g);
      return matches ? matches.length : 0;
    }

    function updateValidation() {
      const words = countWords(textarea.value);
      countEl.textContent = words;

      if (words &lt; requiredWords) {
        errorEl.textContent = errorMessage;
        textarea.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        textarea.setCustomValidity(errorMessage);
      } else {
        errorEl.textContent = &#x27;&#x27;;
        textarea.removeAttribute(&#x27;aria-invalid&#x27;);
        textarea.setCustom</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;8&quot; required aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;p id=&quot;message-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;
    Your message should be at least 20 words long. Please describe your problem in as much detail as possible.
  &lt;/p&gt;
  &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;6&quot; cols=&quot;40&quot;&gt;&lt;/textarea&gt;
  &lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; minlength=&quot;20&quot; required&gt;&lt;/textarea&gt;
  &lt;div&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
&lt;p role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
  &lt;p id=&quot;message-error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; required&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; required&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; required&gt;&lt;/textarea&gt;
&lt;div class=&quot;error-message&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
  &lt;span class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot;&gt;&lt;/textarea&gt;
  &lt;p&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
  &lt;div class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
&lt;p class=&quot;error&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a validation error “Your message should be at least 20 words long. Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; aria-describedby=&quot;message-error&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-error&quot; role=&quot;alert&quot;&gt;Your message should be at least 20 words long. Please describe your problem in as much detail as possible.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
