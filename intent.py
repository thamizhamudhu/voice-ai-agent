import ollama

def detect_intent(text):
    text_lower = text.lower()

    # strict summarize rule
    if ("summarize" in text_lower or "summary" in text_lower) and len(text_lower.split()) > 6:
        return "summarize"

    # file creation
    if "create" in text_lower and "file" in text_lower:
        return "create_file"

    # code generation
    if ".py" in text_lower or "python" in text_lower or "code" in text_lower:
        return "write_code"

    # fallback to LLM
    prompt = f"""
Classify into ONE word:

create_file
write_code
summarize
chat

Text: {text}

Return only one word.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    intent = response['message']['content'].strip().lower()

    valid = ["create_file", "write_code", "summarize", "chat"]
    if intent not in valid:
        return "chat"

    return intent