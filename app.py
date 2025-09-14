import os
import json
import gradio as gr
import requests

# Load local Q&A database
QA_FILE = "qa_data.json"
if os.path.exists(QA_FILE):
    with open(QA_FILE, "r", encoding="utf-8") as f:
        qa_data = json.load(f)
else:
    qa_data = {}

# OpenRouter API settings
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", None)
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Helper: check local QA database
def check_local_db(question: str):
    return qa_data.get(question.strip())

# Helper: ask OpenR
demo.launch(server_name="0.0.0.0", server_port=5000)
