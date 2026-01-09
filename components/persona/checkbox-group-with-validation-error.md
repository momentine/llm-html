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
  &lt;div style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      bananas
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      oranges
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      apples
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
      bananas
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
      oranges
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
      apples
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
  
  &lt;div role=&quot;alert&quot;&gt;
    &lt;span style=&quot;color: red;&quot;&gt;You must choose one or more fruits&lt;/span&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
  &lt;div role=&quot;group&quot; aria-labelledby=&quot;fruits-label&quot; aria-describedby=&quot;fruits-error&quot;&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; aria-invalid=&quot;true&quot;&gt;
      &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot; aria-invalid=&quot;true&quot;&gt;
      &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot; aria-invalid=&quot;true&quot;&gt;
      &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;div id=&quot;fruits-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;
    &lt;span style=&quot;color: #d32f2f;&quot;&gt;You must choose one or more fruits&lt;/span&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
  &lt;div id=&quot;error&quot; style=&quot;color:red; display:none;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
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
    &lt;div id=&quot;error-message&quot; style=&quot;color: red; display: none;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
  &lt;div style=&quot;color: red; font-size: 0.9em; margin-top: 5px;&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;p&gt;What fruits do you like?&lt;/p&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;&lt;br&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;&lt;br&gt;
  &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;&lt;br&gt;
  &lt;p style=&quot;color: red; display: none;&quot; id=&quot;error-msg&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
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
  &lt;div role=&quot;alert&quot; id=&quot;fruit-error&quot; aria-live=&quot;assertive&quot; hidden&gt;You must choose one or more fruits&lt;/div&gt;
  
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
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-invalid=&quot;true&quot; aria-describedby=&quot;fruit-error&quot;&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;fruit-error-message&quot;&gt;
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
  &lt;p id=&quot;fruit-error-message&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;fruit-error&quot; aria-invalid=&quot;true&quot;&gt;
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
  &lt;div id=&quot;fruit-error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;fruit-error&quot;&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;checkbox&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-invalid=&quot;true&quot; aria-describedby=&quot;fruit-error&quot;&gt;
  &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;fruit-form&quot; action=&quot;#&quot; method=&quot;post&quot;&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;fruit-form&#x27;);
      const checkboxes = form.querySelectorAll(&#x27;input[name=&quot;fruits[]&quot;]&#x27;);
      const first = checkboxes[0];

      function validateFruits() {
        const anyChecked = Array.prototype.some.call(checkboxes, function (cb) {
          return cb.checked;
        });
        if (!anyChecked) {
          first.setCustomValidity(&#x27;You must choose one or more fruits&#x27;);
        } else {
          first.setCustomValidity(&#x27;&#x27;);
        }
      }

      Array.prototype.forEach.call(checkboxes, function (cb) {
        cb.addEventListener(&#x27;change&#x27;, validateFruits);
        cb.addEventListener(&#x27;invalid&#x27;, validateFruits);
      });

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        validateFruits();
        if (!form.checkValidity()) {
          e.preventDefault();
          form.reportValidity();
        }
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Checkbox group: What fruits do you like? with options bananas, oranges, apples with error message “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;fruitForm&quot; novalidate&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;bananas&quot;&gt; Bananas
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;oranges&quot;&gt; Oranges
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits[]&quot; value=&quot;apples&quot;&gt; Apples
    &lt;/label&gt;
    &lt;div id=&quot;fruits-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color:#b00020; display:none; margin-top:8px;&quot;&gt;
      You must choose one or more fruits
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;div style=&quot;margin-top:12px;&quot;&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/div&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;fruitForm&#x27;);
    const checkboxes = form.querySelectorAll(&#x27;input[name=&quot;fruits[]&quot;]&#x27;);
    const errorEl = document.getElementById(&#x27;fruits-error&#x27;);

    function atLeastOneChecked() {
      return Array.from(checkboxes).some(cb =&gt; cb.checked);
    }

    function showError() {
      errorEl.textContent = &#x27;You must choose one or more fruits&#x27;;
      errorEl.style.display = &#x27;block&#x27;;
    }

    function hideError() {
      errorEl.textContent = &#x27;&#x27;;
      errorEl.style.display = &#x27;none&#x27;;
    }

    form.addEventListener(&#x27;submit&#x27;, function (e) {
      if (!atLeastOneChecked()) {
        e.preventDefault();</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A checkbox group labeled “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;fruit-form&quot; novalidate&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; bananas
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; oranges
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; apples
    &lt;/label&gt;
    &lt;div id=&quot;fruit-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;display:none;color:#b00020;margin-top:8px;&quot;&gt;
      You must choose one or more fruits
    &lt;/div&gt;
    &lt;div style=&quot;margin-top:12px;&quot;&gt;
      &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;fruit-form&#x27;);
      const errorEl = document.getElementById(&#x27;fruit-error&#x27;);
      const checkboxes = form.querySelectorAll(&#x27;input[name=&quot;fruits&quot;]&#x27;);

      function validateFruits() {
        const anyChecked = Array.prototype.some.call(checkboxes, function (cb) {
          return cb.checked;
        });
        if (!anyChecked) {
          errorEl.style.display = &#x27;block&#x27;;
          return false;
        }
        errorEl.style.display = &#x27;none&#x27;;
        return true;
      }

      form.addEventListener(&#x27;submit&#x27;, function (e) {
        if (!validateFruits()) {
          e.preventDefault();
          return false;
        }
        e.preventDefault();
        alert(&#x27;Submitted!&#x27;);
      });

      checkboxes.forEach(function (cb) {
        cb.addEventListener(&#x27;change&#x27;, validateFruits);
      });
    })();
  &lt;/script&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a checkbox group and labels for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;fruit-form&quot; method=&quot;post&quot; action=&quot;#&quot;&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;&lt;br&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;fruit-form&#x27;);
    const checkboxes = form.querySelectorAll(&#x27;input[name=&quot;fruits&quot;]&#x27;);

    function</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;title&gt;Accessible Checkbox Group - Fruits&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;main&gt;
    &lt;h1&gt;What fruits do you like?&lt;/h1&gt;

    &lt;form id=&quot;fruit-form&quot; novalidate&gt;
      &lt;fieldset id=&quot;fruit-fieldset&quot;
                role=&quot;group&quot;
                aria-labelledby=&quot;fruit-legend&quot;
                aria-describedby=&quot;fruit-error&quot;&gt;
        &lt;legend id=&quot;fruit-legend&quot;&gt;What fruits do you like?&lt;/legend&gt;

        &lt;div class=&quot;options&quot;&gt;
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
        &lt;/div&gt;

        &lt;p id=&quot;fruit-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot; hidden&gt;
          You must choose one or more fruits
        &lt;/p&gt;
      &lt;/fieldset&gt;

      &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
    &lt;/form&gt;
  &lt;/main&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
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
  &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
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
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;bananas&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;oranges&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;apples&lt;/label&gt;
    &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;
    &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
      &lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; required&gt;
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
  &lt;p&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset aria-describedby=&quot;fruit-error&quot;&gt;
    &lt;legend&gt;What fruits do you like?&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;checkbox&quot; id=&quot;fruit-bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot; aria-invalid=&quot;true&quot;&gt;
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
    &lt;p id=&quot;fruit-error&quot; role=&quot;alert&quot;&gt;You must choose one or more fruits&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
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
  &lt;input type=&quot;checkbox&quot; id=&quot;bananas&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt;
  &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
  &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
  &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;span class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/span&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
  &lt;label for=&quot;bananas&quot;&gt;Bananas&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;oranges&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt;
  &lt;label for=&quot;oranges&quot;&gt;Oranges&lt;/label&gt;&lt;br&gt;
  &lt;input type=&quot;checkbox&quot; id=&quot;apples&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt;
  &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;&lt;br&gt;
  &lt;span class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/span&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
  &lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a checkbox group for “What fruits do you like?” with options bananas, oranges, apples with a validation error “You must choose one or more fruits”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;What fruits do you like?&lt;/label&gt;
&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas
&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges
&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples
&lt;div&gt;You must choose one or more fruits&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
    &lt;label for=&quot;apples&quot;&gt;Apples&lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;p id=&quot;error-message&quot;&gt;You must choose one or more fruits&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;&lt;br&gt;
    &lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;bananas&quot;&gt; Bananas&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;oranges&quot;&gt; Oranges&lt;/label&gt;&lt;br&gt;
    &lt;label&gt;&lt;input type=&quot;checkbox&quot; name=&quot;fruits&quot; value=&quot;apples&quot;&gt; Apples&lt;/label&gt;&lt;br&gt;
  &lt;/fieldset&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
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
  &lt;div role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;You must choose one or more fruits&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/checkbox-group-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
