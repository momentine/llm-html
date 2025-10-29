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

### Component: text-field

| Model                 | Form Component | Variant | Prompt                                                               | Output (HTML) | File Link                                                   |
| --------------------- | -------------- | ------- | -------------------------------------------------------------------- | ------------- | ----------------------------------------------------------- |
| x-ai/grok-code-fast-1 | text-field     | G1      | Insert a field to respond to the question “What color is an orange?” | —             | [g1.html](outputs/x-ai/grok-code-fast-1/text-field/g1.html) |
|                       |                | G2      | Text field: What color is an orange?                                 | —             | [g2.html](outputs/x-ai/grok-code-fast-1/text-field/g2.html) |
|                       |                | G3      | Field: What color is an orange?                                      | —             | [g3.html](outputs/x-ai/grok-code-fast-1/text-field/g3.html) |
|                       |                | G4      | Field and label for “What color is an orange?”                       | —             | [g4.html](outputs/x-ai/grok-code-fast-1/text-field/g4.html) |
|                       |                | G5      | Accessible field to answer What color is an orange?                  | —             | [g5.html](outputs/x-ai/grok-code-fast-1/text-field/g5.html) |
