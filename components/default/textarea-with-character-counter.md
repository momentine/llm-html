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
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Message Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
        &lt;div&gt;
            &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Message Textarea with Character Counter&lt;/title&gt;
    &lt;style&gt;
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, &#x27;Segoe UI&#x27;, Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 40px;
            width: 100%;
            max-width: 500px;
        }
        h1 {
            color: #333;
            margin-bottom: 24px;
            font-size: 24px;
        }
        .form-group {
            position: relative;
        }
        label {
            display: block;
            color: #555;
            font-weight: 600;
            margin-bottom: 8px;
            font-size: 14px;
        }
        textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-family: inherit;
            font-size: 15px;
            resize: vertical;
            min-height: 120px;
            transition: border-color 0.3s ease;
            outline: none;
        }
        textarea:focus {
            border-color: #667eea;
        }
        textarea.error {
            border-color: #e74c3c;
        }
        .counter {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 8px;
            font-size: 13px;
        }
        .counter-text {
            color: #666;
        }
        .counter-text.warning {
            color: #f39c12;
            font-weight: 600;
        }
        .counter-text.error {
            color: #e74c3c;
            font-weight: 600;
        }
        .helper-text {
            color: #999;
            font-size: 12px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class=&quot;container&quot;&gt;
        &lt;h1&gt;Send a Message&lt;/h1&gt;
        &lt;div class=&quot;form-group&quot;&gt;
            &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
            &lt;textarea id=&quot;message&quot; placeholder=&quot;Type your message here...&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
            &lt;div class=&quot;counter&quot;&gt;
                &lt;span class=&quot;helper-text&quot;&gt;Maximum 200 characters&lt;/span&gt;
                &lt;span class=&quot;counter-text&quot;&gt;&lt;span id=&quot;current&quot;&gt;0&lt;/span&gt; / 200&lt;/span&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const currentCount = document.getElementById(&#x27;current&#x27;);
        const counterText = document.querySelector(&#x27;.counter-text&#x27;);

        textarea.addEventListener(&#x27;input&#x27;, function() {
            const length = this.value.length;
            currentCount.textContent = length;

            counterText.classList.remove(&#x27;warning&#x27;, &#x27;error&#x27;);
            textarea.classList.remove(&#x27;error&#x27;);

            if (length &gt;= 200) {
                counterText.classList.add(&#x27;error&#x27;);
                textarea.classList.add(&#x27;error&#x27;);
            } else if (length &gt;= 180) {
                counterText.classList.add(&#x27;warning&#x27;);</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Message Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; cols=&quot;50&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
        &lt;div&gt;
            &lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Message Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; cols=&quot;50&quot; oninput=&quot;document.getElementById(&#x27;charCount&#x27;).textContent = this.value.length&quot;&gt;&lt;/textarea&gt;
        &lt;div&gt;&lt;span id=&quot;charCount&quot;&gt;0&lt;/span&gt;/200 characters&lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Message Textarea with Character Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
        &lt;textarea 
            id=&quot;message&quot; 
            name=&quot;message&quot; 
            maxlength=&quot;200&quot; 
            rows=&quot;5&quot; 
            aria-describedby=&quot;char-count&quot;
            oninput=&quot;document.getElementById(&#x27;current-count&#x27;).textContent = this.value.length&quot;
        &gt;&lt;/textarea&gt;
        &lt;div id=&quot;char-count&quot; aria-live=&quot;polite&quot;&gt;
            &lt;span id=&quot;current-count&quot;&gt;0&lt;/span&gt; / 200 characters
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; placeholder=&quot;Message&quot; oninput=&quot;document.getElementById(&#x27;counter&#x27;).textContent = this.value.length + &#x27;/200&#x27;&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;Characters: &lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot; placeholder=&quot;Type your message here...&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot;&gt;0/200 characters&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; placeholder=&quot;Message&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;counter&quot;&gt;0 / 200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
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
&lt;div id=&quot;char-counter&quot;&gt;0/200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
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
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; aria-describedby=&quot;message-counter&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot;&gt;0/200 characters&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
    &lt;title&gt;Textarea with Character Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;br&gt;
    &lt;textarea id=&quot;message&quot; name</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
    &lt;title&gt;Textarea Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
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
    &lt;title&gt;Textarea Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
    &lt;title&gt;Textarea Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
  &lt;title&gt;Accessible Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; aria-describedby=&quot;char-count&quot;&gt;&lt;/textarea&gt;
    &lt;div id=&quot;char-count&quot; aria-live=&quot;polite&quot;&gt;0 / 200 characters&lt;/div&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;contact-form&quot; action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
  &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; maxlength=&quot;200&quot; required aria-describedby=&quot;message-counter&quot;&gt;&lt;/textarea&gt;
  &lt;div id=&quot;message-counter&quot; aria-live=&quot;polite&quot;&gt;0/200 characters&lt;/div&gt;

  &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;message-counter&#x27;);
      const max = textarea.maxLength || 200;

      function updateCounter() {
        const used = textarea.value.length;
        counter.textContent = used + &#x27;/&#x27; + max + &#x27; characters&#x27;;
      }

      textarea.addEventListener(&#x27;input&#x27;, updateCounter);
      updateCounter();
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;style&gt;
    :root {
      --fg: #222;
      --muted: #6b7280;
      --danger: #b00020;
      --bg: #fff;
      --border: #d1d5db;
      --focus: #2563eb;
    }
    body {
      margin: 0;
      padding: 2rem;
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, &quot;Apple Color Emoji&quot;, &quot;Segoe UI Emoji&quot;;
      color: var(--fg);
      background: var(--bg);
    }
    .field {
      max-width: 640</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    .field { max-width: 600px; }
    label { display: block; font-weight: 600; margin-bottom: .5rem; }
    textarea { width: 100%; min-height: 120px; padding: .625rem .75rem; resize: vertical; }
    .counter { margin-top: .375rem; font-size: .9rem; color: #555; }
    .counter.over { color: #b00020; font-weight: 600; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class=&quot;field&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;5&quot; aria-describedby=&quot;messageCounter&quot; placeholder=&quot;Type your message...&quot;&gt;&lt;/textarea&gt;
    &lt;div id=&quot;messageCounter&quot; class=&quot;counter&quot; aria-live=&quot;polite&quot;&gt;0 / 200&lt;/div&gt;
  &lt;/div&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;messageCounter&#x27;);
      const max = textarea.maxLength || 200;

      function update() {
        const length = textarea.value.length;
        counter.textContent = length + &#x27; / &#x27; + max;
        counter.classList.toggle(&#x27;over&#x27;, length &gt; max);
      }

      textarea.addEventListener(&#x27;input&#x27;, update);
      update();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message with Character Counter&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    .field { max-width: 600px; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    textarea { width: 100%; min-height: 120px; padding: 0.625rem; border: 1px solid #c7c7c7; border-radius: 6px; font: inherit; resize: vertical; }
    textarea:focus { outline: 2px solid #4c9ffe; outline-offset: 2px; border-color: #4c9ffe; }
    .counter { margin-top: 0.5rem; font-size: 0.9rem; color: #555; display: flex; justify-content: flex-end; }
    .counter[data-overlimit=&quot;true&quot;] { color: #b00020; font-weight: 600; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form class=&quot;field&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; maxlength=&quot;200&quot; aria-describedby=&quot;messageCounter&quot; placeholder=&quot;Type your message...&quot;&gt;&lt;/textarea&gt;
    &lt;div id=&quot;messageCounter&quot; class=&quot;counter&quot; aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;0 / 200&lt;/div&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;messageCounter&#x27;);
      const max = textarea.maxLength || 200;

      function updateCounter() {
        const used = textarea.value.length;
        counter.textContent = used + &#x27; / &#x27; + max;
        counter.dataset.overlimit = used &gt; max ? &#x27;true&#x27; : &#x27;false&#x27;;
      }

      function enforceLimit() {
        if (textarea.value.length &gt; max) {
          textarea.value = textarea.value.slice(0, max);
        }
        updateCounter();
      }

      textarea.addEventListener</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot;&gt;&lt;/textarea&gt;
&lt;div&gt;0/200&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; aria-describedby=&quot;message-helper message-counter&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;message-helper&quot;&gt;You can enter up to 200 characters.&lt;/div&gt;
&lt;div id=&quot;message-counter&quot; role=&quot;status&quot; aria-live=&quot;polite&quot;&gt;Characters used: 0/200&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
        &lt;span id=&quot;charCount&quot;&gt;0/200 characters&lt;/span&gt;
    &lt;/form&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const charCount = document.getElementById(&#x27;charCount&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            const currentLength = textarea.value.length;
            charCount.textContent = currentLength + &#x27;/200 characters&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
        &lt;span id=&quot;charCount&quot;&gt;0/200 characters&lt;/span&gt;
    &lt;/form&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const charCount = document.getElementById(&#x27;charCount&#x27;);

        textarea.addEventListener(&#x27;input&#x27;, function() {
            const currentLength = textarea.value.length;
            charCount.textContent = currentLength + &#x27;/200 characters&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
    &lt;div id=&quot;charCounter&quot;&gt;0 / 200&lt;/div&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const counter = document.getElementById(&#x27;charCounter&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            const currentLength = textarea.value.length;
            counter.textContent = currentLength + &#x27; / 200&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with a character counter (max 200 characters)</td>
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
    &lt;div id=&quot;charCount&quot;&gt;0 / 200&lt;/div&gt;

    &lt;script&gt;
        const textarea = document.getElementById(&#x27;message&#x27;);
        const charCount = document.getElementById(&#x27;charCount&#x27;);
        
        textarea.addEventListener(&#x27;input&#x27;, function() {
            charCount.textContent = this.value.length + &#x27; / 200&#x27;;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
  &lt;div id=&quot;char-count&quot; aria-live=&quot;polite&quot;&gt;0 / 200 characters&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; maxlength=&quot;200&quot; rows=&quot;4&quot; cols=&quot;50&quot;&gt;&lt;/textarea&gt;
&lt;span id=&quot;counter&quot;&gt;0 / 200 characters&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;title&gt;Message Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;message&quot;&gt;Message:&lt;/label&gt;&lt;br&gt;
        &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot; maxlength=&quot;200&quot; placeholder=&quot;Enter your message&quot;&gt;&lt;/textarea&gt;&lt;br&gt;
        &lt;span&gt;Characters: 0/200&lt;/span&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
&lt;p&gt;Characters: &lt;span id=&quot;count&quot;&gt;0&lt;/span&gt;/200&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
&lt;span id=&quot;counter&quot;&gt;0/200&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with a character counter (max 200 characters)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;4&quot; cols=&quot;50&quot; maxlength=&quot;200&quot; aria-describedby=&quot;char-counter&quot;&gt;&lt;/textarea&gt;
&lt;div id=&quot;char-counter&quot;&gt;0/200 characters&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/textarea-with-character-counter/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
