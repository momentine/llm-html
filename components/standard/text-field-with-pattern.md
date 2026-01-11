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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot; name=&quot;codeInput&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; placeholder=&quot;e.g., AB123&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;textField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;textField&quot; name=&quot;textField&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; placeholder=&quot;AB123&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;textField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;textField&quot; name=&quot;textField&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot; name=&quot;codeInput&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; placeholder=&quot;AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input 
  type=&quot;text&quot; 
  id=&quot;code-input&quot; 
  name=&quot;code&quot; 
  pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; 
  maxlength=&quot;5&quot;
  aria-describedby=&quot;code-hint&quot;
  required
&gt;
&lt;span id=&quot;code-hint&quot;&gt;Format: Two letters followed by three numbers (e.g., AB123)&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;field&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;field&quot; name=&quot;field&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; aria-describedby=&quot;hint&quot; required&gt;
&lt;p id=&quot;hint&quot;&gt;Example: AB123&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;alphaNumInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;alphaNumInput&quot; name=&quot;alphaNum</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;custom-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;custom-input&quot; name=&quot;custom-</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;code-input</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code_input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code_input&quot; name=&quot;code_input&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
	&lt;label for=&quot;accessCode&quot;&gt;Access Code&lt;/label&gt;
	&lt;input type=&quot;text&quot; id=&quot;accessCode&quot; name=&quot;accessCode&quot; pattern=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input
  id=&quot;code&quot;
  name=&quot;code&quot;
  type=&quot;text&quot;
  placeholder=&quot;AB123&quot;
  pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
  maxlength=&quot;5&quot;
  title=&quot;Enter exactly two letters followed by three numbers (e.g., AB123)&quot;
  required
/&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Two Letters + Three Numbers&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;codeForm&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
    &lt;input
      id=&quot;code&quot;
      name=&quot;code&quot;
      type=&quot;text&quot;
      inputmode=&quot;latin&quot;
      autocomplete=&quot;off&quot;
      autocapitalize=&quot;characters&quot;
      spellcheck=&quot;false&quot;
      placeholder=&quot;AB123&quot;
      maxlength=&quot;5&quot;
      pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
      aria-describedby=&quot;hint error&quot;
      required
    &gt;
    &lt;div id=&quot;hint&quot; style=&quot;font-size:0.9em;color:#555;margin-top:0.25rem;&quot;&gt;Format: 2 letters + 3 digits (e.g., AB123)&lt;/div&gt;
    &lt;div id=&quot;error&quot; role=&quot;alert&quot; style=&quot;font-size:0.9em;color:#b00020;margin-top:0.25rem;display:none;&quot;&gt;Please enter exactly 2 letters followed by 3 digits.&lt;/div&gt;

    &lt;button type=&quot;submit&quot; style=&quot;margin-top:0.75rem;&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const input = document.getElementById(&#x27;code&#x27;);
      const form = document.getElementById(&#x27;codeForm&#x27;);
      const errorEl = document.getElementById(&#x27;error&#x27;);

      function isLetter(ch) {
        return /^[A-Za-z]$/.test(ch);
      }
      function isDigit(ch) {
        return /^[0-9]$/.test(ch);
      }

      input.addEventListener(&#x27;keydown&#x27;, function (e) {
        const pos = this.selectionStart;
        const val = this.value;
        const key = e.key;

        if (key === &#x27;Tab&#x27; || key === &#x27;Enter&#x27; || key === &#x27;Escape&#x27; || key === &#x27;ArrowLeft&#x27; || key === &#x27;ArrowRight&#x27; || key === &#x27;ArrowUp</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Code Input&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
    &lt;input
      id=&quot;code&quot;
      name=&quot;code&quot;
      type=&quot;text&quot;
      placeholder=&quot;AB123&quot;
      inputmode=&quot;text&quot;
      autocapitalize=&quot;characters&quot;
      autocomplete=&quot;off&quot;
      spellcheck=&quot;false&quot;
      maxlength=&quot;5&quot;
      required
      pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
      title=&quot;Two letters followed by three numbers (e.g., AB123)&quot;
      aria-describedby=&quot;code-hint&quot;
    &gt;
    &lt;small id=&quot;code-hint&quot;&gt;Format: 2 letters + 3 numbers (e.g., AB123)&lt;/small&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; maxlength=&quot;5&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Format: two letters followed by three numbers, e.g., AB123&quot; required&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input
    id=&quot;code&quot;
    name=&quot;code&quot;
    type=&quot;text&quot;
    inputmode=&quot;latin&quot;
    autocomplete=&quot;one-time-code&quot;
    placeholder=&quot;AB123&quot;
    maxlength=&quot;5&quot;
    pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
    aria-describedby=&quot;code-help&quot;
    aria-label=&quot;Two letters followed by three numbers&quot;
    required
  /&gt;
  &lt;div id=&quot;code-help&quot; role=&quot;note&quot;&gt;Format: 2 letters then 3 digits (e.g., AB123). Use uppercase or lowercase letters.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; maxlength=&quot;5&quot; placeholder=&quot;AB123&quot; required&gt;
&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Enter two letters followed by 3 numbers
&lt;input type=&quot;text&quot;&gt;
&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code&quot; type=&quot;text&quot; minlength=&quot;5&quot; maxlength=&quot;5&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code&quot; name=&quot;code&quot; type=&quot;text&quot; inputmode=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; aria-describedby=&quot;code-format&quot; aria-required=&quot;true&quot;&gt;
&lt;div id=&quot;code-format&quot;&gt;Example: AB123&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by 3 numbers&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;letterNumberInput&quot; name=&quot;letterNumberInput&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Please enter exactly two letters followed by exactly three numbers&quot; required&gt;
&lt;label for=&quot;letterNumberInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by 3 numbers&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;code&quot; aria-describedby=&quot;code-format&quot; maxlength=&quot;5&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; required&gt;
&lt;div id=&quot;code-format&quot;&gt;Enter two letters followed by 3 numbers (e.g., AB123)&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; placeholder=&quot;e.g., AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
