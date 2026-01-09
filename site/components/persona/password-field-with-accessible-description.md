---
title: "password-field-with-accessible-description"
slug: password-field-with-accessible-description
track: persona
kind: component
order: 23
---

<details>
  <summary><strong>Password Field with Accessible Description</strong></summary>
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
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;newPassword&quot; name=&quot;newPassword&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/anthropic-claude-sonnet-4.5/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/anthropic-claude-sonnet-4.5/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;div id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/anthropic-claude-sonnet-4.5/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/anthropic-claude-sonnet-4.5/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input 
    type=&quot;password&quot; 
    id=&quot;new-password&quot; 
    name=&quot;new-password&quot; 
    aria-describedby=&quot;new-password-requirements&quot;
    required
  &gt;
  &lt;div id=&quot;new-password-requirements&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/anthropic-claude-sonnet-4.5/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; placeholder=&quot;New password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/deepseek-deepseek-chat-v3.1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; placeholder=&quot;New password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;span id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/span&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/deepseek-deepseek-chat-v3.1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
  &lt;small id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/deepseek-deepseek-chat-v3.1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;p id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/deepseek-deepseek-chat-v3.1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-requirements&quot;&gt;
&lt;div id=&quot;password-requirements&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/deepseek-deepseek-chat-v3.1/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/google-gemini-2.5-pro/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new_password&quot; aria-describedby=&quot;password-hint&quot;&gt;
  &lt;small id=&quot;password-hint&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/google-gemini-2.5-pro/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-hint&quot;&gt;
  &lt;p id=&quot;password-hint&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/google-gemini-2.5-pro/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
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
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/google-gemini-2.5-pro/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; autocomplete=&quot;new-password&quot; aria-describedby=&quot;password-hint&quot; required&gt;
  &lt;p id=&quot;password-hint&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/google-gemini-2.5-pro/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>minimax/minimax-m2</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html lang=&quot;en&quot;&gt;
&lt;head&gt;
  &lt;meta charset=&quot;UTF-8&quot;&gt;
  &lt;title&gt;Password Field Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;form&gt;
    &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
    &lt;input id=&quot;new-password&quot; name=&quot;new_password&quot; type=&quot;password&quot; required pattern=&quot;.*[0-9].*[^A-Za-z0-9].*&quot; aria-describedby=&quot;password-note&quot;&gt;
    &lt;small id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;
    &lt;button type=&quot;submit&quot;&gt;Submit&lt;/button&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/minimax-minimax-m2/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input
  id=&quot;newPassword&quot;
  name=&quot;newPassword&quot;
  type=&quot;password&quot;
  required
  pattern=&quot;^(?=.*\d)(?=.*\W).+$&quot;
  title=&quot;Must include 1 number and 1 symbol.&quot;
  aria-describedby=&quot;passwordNote&quot;
  autocomplete=&quot;new-password&quot;
  placeholder=&quot;Enter new password&quot;
/&gt;
&lt;div id=&quot;passwordNote&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/minimax-minimax-m2/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;new-password&quot; name=&quot;new-password&quot; type=&quot;password&quot; required pattern=&quot;(?=.*\d)(?=.*[\W_]).+&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;small id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/minimax-minimax-m2/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input
  id=&quot;new-password&quot;
  name=&quot;new-password&quot;
  type=&quot;password&quot;
  required
  pattern=&quot;(?=.*\d)(?=.*\W).+&quot;
  title=&quot;Must include 1 number and 1 symbol.&quot;
  autocomplete=&quot;new-password&quot;
  aria-describedby=&quot;password-note&quot;
/&gt;
&lt;small id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/minimax-minimax-m2/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;newPassword&quot;&gt;New password&lt;/label&gt;
&lt;input
  type=&quot;password&quot;
  id=&quot;newPassword&quot;
  name=&quot;new-password&quot;
  autocomplete=&quot;new-password&quot;
  required
  aria-describedby=&quot;newPasswordHelp&quot;
  pattern=&quot;^(?=.*\d)(?=.*[!\&quot;#$%&amp;&#x27;()*+,\-.\/:;&lt;=&gt;?@\[\\\]^_`{|}~]).+$&quot;
  title=&quot;Must include at least 1 number and 1 symbol.&quot;
/&gt;
&lt;p id=&quot;newPasswordHelp&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/minimax-minimax-m2/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5.1-codex</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
&lt;p&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/openai-gpt-5.1-codex/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;form&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot; /&gt;
  &lt;div id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;
&lt;/form&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/openai-gpt-5.1-codex/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;p id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/openai-gpt-5.1-codex/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input id=&quot;new-password&quot; type=&quot;password&quot; /&gt;
&lt;p&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/openai-gpt-5.1-codex/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;p id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/openai-gpt-5.1-codex/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; name=&quot;new_password&quot; placeholder=&quot;New password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/qwen-qwen3-coder/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/qwen-qwen3-coder/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;div&gt;
  &lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
  &lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
  &lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/qwen-qwen3-coder/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot; required&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/qwen-qwen3-coder/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;password-requirements&quot; required&gt;
&lt;div id=&quot;password-requirements&quot;&gt;Must include 1 number and 1 symbol.&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/qwen-qwen3-coder/g5.html">Open HTML</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/x-ai-grok-code-fast-1/g1.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Password field: New password with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; name=&quot;new-password&quot;&gt;
&lt;p class=&quot;note&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/x-ai-grok-code-fast-1/g2.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>A password field labeled “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;small id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/x-ai-grok-code-fast-1/g3.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Build a password field and label for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot;&gt;
&lt;small&gt;Must include 1 number and 1 symbol.&lt;/small&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/x-ai-grok-code-fast-1/g4.html">Open HTML</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible password field for “New password” with note “Must include 1 number and 1 symbol.”</td>
      <td>
        <details>
          <summary>View code</summary>
          <pre><code class="language-html">&lt;label for=&quot;new-password&quot;&gt;New password&lt;/label&gt;
&lt;input type=&quot;password&quot; id=&quot;new-password&quot; aria-describedby=&quot;password-note&quot;&gt;
&lt;p id=&quot;password-note&quot;&gt;Must include 1 number and 1 symbol.&lt;/p&gt;</code></pre>
        </details>
      </td>
      <td><a href="docs/persona-outputs/password-field-with-accessible-description/x-ai-grok-code-fast-1/g5.html">Open HTML</a></td>
    </tr>
  </tbody>
</table>

</details>

