<details>
  <summary><strong>Checkbox Group with Accessible Description</strong></summary>
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
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;&lt;br&gt;
    &lt;small&gt;You can change this later&lt;/small&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Checkbox Group - Fruits&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.5; margin: 2rem; }
    fieldset { border: 1px solid #ccc; padding: 1rem; border-radius: 8px; max-width: 480px; }
    legend { font-weight: 600; padding: 0 .5rem; }
    .options { display: grid; gap: .5rem; margin-top: .5rem; }
    label { cursor: pointer; }
    .note { color: #555; font-size: .9rem; margin-top: .25rem; }
    .actions { margin-top: 1rem; }
    button { padding: .5rem .75rem; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;

      &lt;div class=&quot;options&quot;&gt;
        &lt;div&gt;
          &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot; /&gt;
          &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
        &lt;/div&gt;

        &lt;div&gt;
          &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot; /&gt;
          &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
        &lt;/div&gt;

        &lt;div&gt;
          &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot; /&gt;
          &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
  &lt;title&gt;Fruit Checkbox Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
        Bananas
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
        Oranges
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
        Apples
      &lt;/label&gt;
    &lt;/fieldset&gt;
    &lt;p&gt;&lt;small&gt;You can change this later.&lt;/small&gt;&lt;/p&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;body&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;p id=&quot;fruit-note&quot; class=&quot;note&quot;&gt;You can change this later&lt;/p&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; aria-describedby=&quot;fruit-note&quot;&gt;
      &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
    &lt;/div&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; aria-describedby=&quot;fruit-note&quot;&gt;
      &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
    &lt;/div&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot; aria-describedby=&quot;fruit-note&quot;&gt;
      &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;p id=&quot;fruit-note&quot;&gt;You can change this later.&lt;/p&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      &lt;label for=&quot;fruit-bananas&quot;&gt;Bananas&lt;/label&gt;
    &lt;/div&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;fruit-oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      &lt;label for=&quot;fruit-oranges&quot;&gt;Oranges&lt;/label&gt;
    &lt;/div&gt;

    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;fruit-apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      &lt;label for=&quot;fruit-apples&quot;&gt;Apples&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/checkbox-group-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
