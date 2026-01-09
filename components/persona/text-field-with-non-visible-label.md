<details>
  <summary><strong>Text Field with Non-visible Label</strong></summary>
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
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; class=&quot;sr-only&quot;&gt;Search for&lt;/label&gt;
&lt;input id=&quot;search&quot; name=&quot;search&quot; type=&quot;text&quot; placeholder=&quot;Search for...&quot; /&gt;
&lt;style&gt;
  .sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; class=&quot;sr-only&quot;&gt;Search for&lt;/label&gt;
&lt;input id=&quot;search&quot; type=&quot;search&quot; placeholder=&quot;Search&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Search with Hidden Label&lt;/title&gt;
  &lt;style&gt;
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form role=&quot;search&quot; action=&quot;/search&quot; method=&quot;get&quot;&gt;
    &lt;label class=&quot;sr-only&quot; for=&quot;search-field&quot;&gt;Search for&lt;/label&gt;
    &lt;input
      type=&quot;search&quot;
      id=&quot;search-field&quot;
      name=&quot;q&quot;
      placeholder=&quot;Search…&quot;
      aria-label=&quot;Search for&quot;
    /&gt;
    &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label class=&quot;sr-only&quot; for=&quot;search-for&quot;&gt;Search for&lt;/label&gt;
&lt;input id=&quot;search-for&quot; type=&quot;search&quot; placeholder=&quot;Search for...&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Search Field&lt;/title&gt;
  &lt;style&gt;
    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form role=&quot;search&quot; action=&quot;/search&quot; method=&quot;get&quot;&gt;
    &lt;label class=&quot;sr-only&quot; for=&quot;search&quot;&gt;Search for&lt;/label&gt;
    &lt;input
      id=&quot;search&quot;
      name=&quot;q&quot;
      type=&quot;search&quot;
      placeholder=&quot;Search for...&quot;
      required
      aria-describedby=&quot;search-help&quot;
    /&gt;
    &lt;span id=&quot;search-help&quot; class=&quot;sr-only&quot;&gt;Enter the term you want to find.&lt;/span&gt;
    &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
