<details>
  <summary><strong>Readonly Field</strong></summary>
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
      <td>Insert a read-only field for “User ID”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;userId&quot;&gt;User ID&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;userId&quot; name=&quot;userId&quot; value=&quot;12345&quot; readonly&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/readonly-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Read-only field: User ID</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Read-only User ID Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/submit&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;userId&quot;&gt;User ID&lt;/label&gt;
    &lt;input
      id=&quot;userId&quot;
      name=&quot;userId&quot;
      type=&quot;text&quot;
      value=&quot;USR-123456&quot;
      readonly
      aria-readonly=&quot;true&quot;
    /&gt;
    &lt;!-- Hidden field to ensure the read-only value is submitted with the form --&gt;
    &lt;input type=&quot;hidden&quot; name=&quot;userId&quot; value=&quot;USR-123456&quot; /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/readonly-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A read-only field labeled “User ID”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Read-only User ID Field&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; }
    .field { margin-bottom: 1rem; }
    label { display: block; margin-bottom: 0.35rem; font-weight: 600; }
    input[readonly] {
      width: 320px;
      padding: 0.5rem 0.6rem;
      font-size: 1rem;
      border: 1px solid #c8c8c8;
      border-radius: 4px;
      background: #f6f6f6;
      color: #333;
      outline: none;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;userId&quot;&gt;User ID&lt;/label&gt;
      &lt;input
        id=&quot;userId&quot;
        name=&quot;userId&quot;
        type=&quot;text&quot;
        value=&quot;12345&quot;
        readonly
        aria-readonly=&quot;true&quot;
        aria-describedby=&quot;userIdHelp&quot;
      /&gt;
      &lt;div id=&quot;userIdHelp&quot; style=&quot;font-size: 0.9rem; color: #666; margin-top: 0.35rem;&quot;&gt;
        This field is read-only.
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/readonly-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a read-only field and label for “User ID”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;user-id&quot;&gt;User ID&lt;/label&gt;
&lt;input id=&quot;user-id&quot; type=&quot;text&quot; value=&quot;12345&quot; readonly aria-readonly=&quot;true&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/readonly-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible read-only field for “User ID”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;userId&quot;&gt;User ID&lt;/label&gt;
&lt;input
  id=&quot;userId&quot;
  name=&quot;userId&quot;
  type=&quot;text&quot;
  value=&quot;12345&quot;
  readonly
  aria-readonly=&quot;true&quot;
  aria-describedby=&quot;userId-hint&quot;
  size=&quot;20&quot;
/&gt;
&lt;div id=&quot;userId-hint&quot;&gt;Read-only. Cannot be edited.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/readonly-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
