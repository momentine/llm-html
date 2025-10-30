# LLM Generated HTML Form Compoents Output 
Each form component functions as a test case.
Every test case includes five prompt variants, each following a distinct grammar pattern but requesting the same underlying behavior.

## Universal Prompt 
You are an AI coding assistant.
Respond with semantic HTML code only.
Do not include explanations, comments, CSS, JavaScript, or code fences.
Assume the snippet will be inserted directly into an existing HTML document.

## Grammar variants (used across every test)
The same component prompt is phrased in five grammatical styles to test LLM sensitivity to wording differences.

| **ID** | **Tag**                       | **Grammar Pattern**                 | **Real-World Developer Voice**                                                                                         | **Structure Template**              |
| ------ | ----------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **G1** | **Action Command**            | Instructional or directive phrasing | Direct instruction style, used when developers issue explicit build commands to an AI tool or code assistant.          | *Insert a ___ for “Label”*          |
| **G2** | **Short Specification**       | Concise, label-like statement       | Shorthand phrasing developers use in prototyping, quick notes, or configuration-style prompts.                         | *Text field: Label*                 |
| **G3** | **Descriptive Object Phrase** | Declarative component description   | Natural descriptive phrasing resembling how developers describe an interface element to another person or review tool. | *A ___ labeled “Label”*             |
| **G4** | **Build Instruction**         | Explicit construction phrasing      | Typical of co-creative prompting where developers ask the AI to build and wire up both the element and its label.      | *Build a ___ and label for “Label”* |
| **G5** | **Accessibility Request**     | Accessibility-focused phrasing      | Indicates explicit intent for accessible markup or inclusive design considerations.                                    | *Accessible ___ for “Label”*        |

## Components 

<details>
  <summary><strong>Text Field</strong></summary>

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
      <td><strong>openai/gpt-5</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;div class="toggle-container"&gt;
  &lt;label for="dark-mode-toggle" class="toggle-label"&gt;
    Dark Mode
    &lt;div class="toggle-switch"&gt;
      &lt;input type="checkbox" id="dark-mode-toggle" class="toggle-input"&gt;
      &lt;span class="toggle-slider"&gt;&lt;/span&gt;
    &lt;/div&gt;
  &lt;/label&gt;
  &lt;p class="helper-text"&gt;Switch between light and dark themes.&lt;/p&gt;
&lt;/div&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-code-fast-1</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-code-fast-1/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-code-fast-1/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-code-fast-1/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-code-fast-1/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-code-fast-1/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>anthropic/claude-sonnet-4.5</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4.5/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4.5/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4.5/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4.5/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4.5/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>anthropic/claude-sonnet-4</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-sonnet-4/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder-30b-a3b-instruct</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-oss-20b</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-oss-20b/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-oss-20b/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-oss-20b/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-oss-20b/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-oss-20b/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-4.1-mini</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-4.1-mini/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-4.1-mini/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-4.1-mini/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-4.1-mini/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-4.1-mini/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>z-ai/glm-4.6</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.6/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.6/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.6/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.6/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.6/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-4-fast</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4-fast/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4-fast/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4-fast/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4-fast/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4-fast/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>google/gemma-3-12b-it</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemma-3-12b-it/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemma-3-12b-it/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemma-3-12b-it/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemma-3-12b-it/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemma-3-12b-it/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-flash</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-flash/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-flash/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-flash/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-flash/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-flash/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>google/gemini-2.5-pro</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-pro/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-pro/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-pro/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-pro/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/google-gemini-2.5-pro/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5-codex</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-codex/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-codex/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-codex/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-codex/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-codex/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-coder</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-coder/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>z-ai/glm-4.5-air</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.5-air/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.5-air/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.5-air/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.5-air/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/z-ai-glm-4.5-air/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>deepseek/deepseek-chat-v3.1</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/deepseek-deepseek-chat-v3.1/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/deepseek-deepseek-chat-v3.1/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/deepseek-deepseek-chat-v3.1/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/deepseek-deepseek-chat-v3.1/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/deepseek-deepseek-chat-v3.1/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>qwen/qwen3-vl-235b-a22b-instruct</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>anthropic/claude-3.7-sonnet</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-3.7-sonnet/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-3.7-sonnet/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-3.7-sonnet/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-3.7-sonnet/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/anthropic-claude-3.7-sonnet/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>x-ai/grok-4</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/x-ai-grok-4/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td><strong>openai/gpt-5-mini</strong></td>
      <td>G1</td>
      <td>Insert a field to respond to the question “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-mini/g1.html">g1.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G2</td>
      <td>Text field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G2 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-mini/g2.html">g2.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G3</td>
      <td>Field: What color is an orange?</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G3 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-mini/g3.html">g3.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G4</td>
      <td>Field and label for “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G4 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-mini/g4.html">g4.html</a></td>
    </tr>
    <tr>
      <td></td>
      <td>G5</td>
      <td>Accessible field to answer “What color is an orange?”</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G5 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5-mini/g5.html">g5.html</a></td>
    </tr>
    <tr>
      <td>test </td>
      <td>G1</td>
      <td>test</td>
      <td>
        <details>
          <summary>View HTML code</summary>
          <pre><code class="language-html">&lt;!-- G1 output here --&gt;</code></pre>
        </details>
      </td>
      <td><a href="outputs/text-field/openai-gpt-5/g5.html">g5.html</a></td>
    </tr>
  </tbody>
</table>

</details>

