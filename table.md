# Universal System Prompt
You are an AI coding assistant.
Respond with semantic HTML code only.
Do not include explanations, comments, CSS, JavaScript, or code fences.
Assume the snippet will be inserted directly into an existing HTML document.

| Tag    | Grammar Pattern         | Cue                                             |
| ------ | ----------------------- | ----------------------------------------------- |
| **G1** | Imperative              | Verb-first: “Add…”, “Insert…”, “Create…”        |
| **G2** | Declarative Label       | Noun + colon: “Text field: …”                   |
| **G3** | Nominal Fragment        | Noun phrase: “A text field labeled …”           |
| **G4** | Verbose (single clause) | Same ask + short clause (“with…”, “including…”) |
| **G5** | Accessibility-Hinted    | Same ask + “Accessible …”                       |
