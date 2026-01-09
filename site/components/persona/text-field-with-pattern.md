---
title: "text-field-with-pattern"
slug: text-field-with-pattern
track: persona
kind: component
order: 45
---

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
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;textField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;textField&quot; name=&quot;textField&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;textField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;textField&quot; name=&quot;textField&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; maxlength=&quot;5&quot; placeholder=&quot;AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
  required
  aria-describedby=&quot;code-format&quot;
  aria-required=&quot;true&quot;
  placeholder=&quot;AB123&quot;
&gt;
&lt;span id=&quot;code-format&quot; class=&quot;helper-text&quot;&gt;Format: Two letters followed by three numbers (e.g., AB123)&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; title=&quot;Format: Two letters followed by three numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;inputField&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;inputField&quot; name=&quot;inputField&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; title=&quot;Two letters followed by three numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by three numbers&quot; aria-label=&quot;Enter two letters followed by three numbers&quot; placeholder=&quot;AB123&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;codeInput&quot; pattern=&quot;[a-zA-Z]{2}[0-9]{3}&quot; title=&quot;Format: Two letters followed by three numbers (e.g., AB123)&quot; placeholder=&quot;LLNNN&quot; maxlength=&quot;5&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;code&quot; pattern=&quot;[</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Please enter two letters followed by three numbers (e.g., AB123).&quot; maxlength=&quot;5&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
&lt;body&gt;
    &lt;label for</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
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
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;code&quot; name=&quot;code&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; /&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
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
  &lt;input id=&quot;code&quot; name=&quot;code&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; required&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input id=&quot;code&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; /&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code-input&quot; type=&quot;text&quot; name=&quot;two-letters-three-numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
  &lt;input id=&quot;code&quot; name=&quot;code&quot; type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot; inputmode=&quot;text&quot; aria-describedby=&quot;codeHelp&quot;&gt;
  &lt;span id=&quot;codeHelp&quot;&gt;Example: AB123&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Please enter exactly two letters followed by three numbers&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; title=&quot;Enter two letters followed by three numbers&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;letter-number-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;letter-number-input&quot; name=&quot;letter-number-input&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/text-field-with-pattern/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;code-input&quot; name=&quot;code&quot; aria-label=&quot;Enter two letters followed by 3 numbers&quot; placeholder=&quot;AB123&quot; maxlength=&quot;5&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}\d{3}&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Enter two letters followed by 3 numbers</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; placeholder=&quot;Enter two letters followed by 3 numbers&quot; pattern=&quot;[A-Za-z]{2}[0-9]{3}&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code-input&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;code-input&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;codeInput&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;codeInput&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Enter two letters followed by 3 numbers”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;code&quot;&gt;Enter two letters followed by 3 numbers&lt;/label&gt;
&lt;input id=&quot;code&quot; type=&quot;text&quot; placeholder=&quot;AB123&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-pattern/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

