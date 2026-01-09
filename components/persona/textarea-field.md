<details>
  <summary><strong>Textarea Field</strong></summary>
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
      <td>Insert a textarea field for “Message”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Message Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; placeholder=&quot;Type your message here&quot; required&gt;&lt;/textarea&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message Textarea&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea
      id=&quot;message&quot;
      name=&quot;message&quot;
      rows=&quot;5&quot;
      cols=&quot;40&quot;
      placeholder=&quot;Type your message&quot;
      required
      maxlength=&quot;1000&quot;
      spellcheck=&quot;true&quot;
      aria-label=&quot;Message&quot;
    &gt;&lt;/textarea&gt;
    &lt;div&gt;
      &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
    &lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message Textarea&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    textarea { width: 100%; box-sizing: border-box; min-height: 8rem; padding: 0.75rem; border: 1px solid #cfd8dc; border-radius: 6px; resize: vertical; }
    textarea:focus { outline: 2px solid #4c9ffe; outline-offset: 2px; border-color: #4c9ffe; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; placeholder=&quot;Type your message...&quot;&gt;&lt;/textarea&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; placeholder=&quot;Enter your message&quot;&gt;&lt;/textarea&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Accessible Message Textarea&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;main&gt;
    &lt;form action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
      &lt;fieldset&gt;
        &lt;legend&gt;Send us a message&lt;/legend&gt;

        &lt;label for=&quot;message&quot;&gt;Message &lt;span aria-hidden=&quot;true&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
        &lt;div id=&quot;messageHelp&quot; class=&quot;help&quot;&gt;Do not include sensitive information.&lt;/div&gt;

        &lt;textarea
          id=&quot;message&quot;
          name=&quot;message&quot;
          rows=&quot;6&quot;
          required
          aria-required=&quot;true&quot;
          aria-describedby=&quot;messageHelp messageCount&quot;
          maxlength=&quot;500&quot;
          placeholder=&quot;Type your message here&quot;&gt;&lt;/textarea&gt;

        &lt;div id=&quot;messageCount&quot; class=&quot;counter&quot; aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;500 characters remaining&lt;/div&gt;

        &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
      &lt;/fieldset&gt;
    &lt;/form&gt;
  &lt;/main&gt;

  &lt;script&gt;
    (function () {
      const textarea = document.getElementById(&#x27;message&#x27;);
      const counter = document.getElementById(&#x27;messageCount&#x27;);
      const max = textarea.maxLength &gt; 0 ? textarea.maxLength : 500;

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
      <td><a href="docs/persona-outputs/textarea-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
