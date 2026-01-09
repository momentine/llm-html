<details>
  <summary><strong>Text Field with Accessible Description</strong></summary>
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
      <td>Insert a text field for “What is your favorite U.S. city?” with note “Please include the state name or abbreviation”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;favorite-city&quot;&gt;What is your favorite U.S. city?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;favorite-city&quot; name=&quot;favorite_city&quot; placeholder=&quot;e.g., Austin, TX&quot; aria-describedby=&quot;city-note&quot;&gt;
&lt;small id=&quot;city-note&quot;&gt;Please include the state name or abbreviation.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What is your favorite U.S. city? with note “Please include the state name or abbreviation”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;favorite-city&quot;&gt;What is your favorite U.S. city?&lt;/label&gt;
  &lt;input
    id=&quot;favorite-city&quot;
    name=&quot;favorite_city&quot;
    type=&quot;text&quot;
    inputmode=&quot;text&quot;
    autocomplete=&quot;address-level2&quot;
    placeholder=&quot;e.g., Austin, TX&quot;
    aria-describedby=&quot;city-note&quot;
  /&gt;
  &lt;small id=&quot;city-note&quot;&gt;Please include the state name or abbreviation.&lt;/small&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “What is your favorite U.S. city?” with note “Please include the state name or abbreviation”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Favorite U.S. City&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;favorite-city&quot;&gt;What is your favorite U.S. city?&lt;/label&gt;
    &lt;input id=&quot;favorite-city&quot; name=&quot;favorite_city&quot; type=&quot;text&quot; placeholder=&quot;e.g., Austin, TX&quot; autocomplete=&quot;address-level2&quot; /&gt;
    &lt;small&gt;Please include the state name or abbreviation.&lt;/small&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “What is your favorite U.S. city?” with note “Please include the state name or abbreviation”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;favorite-city&quot;&gt;What is your favorite U.S. city?&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;favorite-city&quot; name=&quot;favorite_city&quot; autocomplete=&quot;off&quot; /&gt;
&lt;small id=&quot;favorite-city-note&quot;&gt;Please include the state name or abbreviation&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “What is your favorite U.S. city?” with note “Please include the state name or abbreviation”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;label for=&quot;favorite-city&quot;&gt;What is your favorite U.S. city?&lt;/label&gt;
  &lt;input
    id=&quot;favorite-city&quot;
    name=&quot;favorite_city&quot;
    type=&quot;text&quot;
    required
    aria-describedby=&quot;city-help&quot;
    placeholder=&quot;e.g., Austin, TX&quot;
  /&gt;
  &lt;div id=&quot;city-help&quot;&gt;Please include the state name or abbreviation.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/text-field-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
