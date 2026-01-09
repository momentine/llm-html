<details>
  <summary><strong>Text Field with Validation Error</strong></summary>
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
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Form with Validation&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
        &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;error-message&quot;&gt;
        &lt;span id=&quot;error-message&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/span&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Text Field with Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;colorInput&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;colorInput&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;errorMessage&quot;&gt;
    &lt;div id=&quot;errorMessage&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;orange-error&quot;&gt;
  &lt;div id=&quot;orange-error&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;orangeColor&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orangeColor&quot; name=&quot;orangeColor&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;orangeColorError&quot;&gt;
  &lt;span id=&quot;orangeColorError&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;div&gt;
            &lt;label for=&quot;color-input&quot;&gt;What color is an orange?&lt;/label&gt;
            &lt;input 
                type=&quot;text&quot; 
                id=&quot;color-input&quot; 
                name=&quot;color-input&quot; 
                aria-invalid=&quot;true&quot; 
                aria-describedby=&quot;color-error&quot;
            &gt;
            &lt;div id=&quot;color-error&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
        &lt;/div&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;What color is an orange?&quot; required oninvalid=&quot;this.setCustomValidity(&#x27;That’s not right. Try again.&#x27;)&quot; oninput=&quot;this.setCustomValidity(&#x27;&#x27;)&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;answer&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;answer&quot; name=&quot;answer&quot; required&gt;
  &lt;div style=&quot;color: red; font-size: 0.9em; margin-top: 5px;&quot;&gt;That’s not right. Try again.&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;What color is an orange?&quot; aria-label=&quot;What color is an orange?&quot;&gt;
&lt;p style=&quot;color: red; font-size: 0.9rem; margin-top: 0.5rem;&quot;&gt;That’s not right. Try again.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; required&gt;
  &lt;div style=&quot;color: red; display: none;&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color&quot; name=&quot;color&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;error-msg&quot;&gt;
  &lt;div id=&quot;error-msg&quot; role=&quot;alert&quot;&gt;That’s not right. Try again.&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Form Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;color-question&quot;&gt;What color is an orange?&lt;/label&gt;
        &lt;input type=&quot;text&quot; id=&quot;color-question&quot; name=&quot;color-question&quot;&gt;
        &lt;p&gt;That’s not right. Try again</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Text Field with Error&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Input Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;color-error&quot;&gt;
    &lt;div id=&quot;color-error&quot;&gt;That’s not right. Try again.&lt;/div&gt;
&lt;/body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Form Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;color-error&quot;&gt;
    &lt;p id=&quot;color-error&quot;&gt;That’s not right. Try again.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Accessible Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;orangeForm&quot; novalidate&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color&quot; name=&quot;color&quot; required aria-describedby=&quot;colorError&quot;&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;div id=&quot;colorError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;That’s not right. Try again.&lt;/div&gt;
&lt;/form&gt;

&lt;script&gt;
  const form = document.getElementById(&#x27;orangeForm&#x27;);
  const input = document.getElementById(&#x27;color&#x27;);
  const error = document.getElementById(&#x27;colorError&#x27;);

  form.addEventListener(&#x27;submit&#x27;, function (e) {
    const value = input.value.trim().toLowerCase();
    if (value !== &#x27;orange&#x27;) {
      e.preventDefault();
      input.setCustomValidity(&#x27;invalid&#x27;);
      error.hidden = false;
      error.textContent = &quot;That’s not right. Try again.&quot;;
      input.reportValidity();
    } else {
      input.setCustomValidity(&#x27;&#x27;);
      error.hidden = true;
    }
  });</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;color-form&quot; novalidate&gt;
    &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;color&quot; name=&quot;color&quot; type=&quot;text&quot; autocomplete=&quot;off&quot; required /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

    &lt;p id=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; style=&quot;color: #b00020; margin-top: 8px;&quot;&gt;
      That’s not right. Try again.
    &lt;/p&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;color-form&#x27;);
      const input = document.getElementById(&#x27;color&#x27;);
      const error = document.getElementById(&#x27;error&#x27;);

      function showError() {
        error.style.display = &#x27;block&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function hideError() {
        error.style.display = &#x27;none&#x27;;
        input.removeAttribute(&#x27;aria-invalid&#x27;);
      }

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        e.preventDefault();
        const value = (input.value || &#x27;&#x27;).trim().toLowerCase();
        if (value !== &#x27;orange&#x27;) {
          showError();
        } else {
          hideError();
          alert(&#x27;Correct!&#x27;);
        }
      });

      input.addEventListener(&#x27;input&#x27;, function () {
        const value = (input.value || &#x27;&#x27;).trim().toLowerCase();
        if (value &amp;&amp; value !== &#x27;orange&#x27;) {
          showError();
        } else {
          hideError();
        }
      });</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;colorForm&quot; novalidate&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input
    id=&quot;color&quot;
    name=&quot;color&quot;
    type=&quot;text&quot;
    inputmode=&quot;text&quot;
    autocomplete=&quot;off&quot;
    required
    aria-describedby=&quot;colorError&quot;
    aria-invalid=&quot;true&quot;
  /&gt;
  &lt;div id=&quot;colorError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #b00020; margin-top: 4px;&quot;&gt;
    That&#x27;s not right. Try again.
  &lt;/div&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;colorForm&#x27;);
    const input = document.getElementById(&#x27;color&#x27;);
    const error = document.getElementById(&#x27;colorError&#x27;);

    function isCorrect(value) {
      return value.trim().toLowerCase() === &#x27;orange&#x27;;
    }

    function validate() {
      if (input.value.trim() === &#x27;&#x27;) {
        input.setCustomValidity(&#x27;&#x27;);
        error.textContent = &#x27;&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
        return;
      }

      if (!isCorrect(input.value)) {
        input.setCustomValidity(&quot;That&#x27;s not right. Try again.&quot;);
        error.textContent = &quot;That&#x27;s not right. Try again.&quot;;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      } else {
        input.setCustomValidity(&#x27;&#x27;);
        error.textContent = &#x27;&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }
    }

    input.addEventListener(&#x27;input&#x27;, validate);
    form.addEventListener(&#x27;submit&#x27;, function (e) {
      validate();
      if (!form.checkValidity()) {
        e.preventDefault();
        form.reportValidity();
      }
    });
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;orangeColor&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input id=&quot;orangeColor&quot; name=&quot;orangeColor&quot; required pattern=&quot;[Oo][Rr][Aa][Nn][Gg][Ee]+&quot; title=&quot;That’s not right. Try again.&quot;&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input
    id=&quot;orange-color&quot;
    name=&quot;orange-color&quot;
    type=&quot;text&quot;
    required
    aria-describedby=&quot;orange-error&quot;
    title=&quot;That’s not right. Try again.&quot;
  /&gt;
  &lt;div id=&quot;orange-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;That’s not right. Try again.&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-describedby=&quot;orange-color-error&quot;&gt;
  &lt;span id=&quot;orange-color-error&quot;&gt;That’s not right. Try again.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;color-question&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color-question&quot; name=&quot;color-question&quot;&gt;
  &lt;p&gt;That’s not right. Try again.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input id=&quot;orange-color&quot; type=&quot;text&quot; aria-describedby=&quot;orange-color-error&quot;&gt;
&lt;div id=&quot;orange-color-error&quot;&gt;That’s not right. Try again.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-describedby=&quot;orange-error&quot;&gt;
&lt;p id=&quot;orange-error&quot;&gt;That’s not right. Try again.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;orange-question&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input id=&quot;orange-question&quot; name=&quot;orange-question&quot; aria-describedby=&quot;orange-error&quot; aria-invalid=&quot;true&quot;&gt;
&lt;p id=&quot;orange-error&quot;&gt;That’s not right. Try again.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; required&gt;
  &lt;div class=&quot;error&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;What color is an orange?&quot;&gt;
&lt;p&gt;That&#x27;s not right. Try again.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; required&gt;
  &lt;div class=&quot;error-message&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot;&gt;
&lt;div class=&quot;error&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orange-color&quot; aria-describedby=&quot;error-message&quot; aria-invalid=&quot;true&quot; /&gt;
&lt;div id=&quot;error-message&quot; role=&quot;alert&quot;&gt;That&#x27;s not right. Try again.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color&quot; name=&quot;color&quot;&gt;
  &lt;p&gt;That’s not right. Try again.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: “What color is an orange?” with error message “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;html&gt;
&lt;body&gt;
&lt;p&gt;The color of an orange is &lt;strong&gt;orange&lt;/strong&gt;.&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;orangeColor&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;orangeColor&quot;&gt;
&lt;p&gt;That’s not right. Try again.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color&quot; name=&quot;color&quot;&gt;
  &lt;span&gt;That’s not right. Try again.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;color&quot; aria-describedby=&quot;error&quot;&gt;
  &lt;p id=&quot;error&quot; role=&quot;alert&quot;&gt;That’s not right. Try again.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
