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
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;output for=&quot;volume&quot;&gt;5&lt;/output&gt;

&lt;script&gt;
const volumeSlider = document.getElementById(&#x27;volume&#x27;);
const volumeOutput = document.querySelector(&#x27;output[for=&quot;volume&quot;]&#x27;);

volumeSlider.addEventListener(&#x27;input&#x27;, function() {
  volumeOutput.textContent = this.value;
});
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
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
    &lt;title&gt;Volume Control&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
        &lt;input 
            type=&quot;range&quot; 
            id=&quot;volume&quot; 
            name=&quot;volume&quot; 
            min=&quot;1&quot; 
            max=&quot;10&quot; 
            value=&quot;5&quot; 
            step=&quot;1&quot;
            aria-valuemin=&quot;1&quot;
            aria-valuemax=&quot;10&quot;
            aria-valuenow=&quot;5&quot;
            aria-label=&quot;Volume control from 1 to 10&quot;&gt;
        &lt;output for=&quot;volume&quot; aria-live=&quot;polite&quot;&gt;5&lt;/output&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; /&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; aria-label=&quot;Volume&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
    &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A range slider labeled “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
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
  &lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Volume Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;input
      type=&quot;range&quot;
      id=&quot;volume&quot;
      name=&quot;volume&quot;
      min=&quot;1&quot;
      max=&quot;10&quot;
      step=&quot;1&quot;
      value=&quot;5&quot;
      aria-label=&quot;Volume&quot;
    /&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Volume Range Slider (1–10)&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; padding: 2rem; }
    .field { max-width: 420px; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    .row { display: flex; align-items: center; gap: 0.75rem; }
    output { min-width: 2ch; text-align: right; font-variant-numeric: tabular-nums; }
    input[type=&quot;range&quot;] { width: 100%; }
    datalist { display: flex; justify-content: space-between; width: 100%; }
    datalist option { position: relative; top: 1.25rem; font-size: 0.85rem; color: #555; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form class=&quot;field&quot; onsubmit=&quot;return false;&quot;&gt;
    &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
    &lt;div class=&quot;row&quot;&gt;
      &lt;input
        id=&quot;volume&quot;
        name=&quot;volume&quot;
        type=&quot;range&quot;
        min=&quot;1&quot;
        max=&quot;10&quot;
        step=&quot;1&quot;
        value=&quot;5&quot;
        list=&quot;volume-ticks&quot;
        aria-label=&quot;Volume&quot;
      /&gt;
      &lt;output id=&quot;volumeValue&quot; for=&quot;volume&quot; aria-live=&quot;polite&quot;&gt;5&lt;/output&gt;
    &lt;/div&gt;
    &lt;datalist id=&quot;volume-ticks&quot;&gt;
      &lt;option value=&quot;1&quot; label=&quot;1&quot;&gt;&lt;/option&gt;
      &lt;option value=&quot;2&quot; label=&quot;2&quot;&gt;&lt;/option&gt;
      &lt;option value=&quot;3&quot; label=&quot;3&quot;&gt;&lt;/option&gt;
      &lt;option value=&quot;4&quot; label=&quot;4&quot;&gt;&lt;/option&gt;
      &lt;option value=&quot;5&quot;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Volume Range Slider&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; step=&quot;1&quot; aria-label=&quot;Volume&quot;&gt;
  &lt;output id=&quot;volumeValue&quot; for=&quot;volume&quot;&gt;5&lt;/output&gt;
  &lt;script&gt;
    (function () {
      const slider = document.getElementById(&#x27;volume&#x27;);
      const out = document.getElementById(&#x27;volumeValue&#x27;);
      const update = () =&gt; { out.value = slider.value; out.textContent = slider.value; };
      slider.addEventListener(&#x27;input&#x27;, update);
      update();
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a range slider and label for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Volume Range Slider&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input id=&quot;volume&quot; type=&quot;range&quot; min=&quot;1&quot; max=&quot;10&quot; step=&quot;1&quot; value=&quot;5&quot; aria-label=&quot;Volume&quot; /&gt;
  &lt;output id=&quot;volume-value&quot; for=&quot;volume&quot;&gt;5&lt;/output&gt;

  &lt;script&gt;
    const volume = document.getElementById(&#x27;volume&#x27;);
    const volumeValue = document.getElementById(&#x27;volume-value&#x27;);
    volume.addEventListener(&#x27;input&#x27;, () =&gt; {
      volumeValue.textContent = volume.value;
      volume.setAttribute(&#x27;aria-valuenow&#x27;, volume.value);
    });
    // Initialize ARIA value
    volume.setAttribute(&#x27;aria-valuenow&#x27;, volume.value);
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
      --focus: #1d4ed8;
    }
    body {
      font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.5;
      padding: 2rem;
      color: #111;
      background: #fff;
    }
    .field {
      max-width: 28rem;
    }
    label {
      display: inline-block;
      font-weight: 600;
      margin-bottom: 0.5rem;
    }
    .slider-row {
      display: grid;
      grid-template-columns: 1fr auto;
      align-items: center;
      gap: 0.75rem;
    }
    input[type=&quot;range&quot;] {
      width: 100%;
    }
    output {
      min-width: 2ch;
      text-align: right;
      font-variant-numeric: tabular-nums;
    }
    .ticks {
      margin-top: 0.25rem;
      color: #555;
      font-size: 0.875rem;
    }
    /* Visible focus for keyboard users */
    input[type=&quot;range&quot;]:focus-visible {
      outline: 3px solid var(--focus);
      outline-offset:</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
  &lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot;&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Range slider: Volume (range input 1–10)</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;range&quot; id=&quot;volume&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;
&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/qwen-qwen3-coder/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/qwen-qwen3-coder/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume-slider&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume-slider&quot; name=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot; aria-valuemin=&quot;1&quot; aria-valuemax=&quot;10&quot; aria-valuenow=&quot;5&quot; aria-labelledby=&quot;volume-label&quot;&gt;
&lt;div id=&quot;volume-label&quot;&gt;Volume level: &lt;span id=&quot;volume-value&quot;&gt;5&lt;/span&gt;&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/qwen-qwen3-coder/g5.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
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
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible range slider for “Volume” with range input 1–10</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;volume&quot;&gt;Volume&lt;/label&gt;
&lt;input type=&quot;range&quot; id=&quot;volume&quot; min=&quot;1&quot; max=&quot;10&quot; value=&quot;5&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/standard-outputs/range-slider/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
