import streamlit as st
from stt import transcribe_audio
from intent import detect_intent
from tools import run_action
from memory import load_history, save_history

st.set_page_config(page_title="Voice AI Agent", layout="centered")

st.title("Voice AI Agent")
st.caption("Voice → Text → Intent → Action → Output")

audio_file = st.file_uploader("Upload audio (.wav or .mp3)", type=["wav", "mp3"])
text_input = st.text_input("Or type your command")

if "messages" not in st.session_state:
    st.session_state.messages = load_history()

if st.button("Run Agent"):

    if audio_file:
        text = transcribe_audio(audio_file)
    elif text_input.strip():
        text = text_input
    else:
        st.warning("Provide input")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": text})
    save_history(st.session_state.messages)

    st.subheader("Transcription")
    st.write(text)

    if len(text.strip()) < 3:
        st.warning("Unclear audio. Try again.")
        st.stop()

    if "and" in text.lower():
        parts = text.lower().split("and")
        results = []

        for part in parts:
            intent = detect_intent(part)
            result = run_action(intent, part)
            results.append(result)

        final_result = " | ".join(results)

        st.subheader("Final Output")
        st.write(final_result)

        st.session_state.messages.append({"role": "assistant", "content": final_result})
        save_history(st.session_state.messages)

    else:
        intent = detect_intent(text)

        st.subheader("Intent")
        st.write(intent)

        result = run_action(intent, text)

        st.subheader("Final Output")
        st.write(result)

        st.session_state.messages.append({"role": "assistant", "content": result})
        save_history(st.session_state.messages)