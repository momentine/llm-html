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
      <td><a href="docs/persona-outputs/range-slider/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/range-slider/minimax-minimax-m2/g2.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/range-slider/minimax-minimax-m2/g3.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/range-slider/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
      <td><a href="docs/persona-outputs/range-slider/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
