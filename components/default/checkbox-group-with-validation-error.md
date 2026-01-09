<details>
  <summary><strong>Checkbox Group with Validation Error</strong></summary>
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
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      Bananas
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      Oranges
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      Apples
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div role=&quot;alert&quot;&gt;
    &lt;span&gt;You must choose one or more fruits&lt;/span&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Fruit Selection&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
            &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
            &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
            &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
        &lt;/div&gt;
        &lt;div role=&quot;alert&quot;&gt;You must choose one or more fruits&lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div role=&quot;group&quot; aria-describedby=&quot;fruits-error&quot;&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;div id=&quot;fruits-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Fruit Selection&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
            &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
            &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
            &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;span role=&quot;alert&quot;&gt;You must choose one or more fruits&lt;/span&gt;
        &lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Fruit Preferences&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;
        &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
        &lt;div role=&quot;group&quot; aria-describedby=&quot;fruits-error&quot;&gt;
            &lt;div&gt;
                &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
                &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
            &lt;/div&gt;
            &lt;div&gt;
                &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
                &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
            &lt;/div&gt;
            &lt;div&gt;
                &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
                &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        &lt;div id=&quot;fruits-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;You must choose one or more fruits&lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;small style=&quot;display: none; color: red;&quot; id=&quot;fruit-error&quot;&gt;You must choose one or more fruits&lt;/small&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;div id=&quot;error-message&quot; style=&quot;color: red; display: none;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
        &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
        &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
        &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
    &lt;/div&gt;
    &lt;p style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;div style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;div role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Checkbox Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;fruits-error&quot;&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Checkbox Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Accessible Checkbox Group&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;fieldset aria-</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Fruit Checkbox Group&lt;/title&gt;
  &lt;style&gt;
    .error {
      color: #b00020;
      margin-top: 6px;
      display: block;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;fruitForm&quot; novalidate&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;

      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; /&gt;
        bananas
      &lt;/label&gt;
      &lt;br /&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; /&gt;
        oranges
      &lt;/label&gt;
      &lt;br /&gt;
      &lt;label&gt;
        &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot; /&gt;
        apples
      &lt;/label&gt;

      &lt;span id=&quot;fruitError&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/span&gt;
      &lt;br /&gt;
      &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;/fieldset&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;fruitForm&#x27;);
      const errorEl = document.getElementById(&#x27;fruitError&#x27;);

      function validateFruits() {
        const checked = form.querySelectorAll(&#x27;input[name=&quot;fruits&quot;]:checked&#x27;);
        if (checked.length === 0) {
          errorEl.textContent = &#x27;You must choose one or more fruits&#x27;;
          return false;
        }
        errorEl.textContent = &#x27;&#x27;;
        return true;
      }

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validateFruits()) {
          e.preventDefault();
        }
      });

      form.querySelectorAll(&#x27;input[name=&quot;fruits&quot;]&#x27;).forEach(function (cb) {
        cb.addEventListener(&#x27;change&#x27;, function () {
          if (cb.checked) {
            errorEl.textContent = &#x27;&#x27;;
          }
        });
      });
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Checkbox Group: Fruits&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;fruit-form&quot; novalidate&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;

      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; /&gt;
        &lt;label for=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
      &lt;/div&gt;
      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; /&gt;
        &lt;label for=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
      &lt;/div&gt;
      &lt;div&gt;
        &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot; /&gt;
        &lt;label for=&quot;apples&quot;&gt;apples&lt;/label&gt;
      &lt;/div&gt;

      &lt;p id=&quot;fruits-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; style=&quot;color: #b00020; margin-top: 8px; display: none;&quot;&gt;
        You must choose one or more fruits
      &lt;/p&gt;
    &lt;/fieldset&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Fruit Checkbox Group&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; padding: 2rem; }
    fieldset { border: 1px solid #ccc; padding: 1rem; max-width: 420px; }
    legend { font-weight: 600; }
    .options { display: grid; gap: .5rem; margin: .5rem 0 0; }
    .error { color: #b00020; margin-top: .5rem; }
    .hidden { display: none; }
    .invalid { border-color: #b00020; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;fruit-form&quot; novalidate&gt;
    &lt;fieldset id=&quot;fruit-fieldset&quot;&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;div class=&quot;options&quot;&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;
      &lt;/div&gt;
      &lt;p id=&quot;fruit-error&quot; class=&quot;error hidden&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;You must choose one or more fruits&lt;/p&gt;
    &lt;/fieldset&gt;
    &lt;div style=&quot;margin-top:1rem;&quot;&gt;
      &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;/div&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;fruit-form&#x27;);
      const fieldset = document.getElementById(&#x27;fruit-fieldset&#x27;);
      const errorEl = document.getElementById(&#x27;fruit-error&#x27;);
      const checkboxes = Array.from(document.querySelectorAll(&#x27;input[name=&quot;fruits[]&quot;]&#x27;));

      function anyChecked() {
        return checkboxes.some(cb =&gt; cb.checked);
      }

      function showError() {
        errorEl.classList.remove(&#x27;hidden&#x27;);
        fieldset.classList.add(&#x27;invalid&#x27;);</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Fruit Checkbox Group&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.4; padding: 2rem; }
    fieldset { border: 1px solid #ccc; padding: 1rem; border-radius: 6px; }
    legend { font-weight: 600; padding: 0 .4rem; }
    .options { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: .5rem; }
    label { display: inline-flex; align-items: center; gap: .5rem; cursor: pointer; }
    .error { color: #b00020; margin-top: .5rem; }
    .invalid input[type=&quot;checkbox&quot;] { outline: 2px solid #b00020; outline-offset: 2px; }
    button { margin-top: 1rem; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;fruit-form&quot; novalidate&gt;
    &lt;fieldset id=&quot;fruit-fieldset&quot; aria-describedby=&quot;fruit-error&quot;&gt;
      &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
      &lt;div class=&quot;options&quot;&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;
      &lt;/div&gt;
      &lt;p id=&quot;fruit-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/p&gt;
    &lt;/fieldset&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;fruit-form&#x27;);
      const fieldset = document.getElementById(&#x27;fruit-fieldset&#x27;);
      const error = document.getElementBy</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
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
    &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;
    &lt;div&gt;You must choose one or more fruits&lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
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
    &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
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
    &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form novalidate&gt;
&lt;fieldset aria-describedby=&quot;fruit-error&quot;&gt;
&lt;legend&gt;What fruits do you like?&lt;/legend&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;fruit-error&quot;&gt;
&lt;label for=&quot;fruit-bananas&quot;&gt;Bananas&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;fruit-oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;fruit-error&quot;&gt;
&lt;label for=&quot;fruit-oranges&quot;&gt;Oranges&lt;/label&gt;
&lt;/div&gt;
&lt;div&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;fruit-apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;fruit-error&quot;&gt;
&lt;label for=&quot;fruit-apples&quot;&gt;Apples&lt;/label&gt;
&lt;/div&gt;
&lt;p id=&quot;fruit-error&quot; role=&quot;alert&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;/fieldset&gt;
  &lt;span class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;/fieldset&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
  &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
  &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
  &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;/fieldset&gt;
  &lt;span class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/span&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
  &lt;/div&gt;
  &lt;div role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #d32f2f; margin-top: 8px;&quot;&gt;
    You must choose one or more fruits
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;&quot; method=&quot;post&quot;&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
    &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
    &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
    &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
    &lt;p id=&quot;error-message&quot;&gt;You must choose one or more fruits&lt;/p&gt;
    &lt;input type=&quot;submit&quot; value=&quot;Submit&quot;&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label&gt;What fruits do you like?&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
  &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
  &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
  &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;span class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/span&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;What fruits do you like?&lt;/legend&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;&lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;&lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;&lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
&lt;/fieldset&gt;
&lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;h2&gt;What fruits do you like?&lt;/h2&gt;
&lt;form&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;banana&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
&lt;label for=&quot;banana&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;orange&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
&lt;label for=&quot;orange&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
&lt;input type=&quot;checkbox&quot; id=&quot;apple&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
&lt;label for=&quot;apple&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
&lt;p class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset aria-invalid=&quot;true&quot; aria-describedby=&quot;error&quot;&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;div id=&quot;error&quot; role=&quot;alert&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
