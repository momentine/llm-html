<details>
  <summary><strong>Credit Card Field</strong></summary>
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
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input
  type=&quot;text&quot;
  id=&quot;credit-card-number&quot;
  name=&quot;creditCardNumber&quot;
  inputmode=&quot;numeric&quot;
  autocomplete=&quot;cc-number&quot;
  placeholder=&quot;1234 5678 9012 3456&quot;
  pattern=&quot;[0-9 ]{12,23}&quot;
  maxlength=&quot;23&quot;
  aria-describedby=&quot;cc-number-hint&quot;
  required
/&gt;
&lt;small id=&quot;cc-number-hint&quot;&gt;Enter the number without dashes or spaces; they will be ignored.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/credit-card-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input
  id=&quot;cc-number&quot;
  name=&quot;cc-number&quot;
  type=&quot;text&quot;
  inputmode=&quot;numeric&quot;
  autocomplete=&quot;cc-number&quot;
  placeholder=&quot;1234 5678 9012 3456&quot;
  aria-describedby=&quot;cc-number-hint&quot;
  pattern=&quot;[0-9\s]{12,23}&quot;
  maxlength=&quot;23&quot;
  required
/&gt;
&lt;small id=&quot;cc-number-hint&quot;&gt;Enter the number as it appears on the card, digits only.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/credit-card-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Credit Card Number Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
    &lt;input
      id=&quot;cc-number&quot;
      name=&quot;cc-number&quot;
      type=&quot;text&quot;
      inputmode=&quot;numeric&quot;
      autocomplete=&quot;cc-number&quot;
      placeholder=&quot;1234 5678 9012 3456&quot;
      aria-describedby=&quot;cc-number-hint&quot;
      required
    /&gt;
    &lt;div id=&quot;cc-number-hint&quot; aria-hidden=&quot;true&quot;&gt;Enter the 13–19 digit number on the front of your card.&lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/credit-card-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Credit Card Number Field&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; }
    .field { max-width: 28rem; }
    label { display: block; font-weight: 600; margin-bottom: .375rem; }
    input[type=&quot;tel&quot;] {
      width: 100%;
      padding: .65rem .75rem;
      font-size: 1rem;
      line-height: 1.2;
      border: 1px solid #c7c7c7;
      border-radius: .375rem;
      outline: none;
      transition: border-color .15s ease;
    }
    input[type=&quot;tel&quot;]:focus { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,.15); }
    .hint { font-size: .875rem; color: #666; margin-top: .375rem; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; autocomplete=&quot;on&quot;&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
      &lt;input
        id=&quot;cc-number&quot;
        name=&quot;cc-number&quot;
        type=&quot;tel&quot;
        inputmode=&quot;numeric&quot;
        autocomplete=&quot;cc-number&quot;
        placeholder=&quot;1234 5678 9012 3456&quot;
        aria-describedby=&quot;cc-number-hint&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/credit-card-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;payment-form&quot; novalidate&gt;
  &lt;div class=&quot;field&quot;&gt;
    &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
    &lt;div id=&quot;cc-help&quot; class=&quot;help&quot;&gt;Enter the number as it appears on your card.&lt;/div&gt;
    &lt;input
      id=&quot;cc-number&quot;
      name=&quot;cc-number&quot;
      type=&quot;text&quot;
      inputmode=&quot;numeric&quot;
      autocomplete=&quot;cc-number&quot;
      placeholder=&quot;1234 5678 9012 3456&quot;
      aria-describedby=&quot;cc-help cc-error&quot;
      aria-invalid=&quot;false&quot;
      required
    /&gt;
    &lt;div id=&quot;cc-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Pay&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const input = document.getElementById(&#x27;cc-number&#x27;);
    const errorEl = document.getElementById(&#x27;cc-error&#x27;);

    const CARD_GAPS = [4, 8, 12, 16]; // positions where a space is inserted
    const MAX_DIGITS = 19; // supports up to 19 digits (UPI, etc.)

    const cardPatterns = {
      amex</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/credit-card-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
