<details>
  <summary><strong>Password Field (Required)</strong></summary>
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
      <td>Insert a required password field for “New password”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;/submit&quot; method=&quot;post&quot;&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input id=&quot;new-password&quot; name=&quot;new_password&quot; type=&quot;password&quot; required autocomplete=&quot;new-password&quot; minlength=&quot;8&quot; placeholder=&quot;Enter new password&quot;&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-required/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field (required): New password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;newPassword&quot; type=&quot;password&quot; required placeholder=&quot;New password&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-required/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required password field labeled “New password”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; required autocomplete=&quot;new-password&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-required/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required password field and label for “New password”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; required autocomplete=&quot;new-password&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-required/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field (required) for “New password”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input
  id=&quot;new-password&quot;
  name=&quot;new_password&quot;
  type=&quot;password&quot;
  required
  autocomplete=&quot;new-password&quot;
  minlength=&quot;8&quot;
  inputmode=&quot;text&quot;
  aria-describedby=&quot;new-password-help new-password-error&quot;
  aria-invalid=&quot;false&quot;
/&gt;
&lt;button type=&quot;button&quot; id=&quot;toggle-password&quot; aria-pressed=&quot;false&quot; aria-controls=&quot;new-password&quot;&gt;Show password&lt;/button&gt;
&lt;div id=&quot;new-password-help&quot;&gt;Use at least 8 characters, including a number and a letter.&lt;/div&gt;
&lt;div id=&quot;new-password-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;&lt;/div&gt;

&lt;script&gt;
  (function () {
    const input = document.getElementById(&#x27;new-password&#x27;);
    const error = document.getElementById(&#x27;new-password-error&#x27;);
    const toggle = document.getElementById(&#x27;toggle-password&#x27;);

    function showError(message) {
      if (message) {
        error.textContent = message;
        error.hidden = false;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
      } else {
        error.textContent = &#x27;&#x27;;
        error.hidden = true;
        input.setAttribute(&#x27;aria-invalid&#x27;, &#x27;false&#x27;);
      }
    }

    function validate() {
      if (input</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-required/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
