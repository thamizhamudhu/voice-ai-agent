import json
import os

FILE = "chat_history.json"

def load_history():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(FILE, "w") as f:
        json.dump(history, f, indent=2)