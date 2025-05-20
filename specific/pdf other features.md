| Split PDF | Separate PDF into multiple documents by page ranges or individual pages | High |
| Remove Pages | Delete specific pages from a PDF document | High |
| Extract Pages | Save selected pages as a new PDF document | High |
| Organize Pages | Rearrange, rotate, or delete pages within a document | Medium |



### 3.2 Conversion Tools
| Feature | Description | Priority |
|---------|-------------|----------|
| JPG/PNG/webp/word/powerpoint/excel/html/text/rtf/epub/odt/odg/ods/odp/tiff/svg/heic/docx/pptx/xlsx/doc/ppt/xls/odt/odg/ods/odp/tiff/text/rtf/epub to PDF | Convert single or multiple files to PDF with customizable layout | High |
| PDF to JPG/PNG/webp/word/powerpoint/excel/html/text/rtf/epub/odt/odg/ods/odp/tiff/svg/heic/docx/pptx/xlsx/doc/ppt/xls/odt/odg/ods/odp/tiff/text/rtf/epub/html/secure PDF/PDF/A | Extract pages as images or convert entire document to  other files | High |

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
- Implement Google's Generative AI capabilities using the official SDK using python
- User must provide their own Gemini API key through a settings page
- Store API key securely using device secure storage (e.g., Expo SecureStore)
- Implement model selection functionality for AI features
- Provide a user-friendly interface for selecting models
### 4.2 Retrieval Augmented Generation (RAG)
- Extract and process text from PDFs for context
- Implement chunking strategy for large documents (e.g., page-based, section-based)
- Create appropriate prompts that combine user queries with document context
- Handle API rate limiting and token limitations gracefully
- Implement fallback mechanisms for when AI features are unavailable
11. Localization / Internationalization (i18n):
Will the app need to support multiple languages?
 English only for the app's UI in the initial version. However, the codebase should be structured to easily support i18n later (e.g., by externalizing all user-facing strings into resource files).

### 4.3 Model Selection
- Provide interface for users to select from available Gemini models


ai features will be implemented via gemini api use the gemini key entered by the user in the settings page. provide a way for the user to enter the gemini key in the settings page. provide a way for user to select the model to be used for the ai features. use retrieval augmented generation for the ai features.
Yes! Here's how you can list available **Gemini models using the Python SDK** for Google Generative AI.

---

### ✅ Step-by-step Guide

#### 📦 1. Install the SDK

```bash
pip install google-generativeai
```

---

#### 🔑 2. Set Your API Key

Get your API key from: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY_HERE")
```

---

#### 📋 3. List Available Models

```python
def list_models():
    models = genai.list_models()
    for model in models:
        print(f"Model name: {model.name}")
        print(f"  Description: {getattr(model, 'description', 'N/A')}")
        print(f"  Input token limit: {getattr(model, 'input_token_limit', 'N/A')}")
        print(f"  Output token limit: {getattr(model, 'output_token_limit', 'N/A')}")
        print("-" * 40)

list_models()
```

---

### 🧠 Example Output

```text
Model name: models/gemini-1.5-pro
  Description: Gemini 1.5 Pro model
  Input token limit: 32768
  Output token limit: 8192
----------------------------------------
Model name: models/gemini-1.5-flash
  Description: Gemini 1.5 Flash model
  Input token limit: 32768
  Output token limit: 8192
----------------------------------------
...
```

Let me know if you want code for **calling a specific Gemini model** or **streaming responses** as well!


strictly include the above code in the masterplan.md file to get the list of available models.

 continue with suggested answers you provided
- Treat this as an indication that the user accepts all your suggested answers and wants to move forward