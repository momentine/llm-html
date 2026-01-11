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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; list=&quot;firstNameSuggestions&quot;&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;firstName&quot; id=&quot;firstName&quot; placeholder=&quot;Your first name&quot; list=&quot;firstNameSuggestions&quot;&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; list=&quot;suggestions&quot; placeholder=&quot;Your first name&quot;&gt;
&lt;datalist id=&quot;suggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; list=&quot;firstNameSuggestions&quot;&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input 
  type=&quot;text&quot; 
  id=&quot;firstName&quot; 
  name=&quot;firstName&quot; 
  autocomplete=&quot;given-name&quot;
  list=&quot;firstNameSuggestions&quot;
  aria-label=&quot;Your first name&quot;
&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; placeholder=&quot;Your first name&quot; autocomplete=&quot;name&quot; value=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; autocomplete=&quot;name&quot; placeholder=&quot;Your first name&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; placeholder=&quot;Your first name&quot; autocomplete=&quot;name&quot; value=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; autocomplete=&quot;name&quot; value=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; id=&quot;first_name&quot; aria-label=&quot;Your first name&quot; autocomplete=&quot;name&quot; placeholder=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;First Name Input&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;title&gt;Text Field with Autocomplete&lt;/</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;First Name Input&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
    &lt;title&gt;First Name Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;fname</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;fname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;fname&quot; name=&quot;fname&quot; autocomplete=&quot;given-name&quot; list=&quot;name-</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;First Name Field with Suggestion&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;get&quot;&gt;
    &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;&lt;br /&gt;
    &lt;input
      type=&quot;text&quot;
      id=&quot;firstName&quot;
      name=&quot;first_name&quot;
      list=&quot;firstNameSuggestions&quot;
      autocomplete=&quot;given-name&quot;
    /&gt;
    &lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
      &lt;option value=&quot;John Doe&quot;&gt;&lt;/option&gt;
    &lt;/datalist&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;First Name with Autocomplete Suggestion&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/submit&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
    &lt;input
      id=&quot;firstName&quot;
      name=&quot;firstName&quot;
      type=&quot;text&quot;
      autocomplete=&quot;given-name&quot;
      list=&quot;first-name-suggestions&quot;
      placeholder=&quot;Start typing...&quot;
    /&gt;
    &lt;datalist id=&quot;first-name-suggestions&quot;&gt;
      &lt;option value=&quot;John Doe&quot;&gt;&lt;/option&gt;
    &lt;/datalist&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;title&gt;First Name Input&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
  &lt;input id=&quot;firstName&quot; name=&quot;firstName&quot; type=&quot;text&quot; autocomplete=&quot;name&quot; list=&quot;firstNameSuggestions&quot; placeholder=&quot;John&quot;&gt;
  &lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
    &lt;option value=&quot;John Doe&quot;&gt;&lt;/option&gt;
  &lt;/datalist&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;First Name with Autocomplete&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
  &lt;input
    type=&quot;text&quot;
    id=&quot;firstName&quot;
    name=&quot;firstName&quot;
    placeholder=&quot;John Doe&quot;
    autocomplete=&quot;given-name&quot;
    list=&quot;firstNameSuggestions&quot;
  /&gt;
  &lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
    &lt;option value=&quot;John Doe&quot;&gt;&lt;/option&gt;
  &lt;/datalist&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;title&gt;First name field with autocomplete suggestion&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
    &lt;input
      id=&quot;firstName&quot;
      name=&quot;firstName&quot;
      type=&quot;text</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;first-name&quot;&gt;Your first name&lt;/label&gt;
&lt;input id=&quot;first-name&quot; name=&quot;first-name&quot; type=&quot;text&quot; list=&quot;name-suggestion&quot;&gt;
&lt;datalist id=&quot;name-suggestion&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; list=&quot;firstNameSuggestions&quot;&gt;
&lt;datalist id=&quot;firstNameSuggestions&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;first-name&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;first-name&quot; list=&quot;first-name-list&quot;&gt;
&lt;datalist id=&quot;first-name-list&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;first-name&quot;&gt;Your first name&lt;/label&gt;
&lt;input id=&quot;first-name&quot; type=&quot;text&quot; name=&quot;first-name&quot; list=&quot;first-name-suggestions&quot;&gt;
&lt;datalist id=&quot;first-name-suggestions&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;first-name&quot;&gt;Your first name&lt;/label&gt;
&lt;input id=&quot;first-name&quot; name=&quot;first-name&quot; type=&quot;text&quot; autocomplete=&quot;given-name&quot; list=&quot;first-name-suggestions&quot; aria-describedby=&quot;first-name-helper&quot;&gt;
&lt;datalist id=&quot;first-name-suggestions&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;
&lt;div id=&quot;first-name-helper&quot;&gt;Enter your given name.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; placeholder=&quot;Your first name&quot; autocomplete=&quot;name&quot; value=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; placeholder=&quot;Your first name&quot; list=&quot;names&quot;&gt;
&lt;datalist id=&quot;names&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;first_name&quot; placeholder=&quot;John Doe&quot; autocomplete=&quot;given-name&quot; aria-label=&quot;Your first name&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstName&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstName&quot; name=&quot;firstName&quot; autocomplete=&quot;name&quot; placeholder=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;first-name&quot; name=&quot;first-name&quot; autocomplete=&quot;name&quot; placeholder=&quot;Your first name&quot; aria-label=&quot;Your first name&quot; value=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstname&quot; autocomplete=&quot;given-name&quot; placeholder=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Your first name with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstname&quot; list=&quot;suggestions&quot;&gt;
&lt;datalist id=&quot;suggestions&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field labeled “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstname&quot; placeholder=&quot;John Doe&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstname&quot; list=&quot;names&quot;&gt;
&lt;datalist id=&quot;names&quot;&gt;
&lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Your first name” with autocomplete suggestion “John Doe”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;firstname&quot;&gt;Your first name&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;firstname&quot; autocomplete=&quot;given-name&quot; list=&quot;names&quot;&gt;
&lt;datalist id=&quot;names&quot;&gt;
  &lt;option value=&quot;John Doe&quot;&gt;
&lt;/datalist&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-autocomplete-suggestion/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
