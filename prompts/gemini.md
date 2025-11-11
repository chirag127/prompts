IMPORTANT: use the following code strictly for the gemini integration:

```javascript
// To run this code you need to install the following dependencies:
// npm install @google/genai mime
// npm install -D @types/node

import { GoogleGenAI } from "@google/genai";

async function main() {
    const ai = new GoogleGenAI({});
    const config = {
        responseMimeType: "text/plain",
    };
    const model = "gemini-2.5-flash-preview-04-17";
    const contents = [
        {
            role: "user",
            parts: [
                {
                    text: `INSERT_INPUT_HERE`,
                },
            ],
        },
    ];

    const response = await ai.models.generateContentStream({
        model,
        config,
        contents,
    });
    for await (const chunk of response) {
        console.log(chunk.text);
    }
}

main();
```

```
