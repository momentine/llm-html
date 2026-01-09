<details>
  <summary><strong>Range Slider</strong></summary>
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
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input 
        type=&quot;range&quot; 
        id=&quot;volume&quot; 
        name=&quot;volume&quot; 
        min=&quot;1&quot; 
        max=&quot;10&quot; 
        value=&quot;5&quot; 
        aria-valuemin=&quot;1&quot; 
        aria-valuemax=&quot;10&quot; 
        aria-valuenow=&quot;5&quot;
        aria-label=&quot;Volume level from 1 to 10&quot;
    &gt;
    &lt;output for=&quot;volume&quot; aria-live=&quot;polite&quot;&gt;5&lt;/output&gt;
    
    &lt;script&gt;
        const slider = document.getElementById(&#x27;volume&#x27;);
        const output = document.querySelector(&#x27;output&#x27;);
        
        slider.addEventListener(&#x27;input&#x27;, function() {
            output.textContent = this.value;
            this.setAttribute(&#x27;aria-valuenow&#x27;, this.value);
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; step=&quot;1&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; id=&quot;volume&quot; name=&quot;volume&quot;&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input id=&quot;volume&quot; type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot; /&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Volume Range Slider&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input id=&quot;volume&quot; type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot;&gt;
  &lt;output for=&quot;volume&quot; id=&quot;volume-value&quot;&gt;5&lt;/output&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; /&gt;
&lt;output for=&quot;volume&quot; id=&quot;volumeValue&quot;&gt;5&lt;/output&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input
    id=&quot;volume&quot;
    name=&quot;volume&quot;
    type=&quot;range&quot;
    min=&quot;1&quot;
    max=&quot;10&quot;
    step=&quot;1&quot;
    value=&quot;5&quot;
    aria-valuemin=&quot;1&quot;
    aria-valuemax=&quot;10&quot;
    aria-valuenow=&quot;5&quot;
    aria-label=&quot;Volume&quot;
  /&gt;
  &lt;output id=&quot;volume-value&quot; for=&quot;volume&quot; aria-live=&quot;polite&quot;&gt;5&lt;/output&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-describedby=&quot;volume-hint&quot;&gt;
  &lt;div id=&quot;volume-hint&quot;&gt;Use the arrow keys to select a value between 1 and 10.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume (range input 1–10)&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume (1-10)&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot; aria-label=&quot;Volume level&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/persona-outputs/range-slider/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
