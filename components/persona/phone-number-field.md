<details>
  <summary><strong>Phone Number Field</strong></summary>
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
      <td>Insert a phone number field for “Phone number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;phone&quot;&gt;Phone number&lt;/label&gt;
&lt;input type=&quot;tel&quot; id=&quot;phone&quot; name=&quot;phone&quot; placeholder=&quot;(555) 123-4567&quot; required&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/phone-number-field/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Phone number field: Phone number</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;phone&quot;&gt;Phone number&lt;/label&gt;
&lt;input
  id=&quot;phone&quot;
  name=&quot;phone&quot;
  type=&quot;tel&quot;
  inputmode=&quot;tel&quot;
  autocomplete=&quot;tel&quot;
  placeholder=&quot;+1 555 123 4567&quot;
  pattern=&quot;^\+?[0-9\s\-\.()]{7,20}$&quot;
  title=&quot;Enter a valid phone number&quot;
  required
/&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/phone-number-field/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A phone number field labeled “Phone number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;phone&quot;&gt;Phone number&lt;/label&gt;
&lt;input
  type=&quot;tel&quot;
  id=&quot;phone&quot;
  name=&quot;phone&quot;
  placeholder=&quot;+1 (555) 123-4567&quot;
  autocomplete=&quot;tel&quot;
  inputmode=&quot;tel&quot;
  pattern=&quot;^\+?[0-9\s\-()]{7,20}$&quot;
  aria-describedby=&quot;phone-hint&quot;
/&gt;
&lt;small id=&quot;phone-hint&quot;&gt;Use numbers, spaces, dashes, parentheses, and an optional leading +.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/phone-number-field/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a phone number field and label for “Phone number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot;&gt;
  &lt;title&gt;Phone number field&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;label for=&quot;phone&quot;&gt;Phone number&lt;/label&gt;
  &lt;input type=&quot;tel&quot; id=&quot;phone&quot; name=&quot;phone&quot; autocomplete=&quot;tel&quot; inputmode=&quot;tel&quot; placeholder=&quot;(555) 123-4567&quot; pattern=&quot;^\+?[0-9\s\-()]{7,20}$&quot; required aria-describedby=&quot;phone-hint&quot;&gt;
  &lt;small id=&quot;phone-hint&quot;&gt;Include country code if outside your region.&lt;/small&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/phone-number-field/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible phone number field for “Phone number”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;title&gt;Accessible Phone Number Field&lt;/title&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;contact-form&quot; action=&quot;#&quot; method=&quot;post&quot; novalidate&gt;
    &lt;div&gt;
      &lt;label for=&quot;phone&quot;&gt;Phone number &lt;span aria-hidden=&quot;true&quot;&gt;*&lt;/span&gt;&lt;/label&gt;
      &lt;input
        id=&quot;phone&quot;
        name=&quot;phone&quot;
        type=&quot;tel&quot;
        inputmode=&quot;tel&quot;
        autocomplete=&quot;tel&quot;
        placeholder=&quot;+1 (555) 123-4567&quot;
        required
        aria-required=&quot;true&quot;
        aria-describedby=&quot;phone-hint phone-error&quot;
        pattern=&quot;^\+?[\d\s().-]{7,}$&quot;
        maxlength=&quot;25&quot;
      /&gt;
      &lt;div id=&quot;phone-hint&quot;&gt;Use numbers and optional +, space, or -(). Example: +1 555-123-4567&lt;/div&gt;
      &lt;div id=&quot;phone-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;

    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/phone-number-field/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
