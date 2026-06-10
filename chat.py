import streamlit as st
import requests, json

st.set_page_config(page_title="LocalChat", page_icon="🦙")
st.title("🦙 LocalChat")
st.caption("Running locally with Ollama — private & free")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox("Model", ["llama3", "mistral", "codellama", "gemma"])
    system_prompt = st.text_area(
        "System Prompt",
        value="You are a helpful, friendly AI assistant.",
        height=100
    )
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Message LocalChat..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_reply = ""

        messages_payload = [
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ]

        try:
            response = requests.post(
                "http://localhost:11434/api/chat",
                json={"model": model, "messages": messages_payload, "stream": True},
                stream=True, timeout=120
            )

            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    token = data.get("message", {}).get("content", "")
                    full_reply += token
                    placeholder.markdown(full_reply + "▌")

            placeholder.markdown(full_reply)

        except Exception as e:
            full_reply = f"⚠️ Error: {e}"
            placeholder.error(full_reply)

    st.session_state.messages.append({"role": "assistant", "content": full_reply})