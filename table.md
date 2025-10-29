# LLM Generated HTML Form Compoents Output 
Each form component is treated as a test case.
Each test case contains five prompt variations, each representing a distinct grammar pattern.

## Universal Prompt 
You are an AI coding assistant.
Respond with semantic HTML code only.
Do not include explanations, comments, CSS, JavaScript, or code fences.
Assume the snippet will be inserted directly into an existing HTML document.

## Grammar variants (used across every test)

| Tag    | Grammar Pattern         | Cue                                             |
| ------ | ----------------------- | ----------------------------------------------- |
| **G1** | Imperative              | Verb-first: “Add…”, “Insert…”, “Create…”        |
| **G2** | Declarative Label       | Noun + colon: “Text field: …”                   |
| **G3** | Nominal Fragment        | Noun phrase: “A text field labeled …”           |
| **G4** | Verbose (single clause) | Same ask + short clause (“with…”, “including…”) |
| **G5** | Accessibility-Hinted    | Same ask + “Accessible …”                       |

## Components 

<details>
  <summary><strong>Text Field</strong></summary>

| Model | Variant | Prompt | Output | File Link |
|--------|----------|---------|----------------|------------|
| **openai/gpt-5** | G1 | Insert a field to respond to the question “What color is an orange?” | <details><summary>View code</summary>
hi
 </details>
| [html](outputs/text-field/openai-gpt-5/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/openai-gpt-5/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/openai-gpt-5/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/openai-gpt-5/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/openai-gpt-5/g5.html) |
| **openai/gpt-5-mini** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/openai-gpt-5-mini/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/openai-gpt-5-mini/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/openai-gpt-5-mini/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/openai-gpt-5-mini/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/openai-gpt-5-mini/g5.html) |
| **openai/gpt-4.1-mini** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/openai-gpt-4.1-mini/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/openai-gpt-4.1-mini/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/openai-gpt-4.1-mini/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/openai-gpt-4.1-mini/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/openai-gpt-4.1-mini/g5.html) |
| **anthropic/claude-sonnet-4.5** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/anthropic-claude-sonnet-4.5/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/anthropic-claude-sonnet-4.5/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/anthropic-claude-sonnet-4.5/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/anthropic-claude-sonnet-4.5/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/anthropic-claude-sonnet-4.5/g5.html) |
| **anthropic/claude-sonnet-4** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/anthropic-claude-sonnet-4/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/anthropic-claude-sonnet-4/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/anthropic-claude-sonnet-4/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/anthropic-claude-sonnet-4/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/anthropic-claude-sonnet-4/g5.html) |
| **anthropic/claude-3.7-sonnet** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/anthropic-claude-3.7-sonnet/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/anthropic-claude-3.7-sonnet/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/anthropic-claude-3.7-sonnet/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/anthropic-claude-3.7-sonnet/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/anthropic-claude-3.7-sonnet/g5.html) |
| **google/gemini-2.5-pro** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/google-gemini-2.5-pro/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/google-gemini-2.5-pro/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/google-gemini-2.5-pro/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/google-gemini-2.5-pro/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/google-gemini-2.5-pro/g5.html) |
| **google/gemini-2.5-flash** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/google-gemini-2.5-flash/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/google-gemini-2.5-flash/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/google-gemini-2.5-flash/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/google-gemini-2.5-flash/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/google-gemini-2.5-flash/g5.html) |
| **google/gemma-3-12b-it** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/google-gemma-3-12b-it/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/google-gemma-3-12b-it/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/google-gemma-3-12b-it/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/google-gemma-3-12b-it/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/google-gemma-3-12b-it/g5.html) |
| **x-ai/grok-4-fast** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/x-ai-grok-4-fast/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/x-ai-grok-4-fast/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/x-ai-grok-4-fast/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/x-ai-grok-4-fast/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/x-ai-grok-4-fast/g5.html) |
| **x-ai/grok-4** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/x-ai-grok-4/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/x-ai-grok-4/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/x-ai-grok-4/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/x-ai-grok-4/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/x-ai-grok-4/g5.html) |
| **deepseek/deepseek-chat-v3.1** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/deepseek-deepseek-chat-v3.1/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/deepseek-deepseek-chat-v3.1/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/deepseek-deepseek-chat-v3.1/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/deepseek-deepseek-chat-v3.1/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/deepseek-deepseek-chat-v3.1/g5.html) |
| **qwen/qwen3-coder-30b-a3b-instruct** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/qwen-qwen3-coder-30b-a3b-instruct/g5.html) |
| **qwen/qwen3-coder-480b-a35b** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/qwen-qwen3-coder-480b-a35b/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/qwen-qwen3-coder-480b-a35b/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/qwen-qwen3-coder-480b-a35b/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/qwen-qwen3-coder-480b-a35b/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/qwen-qwen3-coder-480b-a35b/g5.html) |
| **qwen/qwen3-vl-235b-a22b-instruct** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/qwen-qwen3-vl-235b-a22b-instruct/g5.html) |
| **z-ai/glm-4.6** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/z-ai-glm-4.6/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/z-ai-glm-4.6/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/z-ai-glm-4.6/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/z-ai-glm-4.6/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/z-ai-glm-4.6/g5.html) |
| **z-ai/glm-4.5-air** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/z-ai-glm-4.5-air/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/z-ai-glm-4.5-air/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/z-ai-glm-4.5-air/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/z-ai-glm-4.5-air/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/z-ai-glm-4.5-air/g5.html) |
| **mistral/mixtral-8x22b** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/mistral-mixtral-8x22b/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/mistral-mixtral-8x22b/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/mistral-mixtral-8x22b/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/mistral-mixtral-8x22b/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/mistral-mixtral-8x22b/g5.html) |
| **meta/llama-3.1-405b** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/meta-llama-3.1-405b/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/meta-llama-3.1-405b/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/meta-llama-3.1-405b/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/meta-llama-3.1-405b/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/meta-llama-3.1-405b/g5.html) |
| **meta/llama-3.1-70b** | G1 | Insert a field to respond to the question “What color is an orange?” | — | [g1.html](outputs/text-field/meta-llama-3.1-70b/g1.html) |
|  | G2 | Text field: What color is an orange? | — | [g2.html](outputs/text-field/meta-llama-3.1-70b/g2.html) |
|  | G3 | Field: What color is an orange? | — | [g3.html](outputs/text-field/meta-llama-3.1-70b/g3.html) |
|  | G4 | Field and label for “What color is an orange?” | — | [g4.html](outputs/text-field/meta-llama-3.1-70b/g4.html) |
|  | G5 | Accessible field to answer What color is an orange? | — | [g5.html](outputs/text-field/meta-llama-3.1-70b/g5.html) |

</details>
