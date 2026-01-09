<details>
  <summary><strong>Confirmation Checkbox</strong></summary>
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
      <td>Insert a checkbox for “I agree to the Terms and Conditions”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;agree-terms&quot; name=&quot;agree_terms&quot; required&gt;
    I agree to the &lt;a href=&quot;/terms&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;Terms and Conditions&lt;/a&gt;
  &lt;/label&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/confirmation-checkbox/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox: I agree to the Terms and Conditions</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Terms Agreement&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/submit&quot; method=&quot;post&quot;&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;agree&quot; name=&quot;agree&quot; value=&quot;yes&quot; required aria-required=&quot;true&quot;&gt;
      &lt;label for=&quot;agree&quot;&gt;I agree to the &lt;a href=&quot;/terms&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;Terms and Conditions&lt;/a&gt;&lt;/label&gt;
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/confirmation-checkbox/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox labeled “I agree to the Terms and Conditions”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Terms Agreement Checkbox&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;agree-terms&quot; name=&quot;agree-terms&quot; /&gt;
      I agree to the Terms and Conditions
    &lt;/label&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/confirmation-checkbox/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox and label for “I agree to the Terms and Conditions”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;agree-terms&quot;&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;agree-terms&quot; name=&quot;agree_terms&quot; required&gt;
  I agree to the &lt;a href=&quot;/terms&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;Terms and Conditions&lt;/a&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/confirmation-checkbox/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox for “I agree to the Terms and Conditions”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Accessible Terms Checkbox&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;main&gt;
    &lt;h1&gt;Create your account&lt;/h1&gt;

    &lt;form action=&quot;/signup&quot; method=&quot;post&quot; novalidate&gt;
      &lt;div&gt;
        &lt;input
          type=&quot;checkbox&quot;
          id=&quot;agree&quot;
          name=&quot;agree&quot;
          required
          aria-describedby=&quot;agree-help terms-link&quot;
        &gt;
        &lt;label for=&quot;agree&quot;&gt;
          I agree to the &lt;a id=&quot;terms-link&quot; href=&quot;/terms&quot; target=&quot;_blank&quot; rel=&quot;noopener noreferrer&quot;&gt;Terms and Conditions&lt;/a&gt;
        &lt;/label&gt;
        &lt;div id=&quot;agree-help&quot;&gt;You must agree before creating an account.&lt;/div&gt;
      &lt;/div&gt;

      &lt;button type=&quot;submit&quot;&gt;Sign up&lt;/button&gt;
    &lt;/form&gt;
  &lt;/main&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/confirmation-checkbox/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
