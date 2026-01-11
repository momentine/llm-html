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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;creditCard&quot;&gt;Credit Card Number&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;creditCard&quot; name=&quot;creditCard&quot; placeholder=&quot;1234 5678 9012 3456&quot; maxlength=&quot;19&quot; autocomplete=&quot;cc-number&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;creditCard&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;creditCard&quot; name=&quot;creditCard&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]*&quot; maxlength=&quot;19&quot; placeholder=&quot;1234 5678 9012 3456&quot; autocomplete=&quot;cc-number&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;creditCard&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;creditCard&quot; name=&quot;creditCard&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]{13,19}&quot; maxlength=&quot;19&quot; placeholder=&quot;1234 5678 9012 3456&quot; autocomplete=&quot;cc-number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;creditCard&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;creditCard&quot; name=&quot;creditCard&quot; maxlength=&quot;19&quot; placeholder=&quot;1234 5678 9012 3456&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]{13,19}&quot; autocomplete=&quot;cc-number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;creditCardNumber&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input 
  type=&quot;text&quot; 
  id=&quot;creditCardNumber&quot; 
  name=&quot;creditCardNumber&quot; 
  autocomplete=&quot;cc-number&quot; 
  inputmode=&quot;numeric&quot; 
  pattern=&quot;[0-9\s]{13,19}&quot; 
  maxlength=&quot;19&quot; 
  required 
  aria-required=&quot;true&quot; 
  aria-describedby=&quot;creditCardHelp&quot;
  placeholder=&quot;1234 5678 9012 3456&quot;
&gt;
&lt;span id=&quot;creditCardHelp&quot;&gt;Enter your 13-19 digit credit card number&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Credit Card Number&quot; name=&quot;credit_card_number&quot; pattern=&quot;[0-9]{13,16}&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Credit Card Number&quot; name=&quot;credit_card_number&quot; pattern=&quot;[0-9\s]{13,19}&quot; autocomplete=&quot;cc-number&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Credit Card Number&quot; name=&quot;creditCardNumber&quot; id=&quot;creditCardNumber&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]{13,19}&quot; autocomplete=&quot;cc-number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]{13,19}&quot; autocomplete=&quot;cc-number&quot; aria-required=&quot;true&quot; aria-describedby=&quot;cc-help&quot;&gt;
&lt;span id=&quot;cc-help&quot; class=&quot;sr-only&quot;&gt;Enter your credit card number without spaces or dashes.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-num&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;tel&quot; id=&quot;cc-num&quot; name=&quot;credit-card-number&quot; autocomplete=&quot;cc-number&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9\s]{13,19}&quot; placeholder=&quot;xxxx xxxx xxxx xxxx&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;cc-number&quot; name=&quot;cc-number&quot; inputmode=&quot;numeric&quot; pattern=&quot;[\d ]{13,19}&quot; autocomplete=&quot;cc-number&quot; placeholder=&quot;xxxx xxxx xxxx xxxx&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;tel&quot; id=&quot;cc-number&quot; name=&quot;credit-card-number&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;cc-number&quot; name=&quot;credit-card-number&quot; autocomplete=&quot;cc-number</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Accessible Credit Card Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input
  id=&quot;cc-number&quot;
  name=&quot;cc-number&quot;
  type=&quot;tel&quot;
  inputmode=&quot;numeric&quot;
  autocomplete=&quot;cc-number&quot;
  placeholder=&quot;1234 5678 9012 3456&quot;
  required
  pattern=&quot;[0-9\s]{13,23}&quot;
  maxlength=&quot;23&quot;
  aria-describedby=&quot;cc-number-help&quot;
