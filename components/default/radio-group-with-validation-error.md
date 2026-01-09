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
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div role=&quot;radiogroup&quot; aria-required=&quot;true&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High Contrast
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;span id=&quot;theme-error&quot; role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/span&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div role=&quot;radiogroup&quot; aria-required=&quot;true&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High Contrast
    &lt;/label&gt;
  &lt;/div&gt;
  &lt;div id=&quot;theme-error&quot; role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div role=&quot;radiogroup&quot; aria-labelledby=&quot;theme-label&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      &lt;label for=&quot;light&quot;&gt;light&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      &lt;label for=&quot;dark&quot;&gt;dark&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      &lt;label for=&quot;high-contrast&quot;&gt;high contrast&lt;/label&gt;
    &lt;/div&gt;
  &lt;/div&gt;
  &lt;div id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/div&gt;
  &lt;div role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;meta charset=&quot;UTF-8&quot;&gt;
    &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;
    &lt;title&gt;Theme Selection&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset role=&quot;radiogroup&quot; aria-required=&quot;true&quot; aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
        &lt;legend&gt;Theme&lt;/legend&gt;
        &lt;div&gt;
            &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
            &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
            &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
        &lt;/div&gt;
        &lt;div&gt;
            &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
            &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
        &lt;/div&gt;
        &lt;div id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;assertive&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
    &lt;/fieldset&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;high contrast&lt;/label&gt;
  &lt;/div&gt;
