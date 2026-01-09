<details>
  <summary><strong>Text Field with Autocomplete Suggestion</strong></summary>
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
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;first_name&quot; list=&quot;firstNameSuggestions&quot; autocomplete=&quot;given-name&quot;&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;First Name with Autocomplete Suggestion&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;firstName&quot;&gt;First name&lt;/label&gt;
  &lt;input id=&quot;firstName&quot; name=&quot;first_name&quot; type=&quot;text&quot; autocomplete=&quot;given-name&quot; list=&quot;firstNameSuggestions&quot; placeholder=&quot;e.g., John Doe&quot;&gt;
  &lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
    &lt;option value=&quot;John Doe&quot;&gt;
  &lt;/datalist&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input id=&quot;firstName&quot; name=&quot;first_name&quot; type=&quot;text&quot; list=&quot;nameSuggestions&quot; autocomplete=&quot;off&quot; placeholder=&quot;e.g., John Doe&quot;&gt;
&lt;datalist id=&quot;nameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;First Name Input&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
  &lt;input id=&quot;firstName&quot; name=&quot;firstName&quot; type=&quot;text&quot; list=&quot;firstNameSuggestions&quot;&gt;
  &lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
    &lt;option value=&quot;John Doe&quot;&gt;
  &lt;/datalist&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;First Name Field&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;first-name&quot;&gt;Your first name&lt;/label&gt;
    &lt;input
      id=&quot;first-name&quot;
      name=&quot;first_name&quot;
      type=&quot;text&quot;
      autocomplete=&quot;given-name&quot;
      list=&quot;first-name-suggestions&quot;
      spellcheck=&quot;false&quot;
      inputmode=&quot;text&quot;
      aria-describedby=&quot;first-name-help&quot;
      required
    &gt;
    &lt;datalist id=&quot;first-name-suggestions&quot;&gt;
      &lt;option value=&quot;John Doe&quot;&gt;
      &lt;option value=&quot;John&quot;&gt;
      &lt;option value=&quot;Jane&quot;&gt;
      &lt;option value=&quot;Alex&quot;&gt;
    &lt;/datalist&gt;
    &lt;div id=&quot;first-name-help&quot;&gt;Start typing to see suggestions. Press the down arrow to select.&lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
