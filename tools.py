import os
import ollama
import re

# ---------- MAIN ROUTER ----------
def run_action(intent, text):
    if intent == "create_file":
        return create_file(text)
    elif intent == "write_code":
        return write_code(text)
    elif intent == "summarize":
        return summarize_text(text)
    else:
        return chat_response(text)


# ---------- CREATE FILE ----------
def create_file(text):
    os.makedirs("output", exist_ok=True)

    filename = "file.txt"

    for word in text.split():
        if "." in word:
            filename = word

    path = os.path.join("output", filename)

    with open(path, "w") as f:
        f.write("File created.")

    return f"File created: {filename}"


# ---------- WRITE CODE ----------
def write_code(text):
    os.makedirs("output", exist_ok=True)

    filename = "code.py"

    match = re.search(r'\b\w+\.py\b', text)
    if match:
        filename = match.group()

    path = os.path.join("output", filename)

    prompt = f"""
Generate simple Python code:

{text}

Only code. No explanation.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    code = response['message']['content']

    code = re.sub(r"```.*?\n", "", code)
    code = code.replace("```", "").strip()

    with open(path, "w") as f:
        f.write(code)

    return f"Code saved to {filename}"


# ---------- SUMMARIZE ----------
def summarize_text(text):
    import os
    import ollama

    os.makedirs("output", exist_ok=True)

    clean = text.lower().replace("summarize", "").strip()

    if len(clean.split()) < 5:
        return "Provide more text to summarize."

    prompt = f"""
Summarize clearly:

{clean}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    summary = response['message']['content'].strip()

    # 🔥 SAVE RESULT
    with open("output/summary.txt", "w") as f:
        f.write(summary)

    return summary

# ---------- CHAT ----------
def chat_response(text):
    import os
    import ollama

    os.makedirs("output", exist_ok=True)

    prompt = f"""
Answer clearly:

{text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response['message']['content'].strip()

    # 🔥 SAVE CHAT
    with open("output/chat.txt", "w") as f:
        f.write(reply)

    return reply