&lt;/fieldset&gt;
&lt;div style=&quot;color: red; display: none;&quot; id=&quot;theme-error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;div style=&quot;color: red; display: none;&quot; id=&quot;theme-error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;high contrast&lt;/label&gt;
  &lt;/div&gt;
  &lt;div style=&quot;color: red; font-size: 0.875rem;&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;&lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;&lt;label for=&quot;light&quot;&gt;light&lt;/label&gt;&lt;/div&gt;
  &lt;div&gt;&lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;&lt;label for=&quot;dark&quot;&gt;dark&lt;/label&gt;&lt;/div&gt;
  &lt;div&gt;&lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt;&lt;label for=&quot;high-contrast&quot;&gt;high contrast&lt;/label&gt;&lt;/div&gt;
  &lt;div&gt;&lt;span style=&quot;color: red; font-size: 0.875em;&quot;&gt;You must choose a theme to proceed&lt;/span&gt;&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;theme-error&quot;&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div role=&quot;alert&quot; id=&quot;theme-error&quot; aria-live=&quot;assertive&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;theme-high-contrast&quot;&gt;High contrast&lt;/label&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Theme Selector&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
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
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
    &lt;title&gt;Radio Group Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;fieldset aria</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-describedby=&quot;theme-error&quot;&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/div&gt;
  &lt;div id=&quot;theme-error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot; /&gt;
  &lt;title&gt;Theme Selection&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;themeForm&quot; novalidate&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;Theme&lt;/legend&gt;

      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; /&gt;
        Light
      &lt;/label&gt;

      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; /&gt;
        Dark
      &lt;/label&gt;

      &lt;label&gt;
        &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; /&gt;
        High contrast
      &lt;/label&gt;

      &lt;p id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #b00020; margin-top: 8px; display: none;&quot;&gt;
        You must choose a theme to proceed
      &lt;/p&gt;
    &lt;/fieldset&gt;

    &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;
  &lt;/form&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;themeForm&#x27;);
      const errorEl = document.getElementById(&#x27;theme-error&#x27;);

      function getSelectedTheme() {
        const checked = form.querySelector(&#x27;input[name=&quot;theme&quot;]:checked&#x27;);
        return checked ? checked.value : null;
      }

      function showError() {
        errorEl.style.display = &#x27;block&#x27;;
        errorEl.textContent = &#x27;You must choose a theme to proceed&#x27;;
      }

      function hideError() {
        errorEl.style.display = &#x27;none&#x27;;
        errorEl.textContent = &#x27;&#x27;;
      }

      form.addEventListener(&#x27;change&#x27;, (e) =&gt; {
        if (e.target.name === &#x27;theme&#x27;) hideError();
      });

      form.addEventListener(&#x27;submit&#x27;, (e) =&gt; {
        e.preventDefault();
        const theme = getSelectedTheme();

        if (!theme) {
          showError();
          return;
        }

        hideError();
        alert(&#x27;Selected theme: &#x27; + theme);
        // Proceed with submission or next step here.
      });
    })();
  &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!doctype html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;utf-8&quot; /&gt;
  &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,initial-scale=1&quot; /&gt;
  &lt;title&gt;Theme Radio Group&lt;/title&gt;
  &lt;style&gt;
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; line-height: 1.4; margin: 2rem; }
    fieldset { border: 1px solid #ccc; padding: 1rem; border-radius: 8px; max-width: 420px; }
    legend { font-weight: 600; }
    .options { display: grid; gap: .5rem; margin-top: .5rem; }
    .error { color: #b00020; margin-top: .75rem; }
    .success { color: #0a7a0a; margin-top: .75rem; }
    .actions { margin-top: 1rem; }
    button { padding: .6rem 1rem; border-radius: 6px; border: 1px solid #888; cursor: pointer; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form id=&quot;themeForm&quot; novalidate&gt;
    &lt;fieldset&gt;
      &lt;legend&gt;Theme&lt;/legend&gt;
      &lt;div class=&quot;options&quot;&gt;
        &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
        &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High contrast&lt;/label&gt;
      &lt;/div&gt;

      &lt;p id=&quot;themeError&quot; class=&quot;error&quot; role=&quot;alert&quot; hidden&gt;You must choose a theme to proceed&lt;/p&gt;
      &lt;p id=&quot;themeSuccess&quot; class=&quot;success&quot; role=&quot;status&quot; hidden&gt;&lt;/p&gt;

      &lt;div class=&quot;actions&quot;&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; required&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; required&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;

  &lt;div role=&quot;alert&quot; aria-live=&quot;polite&quot;&gt;
    &lt;input type=&quot;checkbox&quot; name=&quot;confirm_theme&quot; required aria-hidden=&quot;true&quot; tabindex=&quot;-1&quot; style=&quot;display:none&quot;&gt;
    &lt;span class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/span&gt;
  &lt;/div&gt;

  &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
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
    &lt;div id=&quot;theme-error&quot; role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color:#b00020; margin-top:8px; display:none;&quot;&gt;
      You must choose a theme to proceed
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;button type=&quot;submit&quot;&gt;Continue&lt;/button&gt;

  &lt;script&gt;
    (function () {
      const form = document.getElementById(&#x27;theme-form&#x27;);
      const errorEl = document.getElementById(&#x27;theme-error&#x27;);
      const radios = form.querySelectorAll(&#x27;input[name=&quot;theme&quot;]&#x27;);

      function showError() {
        errorEl.style.display = &#x27;block&#x27;;
        radios.forEach(r =&gt; r.setAttribute(&#x27;aria-invalid&#x27;, &#x27;true&#x27;));
      }

      function clearError() {
        errorEl.style.display = &#x27;none&#x27;;
        radios.forEach(r =&gt; r.removeAttribute(&#x27;aria-invalid&#x27;));
      }

      radios.forEach(r =&gt; r.addEventListener(&#x27;change&#x27;, clearError));

      form.addEventListener(&#x27;submit&#x27;, (e) =&gt; {
        const selected = form.querySelector(&#x27;input[name=&quot;theme&quot;]:checked&#x27;);
        if (!selected) {
          e.preventDefault();
          showError();
          const first = radios[0];
          if (first) first.focus();
        } else {
          clearError();
          // Example: proceed with selected value
          // alert(&#x27;Selected theme: &#x27; + selected.value);
        }
      });
    })();
  &lt;/script&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/minimax-minimax-m2/g4.html">Open HTML</a></td>
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
    :root { color-scheme: light dark; }
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif; line-height: 1.5; padding: 2rem; }
    fieldset { border: 1px solid #ccc; padding: 1rem; border-radius: 8px; }
    legend { font-weight: 600; }
    .options { display: grid; gap: .5rem; margin-top: .5rem; }
    .error { color: #b00020; margin-top: .5rem; }
    .error[hidden] { display: none; }
    .visually-hidden { position: absolute !important; height: 1px; width: 1px; overflow: hidden; clip: rect(1px, 1px, 1px, 1px); white-space: nowrap; }
    button { margin-top: 1rem; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Choose your theme&lt;/h1&gt;

  &lt;form id=&quot;theme-form&quot; novalidate&gt;
    &lt;fieldset id=&quot;theme-fieldset&quot; role=&quot;radiogroup&quot; aria-labelledby=&quot;theme-legend theme-error&quot; aria-describedby=&quot;theme-error&quot;&gt;
      &lt;legend id=&quot;theme-legend&quot;&gt;Theme&lt;/legend&gt;

      &lt;div class=&quot;options</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot; required&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; required&gt;
      High contrast
    &lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;div&gt;You must choose a theme to proceed&lt;/div&gt;
  &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
    &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High contrast&lt;/label&gt;
    &lt;p&gt;You must choose a theme to proceed&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
      Light
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
      Dark
    &lt;/label&gt;
    &lt;label&gt;
      &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
      High contrast
    &lt;/label&gt;
    &lt;p&gt;You must choose a theme to proceed&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset aria-describedby=&quot;theme-error&quot;&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt;
      &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot; required&gt;
      &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; required&gt;
      &lt;label for=&quot;theme-high-contrast&quot;&gt;High contrast&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;p id=&quot;theme-error&quot; role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset aria-invalid=&quot;true&quot; aria-describedby=&quot;theme-error&quot;&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt;
      &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot; required&gt;
      &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
    &lt;/div&gt;
    &lt;div&gt;
      &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot; required&gt;
      &lt;label for=&quot;theme-high-contrast&quot;&gt;High contrast&lt;/label&gt;
    &lt;/div&gt;
  &lt;/fieldset&gt;
  &lt;p id=&quot;theme-error&quot; role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/p&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
  &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
  &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
  &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
  &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
&lt;/fieldset&gt;
&lt;p style=&quot;color: red;&quot;&gt;You must choose a theme to proceed&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/fieldset&gt;
  &lt;div class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
  &lt;/div&gt;
  &lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;theme-high-contrast&quot;&gt;High Contrast&lt;/label&gt;
  &lt;/div&gt;
  &lt;div role=&quot;alert&quot; aria-live=&quot;polite&quot; style=&quot;color: #d32f2f; margin-top: 8px;&quot;&gt;
    You must choose a theme to proceed
  &lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot; required&gt; Light&lt;br&gt;
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;br&gt;
  &lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt; High Contrast&lt;br&gt;
  &lt;div&gt;You must choose a theme to proceed&lt;/div&gt;
&lt;/fieldset&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Radio group: Theme with options light, dark, high contrast with error message “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
    &lt;p class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A radio group labeled “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;fieldset&gt;
    &lt;legend&gt;Theme&lt;/legend&gt;
    &lt;input type=&quot;radio&quot; id=&quot;light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
    &lt;label for=&quot;light&quot;&gt;Light&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
    &lt;label for=&quot;dark&quot;&gt;Dark&lt;/label&gt;
    &lt;input type=&quot;radio&quot; id=&quot;high-contrast&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt;
    &lt;label for=&quot;high-contrast&quot;&gt;High Contrast&lt;/label&gt;
    &lt;p&gt;You must choose a theme to proceed&lt;/p&gt;
  &lt;/fieldset&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a radio group and label for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
  &lt;legend&gt;Theme&lt;/legend&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt; Light&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt; Dark&lt;/label&gt;
  &lt;label&gt;&lt;input type=&quot;radio&quot; name=&quot;theme&quot; value=&quot;high-contrast&quot;&gt; High Contrast&lt;/label&gt;
&lt;/fieldset&gt;
&lt;p class=&quot;error&quot;&gt;You must choose a theme to proceed&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible radio group for “Theme” with options light, dark, high contrast with a validation error “You must choose a theme to proceed”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;fieldset&gt;
&lt;legend&gt;Theme&lt;/legend&gt;
&lt;input type=&quot;radio&quot; id=&quot;theme-light&quot; name=&quot;theme&quot; value=&quot;light&quot;&gt;
&lt;label for=&quot;theme-light&quot;&gt;Light&lt;/label&gt;
&lt;input type=&quot;radio&quot; id=&quot;theme-dark&quot; name=&quot;theme&quot; value=&quot;dark&quot;&gt;
&lt;label for=&quot;theme-dark&quot;&gt;Dark&lt;/label&gt;
&lt;input type=&quot;radio&quot; id=&quot;theme-high-contrast&quot; name=&quot;theme&quot; value=&quot;high contrast&quot;&gt;
&lt;label for=&quot;theme-high-contrast&quot;&gt;High contrast&lt;/label&gt;
&lt;/fieldset&gt;
&lt;div class=&quot;error&quot; role=&quot;alert&quot;&gt;You must choose a theme to proceed&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="https://momentine.github.io/llm-html/default-outputs/radio-group-with-validation-error/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>
