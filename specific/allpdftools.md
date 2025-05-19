make a react native expo app that will offer All PDF Tools.
no authentication.

it offers many PDF tools that are tailored to specific problems. All PDF tools are listed below.
Organize PDF
Merge PDF
Split PDF
Remove pages
Extract pages
Organize PDF
Scan to PDF
Optimize PDF
Compress PDF
Repair PDF
OCR PDF
Convert to PDF
JPG to PDF
WORD to PDF
POWERPOINT to PDF
EXCEL to PDF
HTML to PDF
Convert from PDF
PDF to JPG
PDF to WORD
PDF to POWERPOINT
PDF to EXCEL
PDF to PDF/A
Edit PDF
Rotate PDF
Add page numbers
Add watermark
Crop PDF
Edit PDF
PDF security
Unlock PDF
Protect PDF
Sign PDF
Redact PDF
Compare PDF
Every tool you need to work with PDFs in one place
Every tool you need to use PDFs, at your fingertips. All are 100% FREE and easy to use! Merge, split, compress, convert, rotate, unlock and watermark PDFs with just a few clicks.
Merge PDF
Combine PDFs in the order you want with the easiest PDF merger available.

Split PDF
Separate one page or a whole set for easy conversion into independent PDF files.

Compress PDF
Reduce file size while optimizing for maximal PDF quality.

PDF to Word
Easily convert your PDF files into easy to edit DOC and DOCX documents. The converted WORD document is almost 100% accurate.

PDF to PowerPoint
Turn your PDF files into easy to edit PPT and PPTX slideshows.

PDF to Excel
Pull data straight from PDFs into Excel spreadsheets in a few short seconds.

Word to PDF
Make DOC and DOCX files easy to read by converting them to PDF.

PowerPoint to PDF
Make PPT and PPTX slideshows easy to view by converting them to PDF.

Excel to PDF
Make EXCEL spreadsheets easy to read by converting them to PDF.

New!
Edit PDF
Add text, images, shapes or freehand annotations to a PDF document. Edit the size, font, and color of the added content.

PDF to JPG
Convert each PDF page into a JPG or extract all images contained in a PDF.

JPG to PDF
Convert JPG images to PDF in seconds. Easily adjust orientation and margins.

Sign PDF
Sign yourself or request electronic signatures from others.

Watermark
Stamp an image or text over your PDF in seconds. Choose the typography, transparency and position.

Rotate PDF
Rotate your PDFs the way you need them. You can even rotate multiple PDFs at once!

HTML to PDF
Convert webpages in HTML to PDF. Copy and paste the URL of the page you want and convert it to PDF with a click.

Unlock PDF
Remove PDF password security, giving you the freedom to use your PDFs as you want.

Protect PDF
Protect PDF files with a password. Encrypt PDF documents to prevent unauthorized access.

Organize PDF
Sort pages of your PDF file however you like. Delete PDF pages or add PDF pages to your document at your convenience.

PDF to PDF/A
Transform your PDF to PDF/A, the ISO-standardized version of PDF for long-term archiving. Your PDF will preserve formatting when accessed in the future.

Repair PDF
Repair a damaged PDF and recover data from corrupt PDF. Fix PDF files with our Repair tool.

Page numbers
Add page numbers into PDFs with ease. Choose your positions, dimensions, typography.

Scan to PDF
Capture document scans from your mobile device and send them instantly to your browser.

OCR PDF
Easily convert scanned PDF into searchable and selectable documents.

New!
Compare PDF
Show a side-by-side document comparison and easily spot changes between different file versions.

New!
Redact PDF
Redact text and graphics to permanently remove sensitive information from a PDF.

New!
Crop PDF
Crop margins of PDF documents or select specific areas, then apply the changes to one page or the whole document.
Compress
Compress PDF
Convert
PDF Converter

Organize
Merge PDF
Split PDF
Rotate PDF
Delete PDF Pages
Extract PDF Pages
Organize PDF
View & Edit
Edit PDF
PDF Annotator
PDF Reader
Number Pages
Crop PDF
Redact PDF
Watermark PDF
Share PDF
Convert from PDF
PDF to Word
PDF to Excel
PDF to PPT
PDF to JPG
Convert to PDF
Word to PDF
Excel to PDF
PPT to PDF
JPG to PDF
PDF OCR
Sign
Sign PDF
More
Unlock PDF
Protect PDF
Flatten PDF
Scan
PDF Scanner

AI PDF
Chat with PDF
AI PDF Summarizer
Translate PDF
AI Question Generator

ai features will be implemented via gemini api use the gemini key entered by the user in the settings page. provide a way for the user to enter the gemini key in the settings page. provide a way for user to select the model to be used for the ai features. the ai features will be implemented completely on the frontend. as there is no backend . use retrieval augmented generation for the ai features.
To get the list of available **Gemini models** (from Google’s Generative AI platform, formerly known as Bard/PaLM) using **JavaScript**, you typically use the **Google Generative AI SDK** (via REST API or Node.js client).

### 📦 1. Install Google Generative AI SDK (for Node.js)

```bash
npm install @google/generative-ai
```

---

### 🔑 2. Setup API Key

Get your API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

```js
const genAI = require("@google/generative-ai");

const API_KEY = "YOUR_API_KEY_HERE";

const client = new genAI.GoogleGenerativeAI(API_KEY);
```

---

### 📋 3. List Available Models

Use the `listModels()` function:

```js
async function listModels() {
  const models = await client.listModels();
  models.forEach((model) => {
    console.log(`Model name: ${model.name}`);
    console.log(`  Description: ${model.description}`);
    console.log(`  Input token limit: ${model.inputTokenLimit}`);
    console.log(`  Output token limit: ${model.outputTokenLimit}`);
    console.log("---------------------------");
  });
}

listModels().catch(console.error);
```

---

### ✅ Output Example

This will return available models like:

```
Model name: models/gemini-1.5-pro
Model name: models/gemini-1.0-pro
Model name: models/gemini-1.5-flash
...
```

---

### 🧠 Notes

* You must have billing enabled and API access.
* Only accessible via `@google/generative-ai` client or direct REST calls to:

  ```
  GET https://generativelanguage.googleapis.com/v1beta/models
  ```

Would you like a version that uses **plain REST/fetch** instead of the Node.js SDK?
