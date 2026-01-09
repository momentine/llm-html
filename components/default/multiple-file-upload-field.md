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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;fileUpload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;fileUpload&quot; name=&quot;fileUpload&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Multiple File Upload&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;label for=&quot;fileUpload&quot;&gt;Upload Files&lt;/label&gt;
        &lt;input type=&quot;file&quot; id=&quot;fileUpload&quot; name=&quot;fileUpload&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input 
  type=&quot;file&quot; 
  id=&quot;file-upload&quot; 
  name=&quot;file-upload&quot; 
  multiple 
  accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;
&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;file-upload&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Upload Files&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;
        &lt;fieldset&gt;
            &lt;legend&gt;Upload Files&lt;/legend&gt;
            &lt;label for=&quot;file-upload&quot;&gt;
                Choose files to upload (PDF, DOCX, TXT, PNG, JPG, GIF, SVG)
            &lt;/label&gt;
            &lt;input 
                type=&quot;file&quot; 
                id=&quot;file-upload&quot; 
                name=&quot;file-upload&quot; 
                multiple 
                accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot;
                aria-describedby=&quot;file-upload-help&quot;
            &gt;
            &lt;div id=&quot;file-upload-help&quot;&gt;
                You can select multiple files. Accepted formats: PDF, DOCX, TXT, PNG, JPG, GIF, SVG
            &lt;/div&gt;
        &lt;/fieldset&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;upload_files&quot; id=&quot;upload_files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;files&quot; id=&quot;files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;
&lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Upload Files&lt;/legend&gt;
  &lt;label for=&quot;file-upload&quot;&gt;Select files to upload&lt;/label&gt;
  &lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; aria-describedby=&quot;file-types&quot;&gt;
  &lt;p id=&quot;file-types&quot;&gt;Accepted file types: PDF, DOCX, TXT, PNG, JPG, GIF, SVG&lt;/p&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;File Upload&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;File Upload&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
    &lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files[]&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;title&gt;File Upload&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
    &lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;File Upload&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
        &lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; aria-describedby=&quot;file-upload-info&quot;&gt;
        &lt;p id=&quot;file-upload-info&quot;&gt;
            Accepted file types: PDF, DOCX, TXT, PNG, JPG, GIF, SVG.
        &lt;/p&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;uploadFiles&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg,image/png,image/jpeg,image/gif,image/svg+xml&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
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
  &lt;form action=&quot;#&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;label for=&quot;files&quot;&gt;Upload Files (.pdf, .docx, .txt, .png, .jpg, .gif, .svg):&lt;/label&gt;&lt;br&gt;
    &lt;input
      id=&quot;files&quot;
      name=&quot;files[]&quot;
      type=&quot;file&quot;
      multiple
      accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document,text/plain,image/png,image/jpeg,image/gif,image/svg+xml&quot;
    &gt;
    &lt;br&gt;&lt;br&gt;
    &lt;button type=&quot;submit&quot;&gt;Upload&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Upload Files&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
    &lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;
    &lt;input
      type=&quot;file&quot;
      id=&quot;files&quot;
      name=&quot;files[]&quot;
      multiple
      accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;
    &gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input id=&quot;upload-files&quot; name=&quot;files[]&quot; type=&quot;file&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;uploadForm&quot; action=&quot;#&quot; method=&quot;post&quot; enctype=&quot;multipart/form-data&quot;&gt;
  &lt;div&gt;
    &lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;
    &lt;input
      id=&quot;files&quot;
      name=&quot;files&quot;
      type=&quot;file&quot;
      multiple
      accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg,image/svg+xml&quot;
      aria-describedby=&quot;fileHelp fileList&quot;
      required
    /&gt;
    &lt;small id=&quot;fileHelp&quot;&gt;Accepted types: PDF, DOCX, TXT, PNG, JPG, GIF, SVG&lt;/small&gt;
  &lt;/div&gt;

  &lt;div aria-live=&quot;polite&quot; aria-atomic=&quot;true&quot;&gt;
    &lt;p id=&quot;fileList&quot; role=&quot;list&quot; aria-label=&quot;Selected files&quot;&gt;&lt;/p&gt;
  &lt;/div&gt;

  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const input = document.getElementById(&#x27;files&#x27;);
    const list = document.getElementById(&#x27;fileList&#x27;);

    function humanFileSize(bytes) {
      const thresh = 1024;
      if (Math.abs(bytes) &lt; thresh) return bytes + &#x27; B&#x27;;
      const units = [&#x27;KB&#x27;, &#x27;MB&#x27;, &#x27;GB&#x27;, &#x27;TB&#x27;];
      let u = -1;
      do {
        bytes /= thresh;
        ++</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;upload-files&quot;&gt;Upload Files:&lt;/label&gt;
  &lt;input type=&quot;file&quot; id=&quot;upload-files&quot; name=&quot;files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;files&quot;&gt;Upload Files&lt;/label&gt;
  &lt;input type=&quot;file&quot; id=&quot;files&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
  &lt;input id=&quot;upload-files&quot; type=&quot;file&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input id=&quot;upload-files&quot; name=&quot;files&quot; type=&quot;file&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
  &lt;p id=&quot;upload-files-instructions&quot;&gt;Select one or more files (PDF, DOCX, TXT, PNG, JPG, GIF, SVG).&lt;/p&gt;
  &lt;input type=&quot;file&quot; id=&quot;upload-files&quot; name=&quot;upload-files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot; multiple aria-describedby=&quot;upload-files-instructions&quot;&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;upload_files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; name=&quot;files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot; multiple&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Upload Files&lt;/legend&gt;
  &lt;label for=&quot;file-upload&quot;&gt;
    Choose files to upload (PDF, DOCX, TXT, PNG, JPG, GIF, SVG)
  &lt;/label&gt;
  &lt;input 
    type=&quot;file&quot; 
    id=&quot;file-upload&quot; 
    name=&quot;files&quot; 
    accept=&quot;.pdf,.docx,.txt,.png,.jpg,.jpeg,.gif,.svg&quot; 
    multiple 
    aria-describedby=&quot;file-upload-help&quot;
  &gt;
  &lt;div id=&quot;file-upload-help&quot;&gt;
    You can select multiple files. Supported formats: PDF, DOCX, TXT, PNG, JPG, GIF, SVG.
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;upload-files&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Multiple file upload field: Upload Files accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;file&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A multiple file upload field labeled “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;upload-files&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;upload-files&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a multiple file upload field and label for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;fileInput&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;fileInput&quot; multiple accept=&quot;application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document,text/plain,image/png,image/jpeg,image/gif,image/svg+xml&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible multiple file upload field for “Upload Files” accepting .pdf, .docx, .txt, .png, .jpg, .gif, .svg</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;file-upload&quot;&gt;Upload Files&lt;/label&gt;
&lt;input type=&quot;file&quot; id=&quot;file-upload&quot; name=&quot;files&quot; multiple accept=&quot;.pdf,.docx,.txt,.png,.jpg,.gif,.svg&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/multiple-file-upload-field/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
