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
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot; name=&quot;codeInput&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; placeholder=&quot;AB123&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; placeholder=&quot;AB123&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot; name=&quot;codeInput&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Accessible Text Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
    &lt;input 
        type=&quot;text&quot; 
        id=&quot;code-input&quot; 
        name=&quot;code-input&quot;
        pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
        maxlength=&quot;5&quot;
        placeholder=&quot;AB123&quot;
        aria-describedby=&quot;code-help&quot;
        required
    &gt;
    &lt;small id=&quot;code-help&quot;&gt;Format: Two letters followed by three numbers (e.g., AB123)&lt;/small&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; title=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Input Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;&lt;br&gt;
        &lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; title=&quot;Two letters followed by three numbers&quot; required&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by 3 numbers&quot; placeholder=&quot;e.g., AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; aria-describedby=&quot;hint&quot; required&gt;
&lt;div id=&quot;hint&quot; aria-live=&quot;polite&quot;&gt;Example: AB123&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Text Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;custom_code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;custom_code&quot; name=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Text Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Text Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;custom_code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;custom_code&quot; name=&quot;custom_code&quot; pattern=&quot;[a-zA-Z]{2}[0-9]{3}&quot; title=&quot;Format: LLNNN (e.g</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Accessible Text Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
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
  inputmode=&quot;latin&quot;
  pattern=&quot;[A-Za-z]{2}\\d{3}&quot;
  maxlength=&quot;5&quot;
  placeholder=&quot;AB123&quot;
  autocomplete=&quot;off&quot;
  title=&quot;Enter exactly 2 letters followed by 3 numbers (e.g., AB123)&quot;
/&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;title&gt;Two Letters + Three Numbers&lt;/title&gt;
&lt;body&gt;
&lt;label for=&quot;code&quot;&gt;Enter code (2 letters + 3 numbers):&lt;/label&gt;
&lt;input id=&quot;code&quot; name=&quot;code&quot; type=&quot;text&quot; inputmode=&quot;latin&quot; autocomplete=&quot;off&quot; placeholder=&quot;AB123&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; required title=&quot;Enter two letters followed by three numbers (e.g., AB123).&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Two Letters + Three Numbers Input&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input
    id=&quot;code&quot;
    name=&quot;code&quot;
    type=&quot;text&quot;
    placeholder=&quot;AB123&quot;
    pattern=&quot;[A-Za-z]{2}[0-9]{3</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Two Letters + Three Numbers Input&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input
    id=&quot;code&quot;
    name=&quot;code&quot;
    type=&quot;text&quot;
    inputmode=&quot;text&quot;
    autocomplete=&quot;off&quot;
    autocapitalize=&quot;characters&quot;
    placeholder=&quot;AB123&quot;
    pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot;
    title=&quot;Format: 2 letters followed by 3 numbers (e.g., AB123)&quot;
    required
  /&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; title=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;code&quot;&gt;Enter code:&lt;/label&gt;
&lt;input id=&quot;code&quot; name=&quot;code&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; placeholder=&quot;AB123&quot; required&gt;
&lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Enter two letters followed by 3 numbers&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; /&gt;&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;codeField&quot; name=&quot;codeField&quot; type=&quot;text&quot; inputmode=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; aria-describedby=&quot;codeHelp&quot; required&gt;
&lt;div id=&quot;codeHelp&quot;&gt;Example: AB123&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Text Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;
        &lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter exactly two letters followed by three numbers&quot; required&gt;
        &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Input Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;
        &lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers:&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Please enter exactly two letters followed by three numbers&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;code-input&quot; aria-label=&quot;Enter two letters followed by 3 numbers&quot; placeholder=&quot;AB123&quot; maxlength=&quot;5&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Please enter two letters followed by three numbers&quot; autocomplete=&quot;off&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;html&gt;
&lt;body&gt;
&lt;form&gt;
&lt;label for=&quot;inputField&quot;&gt;Text field:&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; required&gt;
&lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
&lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot; placeholder=&quot;e.g., AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code-input&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; aria-describedby=&quot;format-help&quot;&gt;
&lt;span id=&quot;format-help&quot;&gt;Format: two uppercase or lowercase letters followed by three digits.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
