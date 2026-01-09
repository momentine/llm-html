<details>
  <summary><strong>Select Field with Accessible Description</strong></summary>
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
      <td>Insert a select field for “Theme” with options light, dark, high contrast with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot;&gt;
  &lt;option value=&quot;light&quot; selected&gt;light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;high contrast&lt;/option&gt;
&lt;/select&gt;
&lt;p&gt;You can change this later&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/select-field-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Select field: Theme with options light, dark, high contrast with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
&lt;select id=&quot;theme&quot; name=&quot;theme&quot; aria-describedby=&quot;theme-note&quot;&gt;
  &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
  &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
  &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
&lt;/select&gt;
&lt;p id=&quot;theme-note&quot;&gt;You can change this later.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/select-field-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A select field labeled “Theme” with options light, dark, high contrast with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
  &lt;select id=&quot;theme&quot; name=&quot;theme&quot;&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
  &lt;/select&gt;
  &lt;small&gt;You can change this later&lt;/small&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/select-field-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a select field and label for “Theme” with options light, dark, high contrast with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
  &lt;body&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
      &lt;select id=&quot;theme&quot; name=&quot;theme&quot; aria-describedby=&quot;theme-note&quot;&gt;
        &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
        &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
        &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
      &lt;/select&gt;
      &lt;p id=&quot;theme-note&quot;&gt;You can change this later.&lt;/p&gt;
    &lt;/div&gt;
  &lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/select-field-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible select field for “Theme” with options light, dark, high contrast with note “You can change this later”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;theme&quot;&gt;Theme&lt;/label&gt;
  &lt;select id=&quot;theme&quot; name=&quot;theme&quot; required aria-describedby=&quot;theme-note&quot;&gt;
    &lt;option value=&quot;light&quot;&gt;Light&lt;/option&gt;
    &lt;option value=&quot;dark&quot;&gt;Dark&lt;/option&gt;
    &lt;option value=&quot;high-contrast&quot;&gt;High contrast&lt;/option&gt;
  &lt;/select&gt;
  &lt;p id=&quot;theme-note&quot;&gt;You can change this later.&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/select-field-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
