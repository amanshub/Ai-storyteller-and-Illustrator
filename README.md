# AI Storyteller & Illustrator - Setup Guide

## 1. Get API Keys (Free)
You need two API keys to make this work.

### Google Gemini API (For Story)
1.  Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Click **Create API key**.
3.  Copy the key.

### HuggingFace API (For Images)
1.  Go to [HuggingFace Settings](https://huggingface.co/settings/tokens).
2.  Create a new token (Access Token).
3.  Give it a name (e.g., "story-app") and select **Read** permissions.
4.  Copy the token.

## 2. Configure the App
1.  Open the file named `.env` in this folder.
2.  Paste your keys like this:
    ```env
    GOOGLE_API_KEY=AIzaSy...
    HUGGINGFACE_API_TOKEN=hf_...
    ```
3.  Save the file.

## 3. Run the App
1.  Open your terminal/command prompt in this folder.
2.  Run this command:
    ```bash
    python -m streamlit run app.py
    ```
3.  The app will open in your browser!
