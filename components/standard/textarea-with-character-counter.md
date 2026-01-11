<details>
  <summary><strong>Textarea with Character Counter</strong></summary>
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
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; oninput=&quot;updateCounter()&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt; / 200 characters
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
  function updateCounter() {
    const textarea = document.getElementById(&#x27;message&#x27;);
    const charCount = document.getElementById(&#x27;charCount&#x27;);
    charCount.textContent = textarea.value.length;
  }
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; style=&quot;width: 100%; padding: 8px; font-family: Arial, sans-serif; font-size: 14px; border: 1px solid #ccc; border-radius: 4px; resize: vertical;&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
  &lt;div style=&quot;text-align: right; margin-top: 4px; font-size: 12px; color: #666;&quot;&gt;
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot; oninput=&quot;updateCounter()&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt; / 200 characters
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
function updateCounter() {
  const textarea = document.getElementById(&#x27;message&#x27;);
  const charCount = document.getElementById(&#x27;charCount&#x27;);
  charCount.textContent = textarea.value.length;
}
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea 
    id=&quot;message&quot; 
    name=&quot;message&quot; 
    maxlength=&quot;200&quot; 
    rows=&quot;5&quot; 
    aria-describedby=&quot;message-counter message-help&quot;
    required
  &gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-help&quot;&gt;Please enter your message (maximum 200 characters)&lt;/div&gt;
  &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;
    &lt;span id=&quot;char-count&quot;&gt;0&lt;/span&gt; / 200 characters
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
  (function() {
    const textarea = document.getElementById(&#x27;message&#x27;);
    const charCount = document.getElementById(&#x27;char-count&#x27;);
    
    textarea.addEventListener(&#x27;input&#x27;, function() {
      const count = this.value.length;
      charCount.textContent = count;
    });
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot; placeholder=&quot;Message&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;charCount&quot;&gt;0 / 200&lt;/div&gt;
&lt;script&gt;
document.getElementById(&#x27;message&#x27;).addEventListener(&#x27;input&#x27;, function() {
    var length = this.value.length;
    document.getElementById(&#x27;charCount&#x27;).textContent = length + &#x27; / 200&#x27;;
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; oninput=&quot;document.getElementById(&#x27;counter&#x27;).innerText = this.value.length + &#x27;/200&#x27;&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;Characters: &lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message here&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;span id=&quot;charCount&quot;&gt;0 / 200&lt;/span&gt;
&lt;/div&gt;
&lt;script&gt;
    const textarea = document.getElementById(&#x27;message&#x27;);
    const counter = document.getElementById(&#x27;charCount&#x27;);
    textarea.addEventListener(&#x27;input&#x27;, function() {
        const currentLength = this.value.length;
        counter.textContent = `${currentLength} / 200`;
    });
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; oninput=&quot;document.getElementById(&#x27;counter&#x27;).textContent = this.value.length + &#x27;/200&#x27;&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot;&gt;0/200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;counter&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot; aria-live=&quot;polite&quot;&gt;200 characters remaining&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;current-chars&quot;&gt;0&lt;/span&gt; / 200
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message-input&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message-input&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Message Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message-input&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message-input&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; aria-describedby=&quot;char-count&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;char-count&quot; aria-live=&quot;polite&quot;&gt;0 / 200 characters&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; required&gt;&lt;/textarea&gt;
    &lt;div&gt;
      &lt;small id=&quot;charCount&quot;&gt;200 characters remaining&lt;/small&gt;
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;charCount&#x27;);
      const max = textarea.maxLength &gt; 0 ? textarea.maxLength : 200;

      function updateCounter() {
        const remaining = max - textarea.value.length;
        counter.textContent = remaining + &#x27; characters remaining&#x27;;
      }

      textarea.addEventListener(&#x27;input&#x27;, updateCounter);
      updateCounter();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 2rem; line-height: 1.5; }
    form { max-width: 600px; }
    label { font-weight: 600; display: block; margin-bottom: .5rem; }
    textarea { width: 100%; box-sizing: border-box; padding: .625rem .75rem; border: 1px solid #c8c8c8; border-radius: .375rem; resize: vertical; min-height: 6rem; font: inherit; }
    textarea:focus { outline: none; border-color: #4c9ffe; box-shadow: 0 0 0 3px rgba(76,159,254,.25); }
    .counter { font-size: .875rem; margin-top: .375rem; color: #555; }
    .counter.over-limit { color: #b00020; }
    .actions { margin-top: .75rem; }
    button { appearance: none; border: 1px solid #1f6feb; background: #2f81f7; color: #fff; padding: .5rem .9rem; border-radius: .375rem; font: inherit; cursor: pointer; }
    button:disabled { opacity: .6; cursor</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message...&quot; aria-describedby=&quot;messageCounter&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;messageCounter&quot; aria-live=&quot;polite&quot;&gt;200 characters remaining&lt;/div&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;messageCounter&#x27;);
      const max = textarea.maxLength || 200;

      function updateCounter() {
        const remaining = max - textarea.value.length;
        counter.textContent = remaining + &#x27; characters remaining&#x27;;
      }

      textarea.addEventListener(&#x27;input&#x27;, updateCounter);
      updateCounter();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Accessible Message Field with Character Counter&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;div&gt;
      &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
      &lt;p id=&quot;message-hint&quot; class=&quot;hint&quot;&gt;Enter your message (up to 200 characters).&lt;/p&gt;
      &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; cols=&quot;40&quot; maxlength=&quot;200&quot; aria-describedby=&quot;message-hint message-counter&quot; aria-invalid=&quot;false&quot; required&gt;&lt;/textarea&gt;
      &lt;div id=&quot;message-counter&quot; role=&quot;status&quot; aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;0/200 characters&lt;/div&gt;
    &lt;/div&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;message-counter&#x27;);
      const max = textarea.getAttribute(&#x27;maxlength&#x27;) ? parseInt(textarea.getAttribute(&#x27;maxlength&#x27;), 10) : 200;

      function update() {
        const used = textarea.value.length;
        counter.textContent = used + &#x27;/&#x27; + max + &#x27; characters&#x27;;
        textarea.setAttribute(&#x27;aria-invalid&#x27;, used &gt; max ? &#x27;true&#x27; : &#x27;false&#x27;);
      }

      textarea.addEventListener(&#x27;input&#x27;, update);
      update();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;span id=&quot;charCounter&quot;&gt;0/200 characters&lt;/span&gt;
    &lt;/form&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const counter = document.getElementById(&#x27;charCounter&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            const currentLength = textarea.value.length;
            counter.textContent = currentLength + &#x27;/200 characters&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;span id=&quot;charCounter&quot;&gt;0/200 characters&lt;/span&gt;
    &lt;/form&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const counter = document.getElementById(&#x27;charCounter&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            const currentLength = this.value.length;
            counter.textContent = currentLength + &#x27;/200 characters&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
    &lt;div&gt;
        &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
    &lt;/div&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const charCount = document.getElementById(&#x27;charCount&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            charCount.textContent = this.value.length;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;char-count&quot;&gt;0/200&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;char-count&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;char-count&quot; role=&quot;status&quot; aria-live=&quot;polite&quot;&gt;0 / 200 characters&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot; oninput=&quot;document.getElementById(&#x27;counter&#x27;).textContent = this.value.length + &#x27;/200&#x27;&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Character count: &lt;span id=&quot;counter&quot;&gt;0&lt;/span&gt;/200&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message (max 200 characters)&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Character count: &lt;span id=&quot;counter&quot;&gt;0&lt;/span&gt;/200&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; oninput=&quot;document.getElementById(&#x27;counter&#x27;).textContent = this.value.length + &#x27;/200&#x27;&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message&quot;&gt;&lt;/textarea&gt;
&lt;p&gt;Characters: 0 / 200&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;counter&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot; aria-live=&quot;polite&quot;&gt;Characters: 0 / 200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
