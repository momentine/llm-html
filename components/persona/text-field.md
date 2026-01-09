<details>
  <summary><strong>Text Field</strong></summary>
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
      <td>Insert a text field for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Orange Color Question&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;orange-color&quot; name=&quot;orangeColor&quot; placeholder=&quot;Your answer&quot;&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;What color is an orange?&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.5; margin: 2rem; }
    label { display: block; font-weight: 600; margin-bottom: .5rem; }
    input[type=&quot;text&quot;] { width: 100%; max-width: 24rem; padding: .6rem .75rem; font-size: 1rem; border: 1px solid #c7c7c7; border-radius: .375rem; }
    input[type=&quot;text&quot;]:focus { outline: 2px solid #4c9ffe; outline-offset: 2px; border-color: #4c9ffe; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form method=&quot;post&quot; action=&quot;&quot;&gt;
    &lt;label for=&quot;answer&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;answer&quot; name=&quot;answer&quot; type=&quot;text&quot; placeholder=&quot;Type your answer&quot; autocomplete=&quot;off&quot; autofocus /&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;color-answer&quot;&gt;What color is an orange?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;color-answer&quot; name=&quot;color_answer&quot; placeholder=&quot;e.g., orange&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;What color is an orange?&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
  &lt;input id=&quot;orange-color&quot; name=&quot;orange-color&quot; type=&quot;text&quot; placeholder=&quot;Type your answer...&quot; /&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Text Field: What color is an orange?&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.5; margin: 2rem; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    input[type=&quot;text&quot;] { padding: 0.6rem 0.75rem; font-size: 1rem; border: 1px solid #6b7280; border-radius: 0.375rem; width: 100%; max-width: 24rem; }
    input[type=&quot;text&quot;]:focus { outline: 3px solid #1d4ed8; outline-offset: 2px; }
    .hint { color: #374151; margin-top: 0.25rem; }
    .sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border: 0; }
    button { margin-top: 0.75rem; padding: 0.6rem 1rem; font-size: 1rem; border: 1px solid #1f2937; background: #111827; color: #fff; border-radius: 0.375rem; cursor: pointer; }
    button:focus { outline: 3px solid #1d4ed8; outline-offset: 2px; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input
      id=&quot;orange-color&quot;
      name=&quot;orange_color&quot;
      type=&quot;text&quot;
      inputmode=&quot;text&quot;
      autocomplete=&quot;off&quot;
      autocapitalize=&quot;none&quot;
      spellcheck=&quot;false&quot;
      aria-describedby=&quot;orange-color-hint&quot;
      aria-label=&quot;What color is an orange?&quot;
      placeholder=&quot;e.g., orange&quot;
      required
    /&gt;
    &lt;div id=&quot;orange-color-hint&quot; class=&quot;hint&quot;&gt;Enter the color name (for example: orange).&lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
