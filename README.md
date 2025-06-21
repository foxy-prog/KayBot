# 🧠 AI Competitive Tutor

This is an AI-powered educational assistant built using Gradio, Whisper, OCR, and OpenRouter.

## ✨ Features

- Text-based question answering
- Audio transcription using OpenAI Whisper
- OCR (image to text) from uploaded images
- AI answers via OpenRouter
- Automatic fallback to web search if AI fails
- Dashboard-style UI
- Submit on pressing Enter

## 🛠️ Requirements

- Python 3.8+
- Whisper
- OpenRouter API key
- Serper.dev API key for Google Search

## 🚀 How to Run

1. Clone the repo or extract the ZIP.
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Add your `.env` file with:

```
OPENROUTER_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

4. Run the app:

```
python app.py
```

## 🧪 Deployment

- Hugging Face Space
- AWS EC2
- Streamlit Community Cloud
- Railway or Render

---
© 2025 NeauraTrack Robotics