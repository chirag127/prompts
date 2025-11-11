"""
Gemini API Utility Script (gemini.py)

Purpose:
    Provides a simple interface to interact with Google's Gemini AI API.
    Useful for testing Gemini integrations and quick AI queries.

Usage:
    1. Set GEMINI_API_KEY environment variable
    2. Modify the INSERT_INPUT_HERE placeholder with your prompt
    3. Run: python script/gemini.py

Configuration:
    - Model: gemini-2.5-flash-preview-04-17
    - Temperature: 1 (creative)
    - Max tokens: 65536

Author: Chirag Singhal (@chirag127)
"""

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 65536,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.5-flash-preview-04-17",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)