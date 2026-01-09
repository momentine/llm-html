<details>
  <summary><strong>Email Field with Required</strong></summary>
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
      <td>Insert a required email field for “Desired email address”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Desired Email Address&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;desired-email&quot;&gt;Desired email address&lt;/label&gt;
    &lt;input
      id=&quot;desired-email&quot;
      name=&quot;desired_email&quot;
      type=&quot;email&quot;
      placeholder=&quot;you@example.com&quot;
      autocomplete=&quot;email&quot;
      required
    /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    document.querySelector(&#x27;form&#x27;).addEventListener(&#x27;submit&#x27;, (e) =&gt; {
      e.preventDefault();
      const email = document.getElementById(&#x27;desired-email&#x27;).value.trim();
      if (email) {
        alert(&#x27;Submitted: &#x27; + email);
      }
    });
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-required/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Email field (required): Desired email address</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;desired_email&quot;&gt;Email field (required): Desired email address&lt;/label&gt;
&lt;input type=&quot;email&quot; id=&quot;desired_email&quot; name=&quot;desired_email&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-required/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required email field labeled “Desired email address”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Desired Email Address&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;desired_email&quot;&gt;Desired email address&lt;/label&gt;
    &lt;input type=&quot;email&quot; id=&quot;desired_email&quot; name=&quot;desired_email&quot; required placeholder=&quot;name@example.com&quot;&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-required/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required email field and label for “Desired email address”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;desired-email&quot;&gt;Desired email address&lt;/label&gt;
&lt;input id=&quot;desired-email&quot; name=&quot;desired_email&quot; type=&quot;email&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-required/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible email field (required) for “Desired email address”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;profile-form&quot; novalidate&gt;
  &lt;div class=&quot;field&quot;&gt;
    &lt;label for=&quot;desired-email&quot;&gt;Desired email address &lt;span aria-hidden=&quot;true&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
    &lt;p id=&quot;desired-email-help&quot; class=&quot;help&quot;&gt;Use a format like name@example.com.&lt;/p&gt;
    &lt;input
      id=&quot;desired-email&quot;
      name=&quot;desiredEmail&quot;
      type=&quot;email&quot;
      inputmode=&quot;email&quot;
      autocomplete=&quot;email&quot;
      required
      aria-required=&quot;true&quot;
      aria-describedby=&quot;desired-email-help desired-email-error&quot;
      aria-invalid=&quot;false&quot;
    /&gt;
    &lt;p id=&quot;desired-email-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;&lt;/p&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Save&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;profile-form&#x27;);
      const input = document.getElementById(&#x27;desired-email&#x27;);
      const errorEl = document.getElementById(&#x27;desired-email-error&#x27;);

      function setError(message) {
        errorEl.textContent = message || &#x27;&#x27;;
        input.setAttribute(&#x27;aria-invalid&#x27;, message ? &#x27;true&#x27; : &#x27;false&#x27;);
      }

      function validate() {
        const value = input.value.trim();
        if (!value) {
          setError(&#x27;Please enter the desired email address.&#x27;);
          return false;
        }
        // Use native validation for type/format; add a friendly message.
        if (!input.checkValidity()) {
          setError(&#x27;Please enter a valid email address (e.g., name@example.com).&#x27;);
          return false;
        }
        setError(&#x27;&#x27;);
        return true;
      }

      input.addEventListener(&#x27;input&#x27;, validate);
      input.addEventListener(&#x27;blur&#x27;, validate);

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validate()) {
          e.preventDefault();
          input.focus();
        }
      });
    })();
  &lt;/script</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/email-field-with-required/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
