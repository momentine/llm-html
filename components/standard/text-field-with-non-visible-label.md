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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; style=&quot;position: absolute; left: -10000px; width: 1px; height: 1px; overflow: hidden;&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-input&quot; style=&quot;position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0;&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-input&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; style=&quot;position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; style=&quot;position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0,0,0,0); white-space: nowrap; border: 0;&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; class=&quot;visually-hidden&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search&quot; placeholder=&quot;Search for&quot;&gt;

&lt;style&gt;
.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; aria-label=&quot;Search for&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot;&gt;
&lt;label for=&quot;search&quot; hidden&gt;Search for&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-input&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-input&quot; name=&quot;search&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search&quot; aria-label=&quot;Search for&quot; placeholder=&quot;Search&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; style=&quot;position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; style=&quot;display: none; visibility: none;&quot;&gt;&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; style=&quot;position:absolute;left:-10000px;top:auto;width:1px;height:1</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Search Form with Hidden Label&lt;/title&gt;
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
    &lt;input id=&quot;search&quot; name=&quot;q&quot; type=&quot;search&quot; placeholder=&quot;Search...&quot; /&gt;
    &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;/search&quot; method=&quot;get&quot; role=&quot;search&quot; aria-label=&quot;Site search&quot;&gt;
  &lt;label for=&quot;search-field&quot; class=&quot;sr-only&quot;&gt;Search&lt;/label&gt;
  &lt;input id=&quot;search-field&quot; name=&quot;q&quot; type=&quot;text&quot; placeholder=&quot;Search…&quot; /&gt;
  &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;searchForm&quot; role=&quot;search&quot;&gt;
  &lt;label for=&quot;searchField&quot; class=&quot;visually-hidden&quot;&gt;Search for&lt;/label&gt;
  &lt;input id=&quot;searchField&quot; name=&quot;q&quot; type=&quot;search&quot; placeholder=&quot;Search for...&quot; /&gt;
  &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;searchForm&#x27;);
    form.addEventListener(&#x27;submit&#x27;, function (e) {
      e.preventDefault();
      const q = document.getElementById(&#x27;searchField&#x27;).value.trim();
      if (q) alert(&#x27;Searching for: &#x27; + q);
    });
  })();
&lt;/script&gt;

&lt;style&gt;
  .visually-hidden {
    position: absolute !important;
    width: 1px !important;
    height: 1px !important;
    padding: 0 !important;
    margin: -1px !important;
    overflow: hidden !important;
    clip: rect(0 0 0 0) !important;
    clip-path: inset(50%) !important;
    white-space: nowrap !important;
    border: 0 !important;
  }
&lt;/style&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Search Field with Hidden Label&lt;/title&gt;
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
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 2rem;
    }
    .search-field {
      max-width: 480px;
    }
    .search-field input[type=&quot;search&quot;] {
      width: 100%;
      box-sizing: border-box;
      padding: 0.6rem 0.75rem;
      border: 1px solid #c7c7c7;
      border-radius: 6px;
      font-size: 1rem;
      line-height: 1.2;
    }
    .search-field input[type=&quot;search&quot;]:focus {
      outline: 2px solid #4c9ffe;
      outline-offset: 2px;
      border-color: #4c9ffe;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form class=&quot;search-field&quot; action=&quot;/search&quot; method=&quot;get&quot; role=&quot;search&quot;&gt;
    &lt;label class=&quot;sr-only&quot; for=&quot;search-input&quot;&gt;Search for&lt;/label&gt;
    &lt;input
      id=&quot;search-input&quot;
      name=&quot;q&quot;
      type=&quot;search&quot;
      placeholder=&quot;Search for...&quot;
      autocomplete=&quot;off&quot;
      spellcheck=&quot;false&quot;
      aria-label=&quot;Search for&quot;
    /&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Search Field (Hidden Label)&lt;/title&gt;
  &lt;style&gt;
    /* Visually hidden but accessible to screen readers */
    .sr-only {
      position: absolute !important;
      width: 1px !important;
      height: 1px !important;
      padding: 0 !important;
      margin: -1px !important;
      overflow: hidden !important;
      clip: rect(0 0 0 0) !important;
      white-space: nowrap !important;
      border: 0 !important;
    }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form role=&quot;search&quot; action=&quot;/search&quot; method=&quot;get&quot;&gt;
    &lt;label class=&quot;sr-only&quot; for=&quot;search-field&quot;&gt;Search for&lt;/label&gt;
    &lt;input
      id=&quot;search-field&quot;
      name=&quot;q&quot;
      type=&quot;search&quot;
      placeholder=&quot;Search&quot;
      autocomplete=&quot;off&quot;
      required
    /&gt;
    &lt;button type=&quot;submit&quot;&gt;Search&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search&quot; name=&quot;search&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;search-field&quot; hidden&gt;Search for&lt;/label&gt;
  &lt;input type=&quot;text&quot; id=&quot;search-field&quot; placeholder=&quot;Search for&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;search-field&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;search-field&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input id=&quot;search-field&quot; type=&quot;text&quot; placeholder=&quot;Search for&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; style=&quot;display: none;&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search&quot; placeholder=&quot;Search for...&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; aria-label=&quot;Search for&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;search-field&quot; name=&quot;search&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-field&quot; class=&quot;visually-hidden&quot;&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-field&quot; placeholder=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; id=&quot;search-field&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;search-input&quot; hidden&gt;Search for&lt;/label&gt;
&lt;input type=&quot;text&quot; id=&quot;search-input&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: Search for (hidden label)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;search&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a text field and label for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;text&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible text field for “Search for” with a hidden label</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;search&quot; aria-label=&quot;Search for&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/text-field-with-non-visible-label/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
