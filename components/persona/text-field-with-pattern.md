<details>
  <summary><strong>Text Field with Pattern</strong></summary>
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
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Two Letters + Three Numbers&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; padding: 2rem; }
    .field { margin-bottom: 1rem; }
    label { display: block; margin-bottom: .25rem; font-weight: 600; }
    input { font-size: 1rem; padding: .5rem .6rem; width: 12rem; }
    .hint { font-size: .9rem; color: #555; }
    .error { color: #b00020; font-size: .9rem; margin-top: .25rem; min-height: 1.2em; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;codeForm&quot; novalidate&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;code&quot;&gt;Code&lt;/label&gt;
      &lt;input
        id=&quot;code&quot;
        name=&quot;code&quot;
        type=&quot;text&quot;
        inputmode=&quot;latin&quot;
        autocomplete=&quot;off&quot;
        autocapitalize=&quot;characters&quot;
        placeholder=&quot;AB123&quot;
        maxlength=&quot;5&quot;
        pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
        aria-describedby=&quot;codeHint codeError&quot;
        required
      /&gt;
      &lt;div id=&quot;codeHint&quot; class=&quot;hint&quot;&gt;Enter two letters followed by three numbers (e.g., AB123).&lt;/div&gt;
      &lt;div id=&quot;codeError&quot; class=&quot;error&quot; role</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Two Letters + Three Numbers&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    label { display: block; margin-bottom: .5rem; font-weight: 600; }
    input { padding: .5rem; font-size: 1rem; width: 12rem; }
    .row { display: flex; gap: .75rem; align-items: center; }
    .msg { margin-top: .5rem; font-size: .95rem; }
    .ok { color: #0a7f2e; }
    .err { color: #b00020; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;codeForm&quot; novalidate&gt;
    &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
    &lt;div class=&quot;row&quot;&gt;
      &lt;input
        id=&quot;code&quot;
        name=&quot;code&quot;
        type=&quot;text&quot;
        inputmode=&quot;text&quot;
        autocomplete=&quot;off&quot;
        spellcheck=&quot;false&quot;
        placeholder=&quot;AB123&quot;
        maxlength=&quot;5&quot;
        pattern=&quot;^[A-Za-z]{2}[0-9]{3}$&quot;
        title=&quot;Format: two letters followed by three numbers (e.g., AB123)&quot;
        required
        aria-describedby=&quot;codeHelp codeMsg&quot;
      /&gt;
      &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;/div&gt;
    &lt;div</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Two Letters + Three Numbers&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input
    id=&quot;code&quot;
    name=&quot;code&quot;
    type=&quot;text&quot;
    maxlength=&quot;5&quot;
    pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
    title=&quot;Format: two letters followed by three numbers (e.g., AB123)&quot;
    placeholder=&quot;AB123&quot;
  &gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;code-form&quot; novalidate&gt;
  &lt;div&gt;
    &lt;label for=&quot;code&quot;&gt;Code&lt;/label&gt;
    &lt;input
      id=&quot;code&quot;
      name=&quot;code&quot;
      type=&quot;text&quot;
      inputmode=&quot;text&quot;
      autocomplete=&quot;one-time-code&quot;
      placeholder=&quot;Enter two letters followed by 3 numbers&quot;
      aria-describedby=&quot;code-hint code-error&quot;
      aria-invalid=&quot;false&quot;
      maxlength=&quot;5&quot;
      pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
      title=&quot;Enter exactly two letters followed by three numbers (e.g., AB123).&quot;
      required
    /&gt;
    &lt;div id=&quot;code-hint&quot;&gt;Format: 2 letters followed by 3 numbers (e.g., AB123).&lt;/div&gt;
    &lt;div id=&quot;code-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;code-form&#x27;);
    const input = document.getElementById(&#x27;code&#x27;);
    const error = document.getElementById(&#x27;code-error&#x27;);

    function setError(msg) {
      error.textContent = msg;
      input.setAttribute(&#x27;aria-invalid&#x27;, msg ? &#x27;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
