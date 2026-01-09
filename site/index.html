<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Methods overview: how we chose models, form components, and prompts.</title>
  <style>
    :root{
      color-scheme: light;
      --bg:#ffffff;
      --surface:#f6f7f9;
      --surface2:#fbfbfc;
      --text:#111827;
      --muted:#6b7280;
      --border:#e5e7eb;
      --focus:#2563eb;
      --code-bg:#0b1020;
      --code-text:#e5e7eb;
      --shadow: 0 1px 0 rgba(0,0,0,.03), 0 10px 25px rgba(17,24,39,.06);
      --tag:#eef2ff;
      --tagtext:#3730a3;
    }
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,"Apple Color Emoji","Segoe UI Emoji";
      background: var(--bg);
      color: var(--text);
      line-height: 1.6;
    }
    a{color:inherit}
    a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{
      outline:3px solid rgba(37,99,235,.35);
      outline-offset:2px;
      border-radius:10px;
    }

    /* Top bar */
    .topbar{
      position:sticky;top:0;z-index:10;
      background: rgba(255,255,255,.92);
      backdrop-filter: blur(10px);
      border-bottom:1px solid var(--border);
    }
    .topbar-inner{
      max-width:1100px;margin:0 auto;
      padding:12px 16px;
      display:flex;gap:14px;align-items:center;justify-content:space-between;flex-wrap:wrap;
    }
    .brand{
      display:flex;flex-direction:column;gap:2px;
      text-decoration:none;
      min-width: 280px;
    }
    .brand .name{
      font-weight:850;
      letter-spacing:.2px;
      font-size:15.5px;
      margin:0;
    }
    .brand .desc{
      margin:0;
      font-size:12.5px;
      color: var(--muted);
      max-width: 62ch;
    }
    .nav{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
    .pill{
      text-decoration:none;
      border:1px solid var(--border);
      background: var(--surface);
      padding:7px 10px;
      border-radius:999px;
      font-size:13px;
      color: var(--text);
      white-space:nowrap;
    }
    .pill:hover{filter:brightness(.985)}

    /* Layout */
    .wrap{max-width:1100px;margin:18px auto 36px;padding:0 16px}
    .panel{
      border:1px solid var(--border);
      border-radius:16px;
      background: var(--bg);
      box-shadow: var(--shadow);
      overflow:hidden;
    }
    .hero{
      display:grid;
      gap:10px;
      padding:18px;
      border-bottom:1px solid var(--border);
      background: linear-gradient(180deg, var(--surface2), var(--bg));
    }
    .hero h1{margin:0;font-size:20px;letter-spacing:.1px}
    .hero p{margin:0;color:var(--muted);max-width: 90ch}
    .hero .chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:2px}
    .chip{
      display:inline-flex;align-items:center;gap:6px;
      padding:6px 10px;border-radius:999px;
      border:1px solid var(--border);
      background: var(--surface);
      font-size:12.5px;color:var(--text);
      white-space:nowrap;
    }
    .chip b{font-weight:800}

    .content{padding:18px}
    h2{margin:22px 0 8px;font-size:16px;letter-spacing:.1px}
    h3{margin:16px 0 8px;font-size:14px;letter-spacing:.1px}
    p{margin:10px 0}
    .muted{color:var(--muted)}
    .callout{
      margin:12px 0 10px;
      padding:12px 12px;
      border-radius:14px;
      background: rgba(37,99,235,.06);
      border:1px solid rgba(37,99,235,.18);
    }
    .callout p{margin:0}

    /* Step list */
    ol.steps{
      margin: 10px 0 0 18px;
      padding: 0;
    }
    ol.steps > li{
      margin: 10px 0;
      padding-left: 4px;
    }
    .tag{
      display:inline-flex;align-items:center;
      padding:2px 8px;border-radius:999px;
      background: var(--tag);
      color: var(--tagtext);
      border: 1px solid rgba(55,48,163,.18);
      font-size: 12px;
      font-weight: 800;
      vertical-align: middle;
      margin-right: 8px;
      white-space: nowrap;
    }

    /* Tables: never cut off */
    .table-wrap{
      margin-top:10px;
      border:1px solid var(--border);
      border-radius:14px;
      overflow:auto;
      background: var(--bg);
    }
    table{
      width:100%;
      border-collapse:collapse;
      font-size:13.25px;
      min-width: 860px;
    }
    thead th{
      text-align:left;
      font-size:12px;
      color:var(--muted);
      text-transform:uppercase;
      letter-spacing:.08em;
      padding:10px 10px;
      border-bottom:1px solid var(--border);
      background: rgba(0,0,0,.012);
      white-space:nowrap;
    }
    tbody td{
      vertical-align:top;
      padding:10px 10px;
      border-bottom:1px solid var(--border);
    }
    tbody tr:last-child td{border-bottom:none}
    tbody tr:hover td{background: rgba(0,0,0,.015)}
    .nowrap{white-space:nowrap}

    /* Details */
    details{
      border:1px solid var(--border);
      border-radius:14px;
      padding:10px 12px;
      background: var(--bg);
      margin:12px 0 14px;
    }
    details > summary{
      cursor:pointer;
      list-style:none;
      display:flex;align-items:center;justify-content:space-between;gap:10px;
      font-weight:900;
      font-size:13.5px;
      padding:6px 2px;
    }
    details > summary::-webkit-details-marker{display:none}
    details > summary::after{
      content:"▸";
      color:var(--muted);
      font-weight:900;
      transition:transform .12s ease;
    }
    details[open] > summary::after{transform:rotate(90deg)}

    /* Code */
    pre{
      margin:10px 0 0;
      background: var(--code-bg);
      color: var(--code-text);
      padding:12px 12px;
      border-radius:12px;
      overflow:auto;
      border:1px solid rgba(17,24,39,.22);
    }
    code{
      font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;
      font-size:12.25px;
    }
    .code-wrap{white-space:pre-wrap; word-break:break-word}

    .hr{height:1px;background:var(--border);margin:18px 0}

    @media (max-width: 640px){
      .brand{min-width:auto}
      table{min-width: 980px}
    }
    @media print{
      .topbar{display:none !important}
      .panel{box-shadow:none}
      pre{background:#f3f4f6;color:#111827;border:1px solid #e5e7eb}
    }
  </style>
</head>
<body>
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand" aria-label="Site title">
        <div class="name">LLM HTML Component Benchmark</div>
        <div class="desc">Initial Prompt Framing and Accessibility in AI Generated HTML
Form Components</div>
      </div>
      <nav class="nav" aria-label="Site">
        <a class="pill" href="/index">Overview</a>
        <a class="pill" href="/default">Default</a>
        <a class="pill" href="/guide">Standard practice</a>
        <a class="pill" href="/persona">Standard + persona</a>
      </nav>
    </div>
  </header>

  <main class="wrap">
    <section class="panel">
      <div class="hero">
        <h1>When “Just Give Me the Code” Isn’t Enough
</h1>
        <p>
         
We examine how initial prompt framing influences accessibility-related outcomes in HTML form components generated by large language models under standard, developer-facing configurations.
This section describes the benchmark design used to operationalize our research questions. These include provider and model selection, the form component set used for evaluation, and the construction of single-shot initial prompting conditions and linguistic variants
        </p>
        <div class="chips" aria-label="At a glance">
          <span class="chip"><b>7</b> providers</span>
          <span class="chip"><b>1</b> model per provider</span>
          <span class="chip"><b>58</b> form components</span>
          <span class="chip"><b>3</b> prompt conditions</span>
          <span class="chip"><b>5</b> linguistic variants</span>
        </div>
      </div>

      <div class="content">
        <h2 id="providers">Provider inclusion criteria</h2>
        <div class="callout">
          <p>
            We selected providers that independently train and deploy large language models, offer public developer-facing APIs,
            and obviously position at least one model as a default option for general-purpose code generation during the study period.
          </p>
        </div>
        <p class="muted">
          This set reflects organizations whose models are directly integrated into contemporary software development workflows.
        </p>

        <div class="hr"></div>

        <h2 id="model-selection">Model selection</h2>
        <p class="muted">
          We evaluated one model per provider. For each included provider, we selected the stable, non-experimental model most prominently designated as the default option
          for general-purpose code generation in official documentation and API examples at the time of study.
        </p>

        <details open>
          <summary>Step-by-step model selection procedure</summary>
<div class="steps">
  <p><span class="tag">Step 1</span>
    Identify eligible providers using the inclusion criteria above (independent training, public APIs, code-generation positioning).
  </p>

  <p><span class="tag">Step 2</span>
    Within each provider, list stable, actively supported candidate models with documentation confirming code generation.
  </p>

  <p><span class="tag">Step 3</span>
    Apply a realism filter using usage signals from the
    <a href="https://openrouter.ai/rankings" target="_blank" rel="noopener noreferrer">
      OpenRouter programming leaderboard
    </a>
    (Aug 25, 2025–Dec 1, 2025) and evidence of integration into developer tooling (SDKs, IDE support, announcements).
  </p>

  <p><span class="tag">Step 4</span>
    Select the model most prominently presented as the default for general-purpose code generation in official documentation and examples.
  </p>

  <p><span class="tag">Step 5</span>
    Evaluate each model using its documented default code-generation configuration. We did not enable optional reasoning/thinking, multimodal modes, or experimental features.
  </p>
</div>

        </details>

    <h3 id="evaluated-models">Evaluated providers and models</h3>
<div class="table-wrap" role="region" aria-label="Evaluated models table">
  <table>
    <thead>
      <tr>
        <th>Provider</th>
        <th>Selected model</th>
        <th>Primary documentation</th>
        <th>Selection note</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="nowrap">OpenAI</td>
        <td class="nowrap">GPT-5.1 Codex</td>
        <td>
          <a href="https://platform.openai.com/docs/models/gpt-5.1-codex" target="_blank" rel="noopener noreferrer">
            Model page
          </a>
        </td>
        <td class="muted">
          Default general-purpose code-generation model in provider documentation at the time of study.
        </td>
      </tr>

      <tr>
        <td class="nowrap">Anthropic</td>
        <td class="nowrap">Claude Sonnet 4.5</td>
        <td>
          <a href="https://www.anthropic.com/claude/sonnet" target="_blank" rel="noopener noreferrer">
            Model page
          </a>
        </td>
        <td class="muted">
          Positioned as a primary coding-capable model in official Anthropic documentation.
        </td>
      </tr>

      <tr>
        <td class="nowrap">Google</td>
        <td class="nowrap">Gemini 2.5 Pro</td>
        <td>
          <a href="https://cloud.google.com/vertex-ai/docs/generative-ai/models/gemini/2-5-pro"
             target="_blank" rel="noopener noreferrer">
            Model page
          </a>
        </td>
        <td class="muted">
          Selected based on developer-facing API documentation and usage as a general-purpose model.
        </td>
      </tr>

      <tr>
        <td class="nowrap">xAI</td>
        <td class="nowrap">Grok Fast 1</td>
        <td>
          <a href="https://docs.x.ai/docs/guides/grok-code-prompt-engineering"
             target="_blank" rel="noopener noreferrer">
            Developer guide
          </a>
        </td>
        <td class="muted">
          Documented for code-oriented prompting and positioned for programming workflows.
        </td>
      </tr>

      <tr>
        <td class="nowrap">Alibaba / Qwen</td>
        <td class="nowrap">Qwen3-Coder (480B A35B)</td>
        <td>
          <a href="https://docs.cloud.google.com/vertex-ai/generative-ai/docs/maas/qwen/qwen3-coder"
             target="_blank" rel="noopener noreferrer">
            Model documentation
          </a>
        </td>
        <td class="muted">
          Large-scale Mixture-of-Experts model explicitly described as code-generation oriented in public documentation.
        </td>
      </tr>

      <tr>
        <td class="nowrap">MiniMax</td>
        <td class="nowrap">MiniMax M2</td>
        <td>
          <a href="https://docs.api.nvidia.com/nim/reference/minimaxai-minimax-m2"
             target="_blank" rel="noopener noreferrer">
            Model documentation
          </a>
        </td>
        <td class="muted">
          Publicly documented MoE model designed for coding and agentic workflows.
        </td>
      </tr>

      <tr>
        <td class="nowrap">DeepSeek</td>
        <td class="nowrap">DeepSeek V3.1</td>
        <td>
          <a href="https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus"
             target="_blank" rel="noopener noreferrer">
            Model card
          </a>
        </td>
        <td class="muted">
          Public model documentation describing stable performance on code and agent-style tasks.
        </td>
      </tr>
    </tbody>
  </table>
</div>


        <details>
          <summary>Configuration and evaluation scope</summary>
          <p class="muted">
All models were evaluated using their documented default configurations for general-purpose code generation. When models offered optional reasoning or specialized modes, we followed the default settings recommended in official documentation or API examples. Our goal is not to measure peak coding performance, but to examine how initial prompt framing shapes accessibility-relevant HTML generation under typical developer-oriented conditions.
          </p>
        </details>

        <!-- form components SECTION STARTS HERE -->
        <div class="hr"></div>

        <h2 id="components">Form components benchmarked</h2>
        <p class="muted">
          We benchmark form components that appear repeatedly in high-traffic, real-world interfaces and are required to complete core tasks.
          This is because we want to evaluate accessibility outcomes on components users encounter frequently and depend on to make progress.
        </p>

<details open>
  <summary>Step-by-step component selection procedure</summary>

  <div class="steps">
    <p><span class="tag">Step 1</span>
      Identify high-traffic websites using publicly available metrics (e.g., Cloudflare Radar) from January 1 to December 1, 2025.
    </p>

    <p><span class="tag">Step 2</span>
      Filter to platforms where structured form input is required to complete core tasks, excluding sites where form interaction is occasional or peripheral (e.g., a single search field).
    </p>

    <p><span class="tag">Step 3</span>
      Apply three criteria: (a) forms are necessary for the primary function of the site, (b) multiple input types appear beyond free-text, and (c) form interactions recur across typical use rather than appearing only once.
    </p>

    <p><span class="tag">Step 4</span>
      Manually examine forms across retained sites and document individual input patterns.
    </p>

    <p><span class="tag">Step 5</span>
      Iteratively sample until new component types stop emerging, treating this point as an approximate saturation boundary.
    </p>

    <p><span class="tag">Step 6</span>
      Cluster the resulting component set by interaction pattern and semantic role to support interpretation.
    </p>
  </div>
</details>


        <h3 id="component-contexts">Functional contexts sampled</h3>
<div class="table-wrap" role="region" aria-label="Functional contexts sampled">
  <table>
    <thead>
      <tr>
        <th class="nowrap">Functional context</th>
        <th>Role of forms in core tasks</th>
        <th>Representative platforms</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="nowrap"><strong>E-commerce</strong></td>
        <td class="muted">
          Forms are required for checkout, payment, shipping, and account management.
        </td>
        <td class="muted">
          Amazon, Walmart, Target, Etsy, eBay
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Account creation and authentication</strong></td>
        <td class="muted">
          Multi-step workflows for login, verification, password setup, and consent.
        </td>
        <td class="muted">
          Google, Microsoft, LinkedIn, Reddit
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Survey and structured data collection</strong></td>
        <td class="muted">
          Repeated, structured input is the primary interaction throughout the interface.
        </td>
        <td class="muted">
          Google Forms, Qualtrics, Typeform
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Government and public services</strong></td>
        <td class="muted">
          Legally required submissions tied to benefits, licensing, or official records.
        </td>
        <td class="muted">
          IRS, USPS, state DMV systems
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Healthcare and financial services</strong></td>
        <td class="muted">
          High-accuracy data entry involving sensitive personal or financial information.
        </td>
        <td class="muted">
          MyChart / Kaiser, PayPal, major banks
        </td>
      </tr>
    </tbody>
  </table>
</div>

        <details>
          <summary>Resulting component set (58 components)</summary>
          <p class="muted">
            We arranged components into clusters based on shared interaction patterns and semantic role.
          </p>
<div class="table-wrap" role="region" aria-label="Benchmark form components">
  <table>
    <thead>
      <tr>
        <th class="nowrap">Component cluster</th>
        <th>Included components</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="nowrap"><strong>Text inputs</strong></td>
        <td>
          Text field; Required; Placeholder; Pattern; Autocomplete suggestion;
          Accessible description; Non-visible label; Validation error
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Email inputs</strong></td>
        <td>
          Email field; Required; Placeholder; Autocomplete suggestion;
          Accessible description; Required + autocomplete + description;
          Validation error
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Specialized single-field inputs</strong></td>
        <td>
          Credit card field; Quantity field; URL field; Search field;
          Phone number field
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Password inputs</strong></td>
        <td>
          Password field; Required; Placeholder; Autocomplete suggestion;
          Accessible description; Validation error
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Selection controls</strong></td>
        <td>
          Select field; Required; Accessible description;
          Radio group; Radio group with description; Radio group with error;
          Checkbox group; Checkbox group with description;
          Checkbox group with error; Country / state picker
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Confirmation & consent</strong></td>
        <td>
          Confirmation checkbox; Confirmation checkbox with link;
          CAPTCHA placeholder
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Multiline input</strong></td>
        <td>
          Textarea; Required; Accessible description;
          Validation error; Character counter
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>File and media input</strong></td>
        <td>
          File upload (multiple); Image upload; Document upload
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Range and switch controls</strong></td>
        <td>
          Range slider; Toggle switch; Multi-toggle
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Date and time inputs</strong></td>
        <td>
          Date field; Time field; Datetime-local field
        </td>
      </tr>

      <tr>
        <td class="nowrap"><strong>Submission and state</strong></td>
        <td>
          Submit button; Submit button with icon;
          Reset button; Disabled field; Readonly field
        </td>
      </tr>
    </tbody>
  </table>
</div>

          <p class="muted">
            Additional patterns observed in the wild were excluded when they exceeded native HTML semantics or required task-specific logic beyond the benchmark scope
            (e.g., complex phone formatting, end-to-end CAPTCHA flows, domain-specific validation pipelines).
          </p>
        </details>

        <details>
          <summary>Coverage validation against developer usage</summary>
          <p class="muted">
            We checked the component set against the <a href="https://2023.stateofhtml.com/en-US" target="_blank" rel="noopener noreferrer">State of HTML 2023 developer survey</a> to confirm coverage of commonly used native form elements.
            This comparison prompted the inclusion of the color picker, which showed higher reported usage in the survey than in our sampled sites.
          </p>
        </details>
        <!-- form component SECTION ENDS HERE -->

        <div class="hr"></div>

        <h2 id="prompting">Prompting conditions</h2>
        <p class="muted">
We defined three prompting conditions to capture increasing levels of prompt-engineering structure. The conditions differ in task specification and role framing, with identical output constraints applied across all conditions.
        </p>

<details open>
  <summary>Step-by-step prompt design</summary>

  <div class="steps">
    <p><span class="tag">Step 1</span>
      Define a low-structure baseline that constrains output format only (HTML-only, no CSS, JavaScript, comments, or explanations).
    </p>

    <p><span class="tag">Step 2</span>
      Add task specification and a success criterion while keeping the same output constraints.
    </p>

    <p><span class="tag">Step 3</span>
      Add a persona role instruction (“expert web developer”), keeping the task wording identical to Step&nbsp;2.
    </p>
  </div>
</details>


        <div class="table-wrap" role="region" aria-label="Prompting conditions table">
          <table>
            <thead>
              <tr>
                <th class="nowrap">Condition</th>
                <th>Justification</th>
                <th>Prompt text</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="nowrap"><strong>Default</strong></td>
                <td class="muted">
Operational reference condition. Only constrains output format; the task is described minimally and no success criteria are provided. This approximates acceleration-oriented usage where developers issue compact prompts and rely on surrounding context.
                </td>
                <td>
                  <pre class="code-wrap"><code>Respond with HTML only. Do not include CSS, JavaScript, comments, or explanations.</code></pre>
                </td>
              </tr>
              <tr>
                <td class="nowrap"><strong>Standard Practice</strong></td>
<td class="muted">
  Adds task specification and a success criterion, consistent with widely cited prompt-engineering guidance that recommends
  clearly stating what the model should do and what constitutes a complete response while keeping output constraints separate
  (<a href="https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api"
      target="_blank" rel="noopener noreferrer">OpenAI</a>;
   <a href="https://github.com/github/awesome-copilot/blob/main/instructions/ai-prompt-engineering-safety-best-practices.instructions.md"
      target="_blank" rel="noopener noreferrer">GitHub Copilot</a>;
   <a href="https://huggingface.co/docs/transformers/en/tasks/prompting"
      target="_blank" rel="noopener noreferrer">Hugging Face</a>).
</td>

                <td>
                  <pre class="code-wrap"><code>Generate HTML that satisfies the requirements described in the request. Ensure the output fully addresses the request. Respond with HTML only. Do not include CSS, JavaScript, comments, or explanations.</code></pre>
                </td>
              </tr>
              <tr>
                <td class="nowrap"><strong>Standard + persona</strong></td>
<td class="muted">
  Isolates the effect of adding a role instruction by changing only the presence of a persona while keeping the task description
  and output constraints identical. This condition is included to test whether persona instructions influence accessibility-related
  outcomes, independent of task specification, consistent with recent findings that expert personas do not reliably improve
  factual accuracy
  (<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5879722"
      target="_blank" rel="noopener noreferrer">
    Prompting Science Report 4
  </a>).
</td>

                <td>
                  <pre class="code-wrap"><code>You are an expert web developer. Your task is to generate HTML that satisfies the requirements described in the request. Ensure the output fully addresses the request. Respond with HTML only. Do not include CSS, JavaScript, comments, or explanations.</code></pre>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <details>
          <summary>Prompt components (why each part exists)</summary>
          <ul>
            <li><strong>Output constraint</strong> (“Respond with HTML only…”) standardizes formatting for automated analysis.</li>
            <li><strong>Task declaration</strong> (“Generate HTML that satisfies the requirements…”) clarifies what to do without adding domain rules.</li>
            <li><strong>Success criterion</strong> (“Ensure the output fully addresses the request.”) defines completeness without prescribing implementation details.</li>
            <li><strong>Persona</strong> (“expert web developer”) tests role framing while holding everything else constant.</li>
          </ul>
        </details>

        <div class="hr"></div>

        <h2 id="linguistic-variants">Linguistic variants</h2>
        <p class="muted">
          For each prompting condition, we expressed the same task request using five linguistic styles.
          These variants introduce controlled surface-level wording changes but preserve underlying intent.
        </p>

        <div class="table-wrap" role="region" aria-label="Linguistic variants table">
          <table>
            <thead>
              <tr>
                <th class="nowrap">Variant ID</th>
                <th class="nowrap">Linguistic style</th>
                <th>What changes</th>
                <th>Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>G1</strong></td>
                <td class="nowrap">Action command</td>
                <td class="muted">Imperative phrasing that issues a direct instruction.</td>
                <td><em>Insert a text field for “What color is an orange?”</em></td>
              </tr>
              <tr>
                <td><strong>G2</strong></td>
                <td class="nowrap">Short specification</td>
                <td class="muted">Fragment/shorthand phrasing similar to notes or specs.</td>
                <td><em>Text field: What color is an orange?</em></td>
              </tr>
              <tr>
                <td><strong>G3</strong></td>
                <td class="nowrap">Descriptive object phrase</td>
                <td class="muted">Declarative noun phrase rather than an instruction.</td>
                <td><em>A text field labeled “What color is an orange?”</em></td>
              </tr>
              <tr>
                <td><strong>G4</strong></td>
                <td class="nowrap">Build instruction</td>
                <td class="muted">Construction-oriented language that names component parts.</td>
                <td><em>Build a text field and label for “What color is an orange?”</em></td>
              </tr>
              <tr>
                <td><strong>G5</strong></td>
                <td class="nowrap">Standards-oriented phrasing</td>
                <td class="muted">Signals expected conventions without prescribing rules.</td>
                <td><em>Accessible text field for “What color is an orange?”</em></td>
              </tr>
            </tbody>
          </table>
        </div>

        <details>
          <summary>Why linguistic variants</summary>
          <p class="muted">
<p class="muted">
  Prior work suggests that LLM outputs can be sensitive to changes in prompt phrasing even when task intent remains constant
  (e.g.,
  <a href="https://arxiv.org/abs/2502.06065" target="_blank" rel="noopener noreferrer">
    Benchmarking Prompt Sensitivity in Large Language Models
  </a>;
  <a href="https://arxiv.org/abs/2410.02185" target="_blank" rel="noopener noreferrer">
    POSIX: A Prompt Sensitivity Index for Large Language Models
  </a>;
  <a href="https://arxiv.org/abs/2504.06969" target="_blank" rel="noopener noreferrer">
    Towards LLM Robustness to Changes in Prompt Format Styles
  </a>).
  We therefore use a small set of clearly differentiated grammatical constructions that vary surface wording and preserve the same underlying request.
  This design allows us to examine sensitivity to phrasing changes without introducing additional task expectations or domain-specific cues that would confound interpretation.
</p>

          </p>
        </details>

        <div class="hr"></div>

      </div>
    </section>
  </main>
</body>
</html>
