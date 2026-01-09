<details>
  <summary><strong>Password Field with Autocomplete Suggestion</strong></summary>
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
      <td>Insert a password field for “new-password” with autocomplete=new-password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; autocomplete=&quot;new-password&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-autocomplete-suggestion/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: new-password with autocomplete=new-password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;New Password Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input id=&quot;new-password&quot; type=&quot;new-password&quot; autocomplete=&quot;new-password&quot; /&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-autocomplete-suggestion/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “new-password” with autocomplete=new-password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;new-password&quot; type=&quot;password&quot; autocomplete=&quot;new-password&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-autocomplete-suggestion/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “new-password” with autocomplete=new-password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;New Password Field&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; autocomplete=&quot;new-password&quot;&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input id=&quot;new-password&quot; type=&quot;password&quot; autocomplete=&quot;new-password&quot; required&gt;
    &lt;button type=&quot;submit&quot;&gt;Save&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-autocomplete-suggestion/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “new-password” with autocomplete=new-password</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;new-password-form&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
  &lt;div&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;div class=&quot;password-field&quot;&gt;
      &lt;input
        id=&quot;new-password&quot;
        name=&quot;new-password&quot;
        type=&quot;password&quot;
        inputmode=&quot;text&quot;
        autocomplete=&quot;new-password&quot;
        spellcheck=&quot;false&quot;
        aria-describedby=&quot;new-password-help new-password-error&quot;
        required
      /&gt;
      &lt;button
        type=&quot;button&quot;
        class=&quot;toggle-visibility&quot;
        aria-controls=&quot;new-password&quot;
        aria-pressed=&quot;false&quot;
        aria-label=&quot;Show password&quot;
      &gt;
        Show
      &lt;/button&gt;
    &lt;/div&gt;
    &lt;div id=&quot;new-password-help&quot; class=&quot;help-text&quot;&gt;
      Use at least 12 characters with a mix of letters, numbers, and symbols.
    &lt;/div&gt;
    &lt;div id=&quot;new-password-error&quot; class=&quot;error-text&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;

  &lt;div&gt;
    &lt;label for=&quot;strength-meter&quot;&gt;Password strength&lt;/label&gt;
    &lt;div
      id=&quot;strength-meter&quot;
      class=&quot;strength-meter&quot;
      role=&quot;progressbar&quot;
      aria-label=&quot;Password strength&quot;
      aria-valuemin=&quot;0&quot;
      aria-valuemax=&quot;5&quot;
      aria-valuenow=&quot;0&quot;
    &gt;
      &lt;div class=&quot;strength-bar&quot; style=&quot;width: 0%&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;
    &lt;div id=&quot;strength-text&quot; class=&quot;strength-text&quot; aria-live=&quot;polite&quot;&gt;Strength: empty&lt;/div&gt;
  &lt;/div&gt;

  &lt;button type=&quot;submit&quot;&gt;Create password&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElement</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-autocomplete-suggestion/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
