import gradio as gr
import os
import requests
from dotenv import load_dotenv
from PIL import Image
import pytesseract
import whisper

# Load environment variables
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# AI Query Function
def ask_ai_model(prompt):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "mistralai/mistral-7b-instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful AI tutor."},
                {"role": "user", "content": prompt}
            ]
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI Error: {str(e)}"

# Web Search with summarization fallback
def perform_web_search(query):
    try:
        headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
        data = {"q": query}
        res = requests.post("https://google.serper.dev/search", headers=headers, json=data)
        results = res.json().get("organic", [])[:3]
        summary = []
        for r in results:
            title = r.get("title", "")
            link = r.get("link", "")
            snippet = r.get("snippet", "")
            summary.append(f"🔗 {title}
{link}
{snippet}
")
        return "
".join(summary)
    except Exception as e:
        return f"Search Error: {e}"

# Audio Transcription
def transcribe_audio(audio_path):
    try:
        model = whisper.load_model("base")
        return model.transcribe(audio_path)["text"]
    except Exception as e:
        return f"Audio error: {e}"

# OCR from image
def extract_text_from_image(img_path):
    try:
        img = Image.open(img_path)
        return pytesseract.image_to_string(img)
    except Exception as e:
        return f"Image error: {e}"

# Handler
def tutor_main(user_input, audio, image):
    question = user_input
    if audio:
        question = transcribe_audio(audio)
    elif image:
        question = extract_text_from_image(image)

    if question:
        result = ask_ai_model(question)
        if "AI Error" in result:
            result += "

Trying Web Search + Summary:
" + perform_web_search(question)
        return result
    return "Please input text or upload audio/image."

# Gradio App with 'Enter' to submit
with gr.Blocks() as dashboard:
    gr.Markdown("# 📘 AI Competitive Tutor Dashboard")
    with gr.Row():
        with gr.Column():
            qbox = gr.Textbox(label="Ask a question", placeholder="Type and hit Enter...", lines=2)
            audio = gr.Audio(type="filepath", label="Upload Audio")
            image = gr.Image(type="filepath", label="Upload Image")
        with gr.Column():
            output = gr.Textbox(label="AI Answer", lines=12)
    qbox.submit(fn=tutor_main, inputs=[qbox, audio, image], outputs=output)
    dashboard.launch()