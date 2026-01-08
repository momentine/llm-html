<details>
  <summary><strong>Select Field with Required</strong></summary>
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
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme &lt;span style=&quot;color: red;&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
    &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme &lt;span style=&quot;color: red;&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme &lt;span style=&quot;color: red;&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;label for=&quot;theme&quot;&gt;Theme &lt;span aria-label=&quot;required&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme &lt;span aria-label=&quot;required&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required aria-required=&quot;true&quot;&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;select name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;select required&gt;
    &lt;option value=&quot;&quot; disabled selected&gt;Select theme&lt;/option&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot; disabled selected&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html"></code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme (required)&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot; disabled selected&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
  &lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
    &lt;option value=&quot;&quot; disabled selected&gt;Select a theme&lt;/option&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
  &lt;/select&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot; disabled selected&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Theme Select&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
    &lt;select id=&quot;theme&quot; name=&quot;theme&quot; required aria-describedby=&quot;theme-hint&quot;&gt;
      &lt;option value=&quot;&quot; disabled selected&gt;Select a theme&lt;/option&gt;
      &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
      &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
      &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
    &lt;/select&gt;
    &lt;p id=&quot;theme-hint&quot;&gt;Choose a color theme. This field is required.&lt;/p&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
  &lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
    &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
  &lt;/select&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
    &lt;option value=&quot;&quot;&gt;Select theme&lt;/option&gt;
    &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;select name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;select required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;label for=&quot;theme&quot;&gt;Theme *&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Select a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">```html
&lt;label for=&quot;theme&quot;&gt;Theme *&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;&quot;&gt;Choose a theme&lt;/option&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High Contrast&lt;/option&gt;
&lt;/select&gt;
```</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a required select field for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field (required): Theme with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A required select field labeled “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; required&gt;
&lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
&lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
&lt;option value=&quot;high contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a required select field and label for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
&lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
&lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
&lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field (required) for “Theme” with options light, dark, high contrast</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; required&gt;
  &lt;option value=&quot;light&quot;&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/select-field-with-required/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
