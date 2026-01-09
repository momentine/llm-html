<details>
  <summary><strong>Text Field (Required)</strong></summary>
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
      <td>Insert a required text field for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Orange Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;orange-color&quot; name=&quot;orange_color&quot; type=&quot;text&quot; required /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-required/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field (required): What color is an orange?</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Color Question&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;get&quot;&gt;
    &lt;label for=&quot;color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;color&quot; name=&quot;color&quot; type=&quot;text&quot; required autocomplete=&quot;off&quot;&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-required/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required text field labeled “What color is an orange?”</td>
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
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;orange_color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input type=&quot;text&quot; id=&quot;orange_color&quot; name=&quot;orange_color&quot; required aria-describedby=&quot;orange_color_help&quot;&gt;
    &lt;small id=&quot;orange_color_help&quot;&gt;Please enter the color of</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-required/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required text field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Orange Color Question&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input id=&quot;orange-color&quot; name=&quot;orangeColor&quot; type=&quot;text&quot; required /&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-required/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field (required) for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;div&gt;
    &lt;label for=&quot;orange-color&quot;&gt;What color is an orange?&lt;/label&gt;
    &lt;input
      id=&quot;orange-color&quot;
      name=&quot;orange_color&quot;
      type=&quot;text&quot;
      required
      aria-required=&quot;true&quot;
      aria-describedby=&quot;orange-help orange-error&quot;
      autocomplete=&quot;off&quot;
      placeholder=&quot;e.g., orange&quot;
      pattern=&quot;^\s*[Oo][Rr][Aa][Nn][Gg][Ee]\s*$&quot;
    /&gt;
    &lt;div id=&quot;orange-help&quot;&gt;Enter the color of an orange (e.g., orange).&lt;/div&gt;
    &lt;div id=&quot;orange-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-required/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
