---
title: "textarea-with-character-counter"
slug: textarea-with-character-counter
track: persona
kind: component
order: 53
---

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
  &lt;div id=&quot;counter&quot;&gt;0 / 200 characters&lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
function updateCounter() {
  const textarea = document.getElementById(&#x27;message&#x27;);
  const counter = document.getElementById(&#x27;counter&#x27;);
  const currentLength = textarea.value.length;
  counter.textContent = currentLength + &#x27; / 200 characters&#x27;;
}
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt; / 200 characters
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
  const textarea = document.getElementById(&#x27;message&#x27;);
  const charCount = document.getElementById(&#x27;charCount&#x27;);
  
  textarea.addEventListener(&#x27;input&#x27;, function() {
    charCount.textContent = this.value.length;
  });
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;&lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; cols=&quot;50&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;&lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    aria-describedby=&quot;message-counter message-hint&quot;
    required
  &gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-hint&quot;&gt;Please enter your message (maximum 200 characters)&lt;/div&gt;
  &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;
    &lt;span id=&quot;character-count&quot;&gt;0&lt;/span&gt; / 200 characters
  &lt;/div&gt;
&lt;/div&gt;

&lt;script&gt;
  (function() {
    const textarea = document.getElementById(&#x27;message&#x27;);
    const characterCount = document.getElementById(&#x27;character-count&#x27;);
    
    textarea.addEventListener(&#x27;input&#x27;, function() {
      const count = this.value.length;
      characterCount.textContent = count;
    });
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;
&lt;script&gt;
const textarea = document.getElementById(&#x27;message&#x27;);
const counter = document.getElementById(&#x27;counter&#x27;);
textarea.addEventListener(&#x27;input&#x27;, function() {
  const length = textarea.value.length;
  counter.textContent = `${length}/200`;
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot;&gt;0/200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot;&gt;0/200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-label=&quot;Message&quot; placeholder=&quot;Type your message here&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot; aria-live=&quot;polite&quot;&gt;200 characters remaining&lt;/div&gt;

&lt;script&gt;
const textarea = document.getElementById(&#x27;message&#x27;);
const counter = document.getElementById(&#x27;counter&#x27;);

textarea.addEventListener(&#x27;input&#x27;, function() {
    const remaining = 200 - this.value.length;
    counter.textContent = `${remaining} characters remaining`;
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message-field&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message-field&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;8&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;char-count&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;char-count&quot; role=&quot;status&quot; aria-live=&quot;polite&quot;&gt;0 / 200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;8&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;char-</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
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
      <td><a href="docs/persona-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; maxlength=&quot;200&quot; aria-describedby=&quot;messageCounter&quot; placeholder=&quot;Enter your message...&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;messageCounter&quot; aria-live=&quot;polite&quot;&gt;0/200&lt;/div&gt;

&lt;script&gt;
  (function() {
    const textarea = document.getElementById(&#x27;message&#x27;);
    const counter = document.getElementById(&#x27;messageCounter&#x27;);
    const MAX = 200;

    function updateCount() {
      const len = textarea.value.length;
      counter.textContent = len + &#x27;/&#x27; + MAX;
      if (len &gt; MAX) {
        textarea.value = textarea.value.slice(0, MAX);
        counter.textContent = MAX + &#x27;/&#x27; + MAX;
      }
    }

    textarea.addEventListener(&#x27;input&#x27;, updateCount);
    updateCount();
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
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
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; aria-describedby=&quot;message-counter&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot;&gt;0/200&lt;/div&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;message-counter&#x27;);
      const max = parseInt(textarea.getAttribute(&#x27;maxlength&#x27;), 10) || 200;

      function updateCounter() {
        const length = textarea.value.length;
        counter.textContent = length + &#x27;/&#x27; + max;
        counter.style.color = length &gt; max ? &#x27;#b00020&#x27; : &#x27;&#x27;;
      }

      textarea.addEventListener(&#x27;input&#x27;, updateCounter);
      textarea.addEventListener(&#x27;propertychange&#x27;, updateCounter);
      updateCounter();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
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
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 2rem;
      display: grid;
      place-items: start center;
      background: Canvas;
      color: CanvasText;
    }
    .field { width: min(600px, 90vw); }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    textarea {
      width: 100%;
      box-sizing: border-box;
      min-height: 8rem;
      padding: 0.75rem;
      font: inherit;
      line-height: 1.4;
      border: 1px solid color-mix(in oklab, CanvasText 25%, transparent);
      border-radius: 0.5rem;
      background: Canvas;
      color: CanvasText;
      resize: vertical;
    }
    .meta {
      margin-top: 0.5rem;
      font-size: 0.9rem;
      display: flex;
      justify-content: flex-end;
      gap: 0.5rem;
      align-items: center;
    }
    .counter { opacity: 0.8; }
    .counter.near-limit { color: #b45309; } /* amber-700 */
    .counter.at-limit { color: #b91c1c; }   /* red-700 */
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class=&quot;field&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea
      id=&quot;message&quot;
      name=&quot;message&quot;
      rows=&quot;6&quot;
      maxlength=&quot;200&quot;
      aria-describedby=&quot;messageCounter&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea
      id=&quot;message&quot;
      name=&quot;message&quot;
      rows=&quot;5&quot;
      maxlength=&quot;200&quot;
      aria-describedby=&quot;message-counter&quot;
      required
    &gt;&lt;/textarea&gt;
    &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot; role=&quot;status&quot;&gt;0/200&lt;/div&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;message-counter&#x27;);
      const max = textarea.maxLength || 200;

      function update() {
        const len = textarea.value.length;
        counter.textContent = len + &#x27;/&#x27; + max;
      }

      textarea.addEventListener(&#x27;input&#x27;, update);
      textarea.addEventListener(&#x27;keyup&#x27;, update);
      update();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Message Textarea with Character Counter&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.5; margin: 2rem; }
    .field { max-width: 40rem; }
    label { display: block; font-weight: 600; margin-bottom: 0.25rem; }
    .hint { color: #555; font-size: 0.95rem; margin-bottom: 0.5rem; }
    textarea { width: 100%; min-height: 8rem; padding: 0.75rem; font: inherit; border: 1px solid #888; border-radius: 0.375rem; resize: vertical; }
    textarea:focus { outline: 3px solid transparent; box-shadow: 0 0 0 3px rgba(0, 115, 230, 0.35); border-color: #0b6bcb; }
    .meta { display: flex; align-items: baseline; justify-content: space-between; margin-top: 0.25rem; }
    .counter { font-variant-numeric: tabular-nums; }
    .error { color: #b00020; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border:</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/minimax-minimax-m2/g5.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;0 / 200 characters&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; aria-describedby=&quot;message-counter&quot; required&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-counter&quot; role=&quot;status&quot; aria-live=&quot;polite&quot;&gt;0 / 200 characters used&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;charCounter&quot;&gt;0/200&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;
    &lt;span id=&quot;char-count&quot;&gt;0&lt;/span&gt;/200 characters
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
  &lt;div id=&quot;char-count&quot;&gt;0 / 200&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
    aria-describedby=&quot;message-count&quot;
    rows=&quot;4&quot;
    cols=&quot;50&quot;
  &gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-count&quot; aria-live=&quot;polite&quot;&gt;
    &lt;span id=&quot;current-count&quot;&gt;0&lt;/span&gt;/200 characters
  &lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;counter&quot;&gt;200 characters remaining&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot; placeholder=&quot;Enter your message (max 200 characters)&quot;&gt;&lt;/textarea&gt;
  &lt;div&gt;Character count: &lt;span&gt;0&lt;/span&gt;/200&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
&lt;p&gt;Character count: &lt;span id=&quot;counter&quot;&gt;0&lt;/span&gt;/200&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;counter&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot; aria-live=&quot;polite&quot;&gt;0 / 200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

