
🔑 Key features:

📝 Paraphrase: Reshape your sentences into clear, engaging alternatives that better match your tone, context, and audience, all while keeping your meaning intact.

✅  Perfect Grammar: Experience flawless grammar and spelling in every rewrite, ensuring your text is perfectly edited before hitting “send”.

💻 Works where you write: Seamlessly integrated into your Chrome browser, allowing you to write, rewrite, and generate content directly on your favorite websites: no need to switch tabs.

➡️ Generate Text: Easily create content within any website you’re writing on. Text that understands your context and fits your tone and style.

🎓Minimize Plagiarism: Generate original content and paraphrase existing text to ensure unique, non-plagiarized writing.

🤖 AI Detection Resistant: Wordtune helps humanize your writing, reducing the likelihood of being flagged by AI detection tools.

🌐 Translate: Eliminate language barriers and deliver perfectly worded translations of your native language to English.

🖊️ Custom Writing Tones: Take your writing from a casual tone to something more formal with the click of a button—and vice versa.

The browser extension is built with the following setup:

-   Frontend: Browser Extension
-   Project Structure:
    -   extension/ folder for browser extension code
    -   backend/ folder for the backend code for the AI model integration with gemini-2.5-flash-preview-04-17
    -   ensure the backend is designed to handle AI model requests efficiently.
    -   ensure the extension is built with a focus on user experience and performance.
    -   Don't leave anything for future, this is a prd for final product not a mvp.
    -   the extension will store the api key in the browser storage and will be used to make requests to the backend.
the browser extension should use the following code for the gemini integration:
  // To run this code you need to install the following dependencies:
// npm install @google/genai mime
// npm install -D @types/node

import {
  GoogleGenAI,
} from '@google/genai';

async function main() {
  const ai = new GoogleGenAI({
    apiKey: process.env.GEMINI_API_KEY,
  });
  const config = {
    thinkingConfig: {
      thinkingBudget: 3881,
    },
    responseMimeType: 'text/plain',
  };
  const model = 'gemini-2.5-flash-preview-04-17';
  const contents = [
    {
      role: 'user',
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