/&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;title&gt;Credit Card Number Field&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;payment-form&quot; novalidate&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
      &lt;input
        id=&quot;cc-number&quot;
        name=&quot;cc-number&quot;
        type=&quot;text&quot;
        inputmode=&quot;numeric&quot;
        autocomplete=&quot;cc-number&quot;
        placeholder=&quot;1234 5678 9012 3456&quot;
        aria-describedby=&quot;cc-number-help cc-number-error&quot;
        aria-invalid=&quot;false&quot;
        maxlength=&quot;23&quot;
        required
      /&gt;
      &lt;div id=&quot;cc-number-help&quot; class=&quot;help&quot;&gt;Enter the number without spaces or dashes.&lt;/div&gt;
      &lt;div id=&quot;cc-number-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;cc-number&#x27;);
      const errorEl = document.getElementById(&#x27;cc-number-error&#x27;);
      const form</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
    &lt;input
      id=&quot;cc-number&quot;
      name=&quot;creditCardNumber&quot;
      type=&quot;text&quot;
      inputmode=&quot;numeric&quot;
      autocomplete=&quot;cc-number&quot;
      placeholder=&quot;1234 5678 9012 3456&quot;
      pattern=&quot;[0-9][0-9 ,.-]{11,23}&quot;
      maxlength=&quot;24&quot;
      required
      aria-describedby=&quot;cc-number-help&quot;
    /&gt;
    &lt;div id=&quot;cc-number-help&quot; aria-live=&quot;polite&quot;&gt;Enter 13–19 digits. Spaces and dashes are allowed.&lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Credit Card Number Field&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; margin: 2rem; line-height: 1.5; }
    .field { max-width: 28rem; }
    label { display: block; font-weight: 600; margin-bottom: 0.25rem; }
    input[type=&quot;text&quot;] { width: 100%; font-size: 1rem; padding: 0.625rem 0.75rem; border: 1px solid #c7c7c7; border-radius: 0.375rem; outline: none; }
    input[type=&quot;text&quot;]:focus { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,.2); }
    .hint { font-size: 0.875rem; color: #666; margin-top: 0.25rem; }
    .error { font-size: 0.875rem; color: #b00020; margin-top: 0.25rem; min-height: 1.2em; }
    .invalid { border-color: #b00020 !important; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class=&quot;field&quot;&gt;
    &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
    &lt;input
      id=&quot;cc-number&quot;
      name=&quot;cc-number&quot;
      type=&quot;text&quot;
      inputmode=&quot;numeric&quot;
      autocomplete=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Credit Card Number&lt;/title&gt;
  &lt;style&gt;
    :root {
      --fg: #0b0b0c;
      --bg: #ffffff;
      --muted: #5c6670;
      --border: #c6c9cf;
      --focus: #0a84ff;
      --error: #b00020;
      --success: #0f7b0f;
    }
    html, body {
      margin: 0;
      padding: 0;
      background: var(--bg);
      color: var(--fg);
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      line-height: 1.5;
    }
    .container {
      max-width: 520px;
      margin: 4rem auto;
      padding: 0 1rem;
    }
    h1 {
      font-size: 1.25rem;
      margin: 0 0 1rem;
    }
    .field {
      margin-block: 1rem;
    }
    label {
      display: inline-block;
      font-weight: 600;
      margin-bottom: 0.25rem;
    }
    .hint {
      color: var(--muted);
      font-size: 0.9375rem;
      margin-top: 0.25rem;
    }
    input[type=&quot;text&quot;] {
      width: 100%;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;card-number&quot; name=&quot;credit_card_number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;cc-number&quot; name=&quot;credit-card-number&quot; placeholder=&quot;Credit Card Number&quot; inputmode=&quot;numeric&quot; autocomplete=&quot;cc-number&quot; required&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;ccnumber&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;ccnumber&quot; name=&quot;ccnumber&quot; inputmode=&quot;numeric&quot; autocomplete=&quot;cc-number&quot; placeholder=&quot;0000 0000 0000 0000&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; inputmode=&quot;numeric&quot; autocomplete=&quot;cc-number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;cc-number&quot;&gt;Credit Card Number&lt;/label&gt;
  &lt;input id=&quot;cc-number&quot; name=&quot;cc-number&quot; type=&quot;text&quot; inputmode=&quot;numeric&quot; autocomplete=&quot;cc-number&quot; aria-describedby=&quot;cc-help&quot; required&gt;
  &lt;span id=&quot;cc-help&quot;&gt;Enter the 16-digit number found on the front of your card.&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;credit_card_number&quot; placeholder=&quot;Credit Card Number&quot; maxlength=&quot;19&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;creditCardNumber&quot; name=&quot;creditCardNumber&quot; placeholder=&quot;Enter credit card number&quot; maxlength=&quot;19&quot; autocomplete=&quot;cc-number&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; placeholder=&quot;Credit Card Number&quot; autocomplete=&quot;cc-number&quot; inputmode=&quot;numeric&quot; pattern=&quot;[0-9]*&quot; maxlength=&quot;19&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; placeholder=&quot;1234 5678 9012 3456&quot; maxlength=&quot;19&quot; pattern=&quot;[0-9]{4} [0-9]{4} [0-9]{4} [0-9]{4}&quot;&gt;
&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
  &lt;input 
    type=&quot;text&quot; 
    id=&quot;credit-card-number&quot; 
    name=&quot;credit-card-number&quot; 
    inputmode=&quot;numeric&quot; 
    pattern=&quot;[0-9\s]{13,19}&quot; 
    maxlength=&quot;19&quot; 
    placeholder=&quot;1234 5678 9012 3456&quot; 
    autocomplete=&quot;cc-number&quot; 
    required
  &gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; maxlength=&quot;19&quot; placeholder=&quot;1234 5678 9012 3456&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Credit card field: Credit Card Number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit_card_number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit_card_number&quot; name=&quot;credit_card_number&quot; maxlength=&quot;19&quot; placeholder=&quot;XXXX XXXX XXXX XXXX&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A credit card field labeled “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; maxlength=&quot;19&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a credit card field and label for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; maxlength=&quot;19&quot; placeholder=&quot;1234 5678 9012 3456&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible credit card field for “Credit Card Number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;credit-card-number&quot;&gt;Credit Card Number&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;credit-card-number&quot; name=&quot;credit-card-number&quot; autocomplete=&quot;cc-number&quot; inputmode=&quot;numeric&quot; aria-describedby=&quot;cc-help&quot;&gt;
&lt;span id=&quot;cc-help&quot; class=&quot;sr-only&quot;&gt;Enter your 16-digit credit card number without spaces or dashes.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/credit-card-field/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
