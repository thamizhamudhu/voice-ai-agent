# Voice-Controlled Local AI Agent

## Overview

This project implements a local AI agent that processes user input through voice or text, understands intent, performs actions, and returns results through a structured interface.

The system uses local models for speech recognition and language understanding, ensuring it works without paid APIs.

---

## Features

* Audio input via file upload (.wav, .mp3)
* Text input support
* Speech-to-text using Whisper (local)
* Intent detection using rule-based logic with LLM fallback (Ollama)
* Tool execution:

  * File creation
  * Python code generation and saving
  * Text summarization
  * General chat responses
* Compound command handling (multiple actions in one input)
* Persistent chat history using JSON storage
* Clean Streamlit UI displaying:

  * Transcription
  * Intent
  * Final output

---

## Architecture

```text
Input (Audio/Text)
        ↓
Speech-to-Text (Whisper)
        ↓
Intent Detection
        ↓
Action Execution
        ↓
Output + Storage
```

---

## Project Structure

```text
voice-ai-agent/
│
├── app.py              # Streamlit application
├── stt.py              # Speech-to-text (Whisper)
├── intent.py           # Intent detection logic
├── tools.py            # Action execution
├── memory.py           # Persistent chat storage
├── output/             # Generated files
├── chat_history.json   # Saved chat history
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repository-link>
cd voice-ai-agent
```

---

### 2. Install Dependencies

```bash
uv add streamlit openai-whisper ollama
```

---

### 3. Install FFmpeg

Whisper requires FFmpeg.

Download:
https://www.gyan.dev/ffmpeg/builds/

Add to PATH:

```text
C:\ffmpeg\bin
```

Verify:

```bash
ffmpeg -version
```

---

### 4. Install Ollama

Download:
https://ollama.com

Pull model:

```bash
ollama pull llama3
```

Verify:

```bash
ollama run llama3
```

---

## Run the Application

```bash
uv run streamlit run app.py
```

---

## Example Inputs

### Chat

what is artificial intelligence

### Code Generation

create a python file hello.py with a hello function

### File Creation

create a file notes.txt

### Summarization

summarize artificial intelligence is transforming industries worldwide

### Compound Command

create a file test.txt and write a python file hello.py

---

## Persistent Memory

Chat history is stored locally in:

```text
chat_history.json
```

This allows the application to retain conversation history across sessions without using a database.

---

## Safety Constraint

All generated files are saved only inside:

```text
output/
```

This prevents unintended modifications to system files.

---

## Challenges

* Handling noisy or inaccurate speech transcription
* Ensuring correct intent classification for short or ambiguous inputs
* Cleaning LLM outputs for consistent formatting
* Managing compound commands reliably
* Maintaining persistence without a database

---

## Future Improvements

* Real-time microphone input
* Improved intent classification using structured prompts
* Support for document upload and summarization
* Multi-session chat management
* More robust error handling for unclear inputs

---

## Author

Thamizha

---

## Summary

This project demonstrates a complete local AI pipeline combining speech recognition, intent understanding, and action execution with persistent memory and modular design.
