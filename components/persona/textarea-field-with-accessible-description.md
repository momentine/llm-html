<details>
  <summary><strong>Textarea Field with Accessible Description</strong></summary>
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
      <td>Insert a textarea field for “Message” with note “Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Message Field&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message &lt;span aria-hidden=&quot;true&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
    &lt;textarea
      id=&quot;message&quot;
      name=&quot;message&quot;
      rows=&quot;6&quot;
      required
      aria-describedby=&quot;message-note&quot;
    &gt;&lt;/textarea&gt;
    &lt;small id=&quot;message-note&quot;&gt;Please describe your problem in as much detail as possible.&lt;/small&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Textarea field: Message with note “Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Contact Form&lt;/title&gt;
  &lt;style&gt;
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 0; padding: 2rem; background: #f8f9fa; color: #212529; }
    .form-field { max-width: 700px; margin: 0 auto; }
    label { display: block; font-weight: 600; margin-bottom: 0.5rem; }
    textarea { width: 100%; min-height: 160px; padding: 0.75rem; border: 1px solid #ced4da; border-radius: 6px; font: inherit; resize: vertical; }
    textarea:focus { outline: none; border-color: #0d6efd; box-shadow: 0 0 0 3px rgba(13,110,253,.15); }
    .form-note { display: block; margin-top: 0.5rem; color: #6c757d; }
    button { margin-top: 1rem; padding: 0.6rem 1rem; border: 1px solid #0d6efd; background: #0d6efd; color: #fff; border-radius: 6px; font: inherit; cursor: pointer; }
    button:hover { background: #0b5ed7; border-color: #0b5ed7; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot; class=&quot;form-field&quot; novalidate&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea id=&quot;message&quot; name=&quot;message&quot; required aria-describedby=&quot;message-note&quot; placeholder=&quot;Type your message...&quot;&gt;&lt;/textarea&gt;
    &lt;small id=&quot;message-note&quot; class=&quot;form-note&quot;&gt;Please describe your problem in as much detail as possible.&lt;/small&gt;
    &lt;button type=&quot;submit&quot;&gt;Send&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A textarea field labeled “Message” with note “Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; placeholder=&quot;Please describe your problem in as much detail as possible.&quot; required aria-describedby=&quot;message-note&quot;&gt;&lt;/textarea&gt;
&lt;small id=&quot;message-note&quot;&gt;Please describe your problem in as much detail as possible.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a textarea field and label for “Message” with note “Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
&lt;textarea id=&quot;message&quot; name=&quot;message&quot; rows=&quot;5&quot; aria-describedby=&quot;message-note&quot;&gt;&lt;/textarea&gt;
&lt;p id=&quot;message-note&quot;&gt;Please describe your problem in as much detail as possible.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible textarea field for “Message” with note “Please describe your problem in as much detail as possible.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Accessible Message Textarea&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form action=&quot;#&quot; method=&quot;post&quot;&gt;
    &lt;label for=&quot;message&quot;&gt;Message&lt;/label&gt;
    &lt;textarea
      id=&quot;message&quot;
      name=&quot;message&quot;
      rows=&quot;6&quot;
      required
      aria-describedby=&quot;message-note&quot;
      placeholder=&quot;Please describe your problem in as much detail as possible.&quot;
    &gt;&lt;/textarea&gt;
    &lt;p id=&quot;message-note&quot;&gt;Please describe your problem in as much detail as possible.&lt;/p&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/textarea-field-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
