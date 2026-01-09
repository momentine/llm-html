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
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Color Question&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;&lt;br&gt;
    &lt;input id=&quot;orange-color&quot; name=&quot;orange-color&quot; type=&quot;text&quot; required&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;div style=&quot;color: #b00020; margin-top: 4px;&quot;&gt;That’s not right. Try again.&lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;colorForm&quot; novalidate&gt;
    &lt;label for=&quot;colorInput&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;colorInput&quot; name=&quot;color&quot; type=&quot;text&quot; autocomplete=&quot;off&quot; required /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;p id=&quot;errorMessage&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;That&#x27;s not right. Try again.&lt;/p&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;colorForm&#x27;);
      const input = document.getElementById(&#x27;colorInput&#x27;);
      const error = document.getElementById(&#x27;errorMessage&#x27;);

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
        const answer = input.value.trim().toLowerCase();
        if (answer === &#x27;orange&#x27;) {
          hideError();
          alert(&#x27;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Color Question&lt;/title&gt;
  &lt;style&gt;
    .error {
      color: #b00020;
      font-size: 0.95rem;
      margin-top: 0.35rem;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;colorForm&quot; novalidate&gt;
    &lt;label for=&quot;colorAnswer&quot;&gt;What color is an orange?&lt;/label&gt;&lt;br /&gt;
    &lt;input
      type=&quot;text&quot;
      id=&quot;colorAnswer&quot;
      name=&quot;colorAnswer&quot;
      required
      aria-describedby=&quot;colorError&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;p id=&quot;colorError&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;
      That’s not right. Try again.
    &lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;colorForm&#x27;);
      const input = document.getElementById(&#x27;colorAnswer&#x27;);
      const error = document.getElementById(&#x27;colorError&#x27;);

      function showError() {
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        error.hidden = false;
      }

      function clearError() {
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
        error.hidden = true;
      }

      input.addEventListener(&#x27;input&#x27;, function () {
        if (input.value.trim().toLowerCase() === &#x27;orange&#x27;) {
          clearError();
        }
      });

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        const value = input.value.trim().toLowerCase();
        if (value !== &#x27;orange&#x27;) {
          e.preventDefault();
          showError();
          input.focus();
        }
      });
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Orange Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;orangeForm&quot; novalidate&gt;
    &lt;label id=&quot;orangeLabel&quot; for=&quot;orangeAnswer&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input
      type=&quot;text&quot;
      id=&quot;orangeAnswer&quot;
      name=&quot;orangeAnswer&quot;
      aria-labelledby=&quot;orangeLabel&quot;
      aria-describedby=&quot;orangeError&quot;
      required
    /&gt;
    &lt;div id=&quot;orangeError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;orangeForm&#x27;);
      const input = document.getElementById(&#x27;orangeAnswer&#x27;);
      const error = document.getElementById(&#x27;orangeError&#x27;);

      function showError(msg) {
        error.textContent = msg;
        input.setCustomValidity(msg);
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function clearError() {
        error.textContent = &#x27;&#x27;;
        input.setCustomValidity(&#x27;&#x27;);
        input.removeAttribute(&#x27;aria-invalid&#x27;);
      }

      input.addEventListener(&#x27;input&#x27;, function () {
        const val = input.value.trim().toLowerCase();
        if (val === &#x27;orange&#x27;) {
          clearError();
        } else if (val.length &gt; 0) {
          showError(&quot;That&#x27;s not right. Try again.&quot;);
        } else {
          clearError();
        }
      });

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        const val = input.value.trim().toLowerCase();
        if (val !== &#x27;orange&#x27;) {
          e.preventDefault();
          showError(&quot;That&#x27;s not right. Try again.&quot;);
          input</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?” with a validation error “That’s not right. Try again.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Text Field with Validation&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.5; padding: 2rem; }
    .field { margin-bottom: 1rem; }
    label { display: block; font-weight: 600; margin-bottom: .25rem; }
    input[type=&quot;text&quot;] { width: 100%; max-width: 24rem; padding: .5rem; font-size: 1rem; }
    .error { color: #b00020; margin-top: .25rem; }
    [aria-invalid=&quot;true&quot;] { border-color: #b00020; outline-color: #b00020; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;colorForm&quot; novalidate&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;colorAnswer&quot;&gt;What color is an orange?&lt;/label&gt;
      &lt;input
        id=&quot;colorAnswer&quot;
        name=&quot;colorAnswer&quot;
        type=&quot;text&quot;
        inputmode=&quot;text&quot;
        autocomplete=&quot;off&quot;
        aria-describedby=&quot;colorHelp colorError&quot;
        aria-invalid=&quot;false&quot;
      /&gt;
      &lt;div id=&quot;colorHelp&quot; class=&quot;hint&quot;&gt;Enter a color name.&lt;/div&gt;
      &lt;p id=&quot;colorError&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; hidden&gt;&lt;/p&gt;
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Check answer&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;colorForm&#x27;);
      const input = document.getElementById(&#x27;colorAnswer&#x27;);
      const error = document.getElementById(&#x27;colorError&#x27;);

      function showError(message) {
        error.textContent = message;
        error.hidden = false;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      }

      function clearError() {
        error.textContent = &#x27;&#x27;;
        error.hidden</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
