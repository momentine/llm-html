<details>
  <summary><strong>Radio Group with Validation Error</strong></summary>
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
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;theme-form&quot; novalidate&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;

  &lt;p id=&quot;theme-error&quot; class=&quot;error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;You must choose a theme to proceed&lt;/p&gt;

  &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;theme-form&#x27;);
    const errorEl = document.getElementById(&#x27;theme-error&#x27;);

    function showError(msg) {
      errorEl.textContent = msg;
      errorEl.hidden = false;
    }

    function clearError() {
      errorEl.hidden = true;
    }

    form.addEventListener(&#x27;submit&#x27;, function (e) {
      const selected = form.querySelector(&#x27;input[name=&quot;theme&quot;]:checked&#x27;);
      if (!selected) {
        e.preventDefault();
        showError(&#x27;You must choose a theme to proceed&#x27;);
      } else {
        clearError();
      }
    });

    form.addEventListener(&#x27;change&#x27;, function () {
      const anyChecked = form.querySelector(&#x27;input[name=&quot;theme&quot;]:checked&#x27;);
      if (anyChecked) clearError();
    });
  })();
&lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;/&gt;
  &lt;title&gt;Theme Selection&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;themeForm&quot; novalidate&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;Theme&lt;/legend&gt;
      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; required /&gt;
        Light
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; required /&gt;
        Dark
      &lt;/label&gt;
      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; required /&gt;
        High contrast
      &lt;/label&gt;
    &lt;/fieldset&gt;

    &lt;p id=&quot;themeError&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #b00020; margin-top: 8px;&quot;&gt;&lt;/p&gt;

    &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;themeForm&#x27;);
      const errorEl = document.getElementById(&#x27;themeError&#x27;);
      const radios = form.querySelectorAll(&#x27;input[name=&quot;theme&quot;]&#x27;);
      const ERROR_MESSAGE = &#x27;You must choose a theme to proceed&#x27;;

      function hasSelection() {
        return Array.from(radios).some(r =&gt; r.checked);
      }

      function showError() {
        errorEl.textContent = ERROR_MESSAGE;
      }

      function clearError() {
        errorEl.textContent = &#x27;&#x27;;
      }

      radios.forEach(r =&gt; {
        r.addEventListener(&#x27;change&#x27;, () =&gt; {
          if (hasSelection()) clearError();
        });
      });

      form.addEventListener(&#x27;submit&#x27;, (e) =&gt; {
        if (!hasSelection()) {
          e.preventDefault();
          showError();
          const first = radios[0];
          if (first &amp;&amp; typeof first.focus === &#x27;function</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;themeForm&quot; novalidate&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; /&gt;
      &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot; /&gt;
      &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; /&gt;
      &lt;label for=&quot;theme-contrast&quot;&gt;High contrast&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;

  &lt;div id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; hidden&gt;
    You must choose a theme to proceed.
  &lt;/div&gt;

  &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;themeForm&#x27;);
    const errorEl = document.getElementById(&#x27;theme-error&#x27;);
    const radios = form.querySelectorAll(&#x27;input[name=&quot;theme&quot;]&#x27;);

    function getSelected() {
      return form.querySelector(&#x27;input[name=&quot;theme&quot;]:checked&#x27;);
    }

    function showError() {
      errorEl.hidden = false;
      radios.forEach(r =&gt; {
        r.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;);
        r.setAttribute(&#x27;aria-describedby&#x27;, &#x27;theme-error&#x27;);
      });
    }

    function clearError() {
      errorEl.hidden = true;
      radios.forEach(r =&gt; {
        r.removeAttribute(&#x27;aria-invalid&#x27;);
        r.removeAttribute(&#x27;aria-describedby&#x27;);
      });
    }

    radios.forEach(r =&gt; {
      r.addEventListener(&#x27;change&#x27;, clearError);
    });

    form.addEventListener(&#x27;submit&#x27;, (e) =&gt; {
      if (!getSelected()) {
        e.prevent</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form id=&quot;theme-form&quot;&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt; Light&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High contrast&lt;/label&gt;
    &lt;div class=&quot;error&quot; id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;&lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;

&lt;script&gt;
  (function () {
    const form = document.getElementById(&#x27;theme-form&#x27;);
    const radios = Array.from(form.querySelectorAll(&#x27;input[name=&quot;theme&quot;]&#x27;));
    const errorEl = document.getElementById(&#x27;theme-error&#x27;);
    const customMessage = &#x27;You must choose a theme to proceed&#x27;;

    function updateError() {
      const checked = radios.some(r =&gt; r.checked);
      if (checked) {
        errorEl.textContent = &#x27;&#x27;;
        radios.forEach(r =&gt; r.setCustomValidity(&#x27;&#x27;));
      }
    }

    radios.forEach(r =&gt; r.addEventListener(&#x27;change&#x27;, updateError));

    form.addEventListener(&#x27;submit&#x27;, function (e) {
      const checked = radios.some(r =&gt; r.checked);</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Accessible Theme Radio Group&lt;/title&gt;
  &lt;style&gt;
    :root {
      --error: #b00020;
      --border: #d0d7de;
      --focus: #0a84ff;
    }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.5; padding: 2rem; }
    fieldset { border: 1px solid var(--border); padding: 1rem; border-radius: 8px; }
    legend { font-weight: 600; padding: 0 .25rem; }
    .options { display: flex; gap: 1rem; flex-wrap: wrap; margin-top: .5rem; }
    .error { color: #fff; background: var(--error); padding: .5rem .75rem; border-radius: 6px; margin-top: .75rem; }
    .error[hidden] { display: none; }
    input[type=&quot;radio&quot;]:focus-visible + label { outline: 2px solid var(--focus); outline-offset: 2px; }
    .invalid { border-color: var(--error); }
    button { margin-top: 1rem; padding: .6rem 1rem; border-radius: 6px; border: 1px solid var(--border); background: #f6f8fa; cursor: pointer; }
    button:hover { background: #eef1f4; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;theme-form&quot; novalidate&gt;
    &lt;fieldset id=&quot;theme</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/radio-group-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
