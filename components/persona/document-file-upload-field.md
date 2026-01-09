<details>
  <summary><strong>Document File Upload Field</strong></summary>
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
      <td>Insert a document file upload field for “Upload Document”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
  &lt;label for=&quot;upload-document&quot;&gt;Upload Document&lt;/label&gt;
  &lt;input id=&quot;upload-document&quot; name=&quot;document&quot; type=&quot;file&quot; accept=&quot;.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.odt,.ods,.odp,.csv&quot; required /&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/document-file-upload-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Document file upload field: Upload Document</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Upload Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;label for=&quot;document-upload&quot;&gt;Upload Document&lt;/label&gt;
    &lt;input
      id=&quot;document-upload&quot;
      name=&quot;document&quot;
      type=&quot;file&quot;
      accept=&quot;.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.csv,.odt,.ods,.odp&quot;
      multiple
      required
      aria-describedby=&quot;document-upload-help&quot;
    /&gt;
    &lt;p id=&quot;document-upload-help&quot;&gt;Accepted formats: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, RTF, CSV, ODT, ODP. You can select multiple files.&lt;/p&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/document-file-upload-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A document file upload field labeled “Upload Document”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form action=&quot;/upload&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
  &lt;label for=&quot;document-upload&quot;&gt;Upload Document&lt;/label&gt;
  &lt;input type=&quot;file&quot; id=&quot;document-upload&quot; name=&quot;document&quot; accept=&quot;.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.odt,.csv&quot; /&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/document-file-upload-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a document file upload field and label for “Upload Document”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;document-upload&quot;&gt;Upload Document&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;document-upload&quot; name=&quot;document&quot; accept=&quot;.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.odt,.ods,.odp&quot; aria-describedby=&quot;document-upload-help&quot; required&gt;
&lt;small id=&quot;document-upload-help&quot;&gt;Accepted types: PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT, RTF, ODT, ODS, ODP&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/document-file-upload-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible document file upload field for “Upload Document”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Document Upload&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 2rem; line-height: 1.5; }
    .field { margin-block: 1rem; max-width: 40rem; }
    label { font-weight: 600; display: inline-block; margin-bottom: .375rem; }
    .help { font-size: .9375rem; color: #555; margin-top: .375rem; }
    @media (prefers-color-scheme: dark) {
      .help { color: #c9c9c9; }
    }
    .file-row { display: flex; align-items: center; gap: .5rem; flex-wrap: wrap; }
    input[type=&quot;file&quot;] { font: inherit; }
    .file-name { min-height: 1.25rem; }
    button.clear-btn {
      border: 1px solid currentColor;
      background: transparent;
      padding: .375rem .625rem;
      border-radius: .375rem;
      cursor: pointer;
    }
    button.clear-btn:disabled { opacity: .6; cursor: not-allowed; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;div class=&quot;field&quot;&gt;
      &lt;label for=&quot;document-upload&quot;&gt;Upload Document&lt;/label&gt;
      &lt;input
        id=&quot;document-upload&quot;
        name=&quot;document&quot;
        type=&quot;file&quot;
        accept=&quot;.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.txt,.rtf,.odt,.ods,.odp,.csv&quot;
        aria-describedby=&quot;document-help document-filename&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/document-file-upload-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
