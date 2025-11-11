make a react native expo app that will offer All PDF Tools.
no authentication.

it offers many PDF tools that are tailored to specific problems. All PDF tools are listed below.

# Project Specification: All PDF Tools - React Native Expo Application

## 1. Project Overview

Develop a comprehensive React Native Expo application that provides users with a complete suite of PDF manipulation tools. The application should function as an all-in-one PDF utility that allows users to perform various operations on PDF files directly from their mobile devices.

**Target Platforms:** iOS and Android and web (Expo)
**Authentication:** None required (serverless implementation)
**Core Value Proposition:** Provide a free, comprehensive set of PDF tools accessible from mobile devices without requiring user accounts or cloud storage.

## 2. Technical Requirements

### 2.1 Development Framework

- React Native with Expo SDK (latest stable version)
- JavaScript implementation (TypeScript optional)
- No backend server requirements (fully client-side implementation)

### 2.2 PDF Processing

- Implement PDF processing using React Native compatible libraries (e.g., react-native-pdf-lib, pdf-lib)
- All PDF operations must be performed on-device to ensure privacy
- Support for PDF files up to 100MB in size
- Implement proper error handling for corrupted or incompatible PDF files
- Include progress indicators for operations that may take time

### 2.3 File Management

- Implement file picking from device storage
- Request appropriate permissions for file access
- Support saving modified PDFs to device storage
- Implement temporary file cleanup to prevent storage bloat

## 3. Feature Categories and Requirements

Merge PDF
Split PDF
Compress PDF
Edit PDF
Sign PDF
PDF Converter
Convert to PDF
Convert PDF to ...
Images to PDF
PDF to images
Extract PDF images
Protect PDF
Unlock PDF
Rotate PDF pages
Remove PDF pages
Extract PDF pages
Rearrange PDF pages
Webpage to PDF
Create PDF job application
Create PDF with a camera
PDF OCR
Add watermark
Add page numbers
View as PDF
PDF Overlay
Compare PDFs
Web optimize PDF
Annotate PDF
Redact PDF
Create PDf

### 3.1 Document Organization

| Feature | Description | Priority |
|---------|-------------|----------|
| Merge PDF | Combine multiple PDFs into a single document with customizable order | High |
| Split PDF | Separate PDF into multiple documents by page ranges or individual pages | High |
| Remove Pages | Delete specific pages from a PDF document | High |
| Extract Pages | Save selected pages as a new PDF document | High |
| Organize Pages | Rearrange, rotate, or delete pages within a document | Medium |

PDF to images
PDF to Word
PDF to PowerPoint
PDF to Excel
PDF to JPG
PDF to PNG
PDF to SVG
PDF to DOCX
PDF to PPTX
PDF to XLSX
PDF to ODT
PDF to ODS
PDF to ODP
PDF to Text
PDF to RTF
PDF to EPUB
PDF to HTML
PDF to secure PDF
PDF to PDF/A

### 3.2 Conversion Tools

| Feature | Description | Priority |
|---------|-------------|----------|
| JPG/PNG/webp/word/powerpoint/excel/html/text/rtf/epub/odt/odg/ods/odp/tiff/svg/heic/docx/pptx/xlsx/doc/ppt/xls/odt/odg/ods/odp/tiff/text/rtf/epub to PDF | Convert single or multiple files to PDF with customizable layout | High |
| PDF to JPG/PNG/webp/word/powerpoint/excel/html | Extract pages as images or convert entire document to  other files | High |

### 3.3 Editing Tools

| Feature | Description | Priority |
|---------|-------------|----------|
| Rotate PDF | Change page orientation (90°, 180°, 270°) for some or all pages | High |
| Add Page Numbers | Insert customizable page numbers with position and format options | Medium |
| Add Watermark | Apply text or image watermarks with opacity and position controls | Medium |
| Crop PDF | Adjust page margins or crop to specific dimensions | Medium |
| Basic Text/Image Editing | Add or edit simple text and images on PDF pages | Low |

### 3.4 Security Tools

| Feature | Description | Priority |
|---------|-------------|----------|
| Unlock PDF | Remove password protection from PDF files | High |
| Protect PDF | Add password protection to PDF files | High |
| Sign PDF | Add digital signatures to documents | Medium |
| Redact PDF | Permanently remove sensitive information from documents | Low |

### 3.5 Enhancement Tools

| Feature | Description | Priority |
|---------|-------------|----------|
| Compress PDF | Reduce file size while maintaining reasonable quality | High |
| Repair PDF | Attempt to fix corrupted PDF files | Medium |
| OCR PDF | Convert scanned documents to searchable text | Medium |
| Scan to PDF | Use device camera to scan documents and convert to PDF | Medium |
| Compare PDF | Show differences between two PDF documents | Low |

### 3.6 AI Features (Gemini API Integration)

| Feature | Description | Priority |
|---------|-------------|----------|
| Chat with PDF | Interactive Q&A with PDF content using RAG | High |
| AI PDF Summarizer | Generate concise summaries of PDF documents | High |
| Translate PDF | Translate PDF content between languages | Medium |
| AI Question Generator | Create questions based on PDF content | Low |

## 4. AI Implementation Requirements

### 4.1 Gemini API Integration

- Implement Google's Generative AI capabilities using the official SDK
- Required installation: `npm install @google/generative-ai`
- User must provide their own Gemini API key through a settings page
- Store API key securely using device secure storage (e.g., Expo SecureStore)
- Implement model selection functionality with appropriate defaults

### 4.2 Retrieval Augmented Generation (RAG)

- Extract and process text from PDFs for context
- Implement chunking strategy for large documents (e.g., page-based, section-based)
- Create appropriate prompts that combine user queries with document context
- Handle API rate limiting and token limitations gracefully
- Implement fallback mechanisms for when AI features are unavailable

### 4.3 Model Selection

- Provide interface for users to select from available Gemini models
- Implement model listing functionality as shown in the example code:

```javascript
async function listModels() {
  const models = await client.listModels();
  return models.map(model => ({
    name: model.name,
    description: model.description,
    inputTokenLimit: model.inputTokenLimit,
    outputTokenLimit: model.outputTokenLimit
  }));
}
```

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

- You must have billing enabled and API access.
- Only accessible via `@google/generative-ai` client or direct REST calls to:

  ```
  GET https://generativelanguage.googleapis.com/v1beta/models
  ```

Would you like a version that uses **plain REST/fetch** instead of the Node.js SDK?
