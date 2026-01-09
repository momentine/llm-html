<details>
  <summary><strong>Checkbox Group</strong></summary>
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
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label for=&quot;fruit-bananas&quot;&gt;
      &lt;input id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; type=&quot;checkbox&quot; value=&quot;bananas&quot;&gt; Bananas
    &lt;/label&gt;
    &lt;label for=&quot;fruit-oranges&quot;&gt;
      &lt;input id=&quot;fruit-oranges&quot; name=&quot;fruits&quot; type=&quot;checkbox&quot; value=&quot;oranges&quot;&gt; Oranges
    &lt;/label&gt;
    &lt;label for=&quot;fruit-apples&quot;&gt;
      &lt;input id=&quot;fruit-apples&quot; name=&quot;fruits&quot; type=&quot;checkbox&quot; value=&quot;apples&quot;&gt; Apples
    &lt;/label&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Checkbox Group: What fruits do you like?&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
        bananas
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
        oranges
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
        apples
      &lt;/label&gt;
    &lt;/fieldset&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; id=&quot;bananas&quot;&gt;
    bananas
  &lt;/label&gt;&lt;br&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; id=&quot;oranges&quot;&gt;
    oranges
  &lt;/label&gt;&lt;br&gt;
  &lt;label&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot; id=&quot;apples&quot;&gt;
    apples
  &lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Fruit Preferences&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;label for=&quot;bananas&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
        Bananas
      &lt;/label&gt;
      &lt;label for=&quot;oranges&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
        Oranges
      &lt;/label&gt;
      &lt;label for=&quot;apples&quot;&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
        Apples
      &lt;/label&gt;
    &lt;/fieldset&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Fruits Checkbox Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot; /&gt;
        &lt;label for=&quot;fruit-bananas&quot;&gt;Bananas&lt;/label&gt;
      &lt;/div&gt;
      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-oranges&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot; /&gt;
        &lt;label for=&quot;fruit-oranges&quot;&gt;Oranges&lt;/label&gt;
      &lt;/div&gt;
      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;fruit-apples&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot; /&gt;
        &lt;label for=&quot;fruit-apples&quot;&gt;Apples&lt;/label&gt;
      &lt;/div&gt;
    &lt;/fieldset&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
