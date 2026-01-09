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
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Volume Control&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
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
    &lt;output for=&quot;volume&quot; id=&quot;volumeValue&quot;&gt;5&lt;/output&gt;
    
    &lt;script&gt;
        const volumeSlider = document.getElementById(&#x27;volume&#x27;);
        const volumeValue = document.getElementById(&#x27;volumeValue&#x27;);
        
        volumeSlider.addEventListener(&#x27;input&#x27;, function() {
            volumeValue.textContent = this.value;
        });
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume: &lt;span id=&quot;volumeValue&quot;&gt;5&lt;/span&gt;&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; oninput=&quot;document.getElementById(&#x27;volumeValue&#x27;).textContent = this.value&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot;&gt;
    &lt;output for=&quot;volume&quot; aria-live=&quot;polite&quot;&gt;5&lt;/output&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; aria-label=&quot;Volume control&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot;&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;output for=&quot;volume&quot; id=&quot;volume-output&quot;&gt;5&lt;/output&gt;

&lt;script&gt;
document.getElementById(&#x27;volume&#x27;).addEventListener(&#x27;input&#x27;, function() {
  document.getElementById(&#x27;volume-output&#x27;).textContent = this.value;
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
  &lt;title&gt;Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;title&gt;Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
  &lt;title&gt;Accessible Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot;&gt;
  &lt;output for=&quot;volume&quot; id=&quot;volume-value&quot;&gt;5&lt;/output&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Volume Range Slider (1–10)&lt;/title&gt;
  &lt;style&gt;
    :root {
      --accent: #3b82f6;
      --track: #e5e7eb;
      --thumb: #ffffff;
    }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 2rem;
      background: #f8fafc;
      color: #0f172a;
    }
    .card {
      max-width: 420px;
      margin: 0 auto;
      background: #fff;
      border: 1px solid #e2e8f0;
      border-radius: 12px;
      padding: 1.25rem 1.25rem 1.5rem;
      box-shadow: 0 1px 2px rgba(0,0,0,.04);
    }
    label {
      display: block;
      font-weight: 600;
      margin-bottom: .5rem;
    }
    .row {
      display: flex;
      align-items: center;
      gap: .75rem;
    }
    output {
      min-width: 2ch;
      text-align: right;
      font-variant-numeric: tabular-nums;
      font-weight: 600;
    }
    input[type=&quot;range&quot;] {
      -webkit-appearance: none;
      appearance: none;
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: linear-gradient(var(--accent), var(--accent)) var(--progress, 0%) / var(--progress, 0%) 100% no-repeat, var(--track);
      outline: none;
      transition: background-size .15s ease;
    }
    input[type=&quot;range&quot;]::-webkit-slider-thumb {
      -webkit-appearance: none;
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--thumb);
      border: 2px solid var(--accent);
      box-shadow: 0 1px 2px rgba(0,0,</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot;&gt;
&lt;span aria-hidden=&quot;true&quot;&gt;5&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Volume&lt;/legend&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume level (1–10)&lt;/label&gt;
    &lt;input
      id=&quot;volume&quot;
      name=&quot;volume&quot;
      type=&quot;range&quot;
      min=&quot;1&quot;
      max=&quot;10&quot;
      step=&quot;1&quot;
      value=&quot;5&quot;
      aria-label=&quot;Volume&quot;
      aria-valuemin=&quot;1&quot;
      aria-valuemax=&quot;10&quot;
      aria-valuenow=&quot;5&quot;
    /&gt;
  &lt;/fieldset&gt;

  &lt;script&gt;
    (function () {
      const volume = document.getElementById(&#x27;volume&#x27;);
      const update = () =&gt; volume.setAttribute(&#x27;aria-valuenow&#x27;, volume.value);
      volume.addEventListener(&#x27;input&#x27;, update);
      update();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Volume Range Slider (1–10)&lt;/title&gt;
  &lt;style&gt;
    :root {
      color-scheme: light dark;
    }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.4;
      margin: 2rem;
    }
    .volume-group {
      max-width: 420px;
    }
    .label-row {
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 0.25rem;
    }
    label {
      font-weight: 600;
    }
    output {
      font-variant-numeric: tabular-nums;
      min-width: 2ch;
      text-align: right;
    }
    .range-wrapper {
      display: grid;
      gap: 0.25rem;
    }
    input[type=&quot;range&quot;] {
      width: 100%;
      margin: 0;
    }
    .ticks {
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      color: #666;
      padding: 0 0.25rem;
    }
    .ticks span {
      position: relative;
      text-align: center;
      width: 1ch;
    }
    .ticks span::before {
      content: &quot;&quot;;
      position: absolute;
      top: -</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label&gt;Volume &lt;input type=&quot;range&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
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
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; list=&quot;volume-levels&quot; aria-describedby=&quot;volume-hint&quot;&gt;
  &lt;datalist id=&quot;volume-levels&quot;&gt;
    &lt;option value=&quot;1&quot;&gt;
    &lt;option value=&quot;2&quot;&gt;
    &lt;option value=&quot;3&quot;&gt;
    &lt;option value=&quot;4&quot;&gt;
    &lt;option value=&quot;5&quot;&gt;
    &lt;option value=&quot;6&quot;&gt;
    &lt;option value=&quot;7&quot;&gt;
    &lt;option value=&quot;8&quot;&gt;
    &lt;option value=&quot;9&quot;&gt;
    &lt;option value=&quot;10&quot;&gt;
  &lt;/datalist&gt;
  &lt;p id=&quot;volume-hint&quot;&gt;Choose a volume level from 1 (quietest) to 10 (loudest).&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume (1-10)&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot; role=&quot;slider&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/range-slider/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
