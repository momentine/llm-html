<details>
  <summary><strong>Multiple File Upload Field</strong></summary>
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
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input id=&quot;upload-files&quot; name=&quot;upload_files[]&quot; type=&quot;file&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/multiple-file-upload-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Multiple File Upload&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;
    &lt;input
      id=&quot;files&quot;
      name=&quot;files[]&quot;
      type=&quot;file&quot;
      multiple
      accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document,text/plain,image/png,image/jpeg,image/gif,image/svg+xml&quot;
    &gt;
    &lt;button type=&quot;submit&quot;&gt;Upload&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/multiple-file-upload-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input id=&quot;upload-files&quot; type=&quot;file&quot; name=&quot;files[]&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/multiple-file-upload-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;uploadFiles&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;uploadFiles&quot; name=&quot;uploadFiles&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/multiple-file-upload-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Upload Files&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;div&gt;
      &lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;
      &lt;input
        id=&quot;files&quot;
        name=&quot;files[]&quot;
        type=&quot;file&quot;
        multiple
        accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot;
        aria-describedby=&quot;files-help&quot;
      /&gt;
      &lt;div id=&quot;files-help&quot;&gt;
        Accepted types: PDF, DOCX, TXT, PNG, JPG, GIF, SVG. You can select multiple files.
      &lt;/div&gt;
    &lt;/div&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/multiple-file-upload-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
