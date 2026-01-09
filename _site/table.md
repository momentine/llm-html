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
| **G2** | **Short Specification**       | Concise, label-like statement       | Shorthand phrasing developers use in prototyping, quick notes, or configuration-style prompts.                         | *Component: Label*                 |
| **G3** | **Descriptive Object Phrase** | Declarative component description   | Natural descriptive phrasing resembling how developers describe an interface element to another person or review tool. | *A ___ labeled “Label”*             |
| **G4** | **Build Instruction**         | Explicit construction phrasing      | Typical of co-creative prompting where developers ask the AI to build and wire up both the element and its label.      | *Build a ___ and label for “Label”* |
| **G5** | **Accessibility Request**     | Accessibility-focused phrasing      | Indicates explicit intent for accessible markup or inclusive design considerations.                                    | *Accessible ___ for “Label”*        |

</details>

