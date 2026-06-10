# 🦙 LocalChat — ChatGPT Clone with Ollama

A fully local ChatGPT clone built with **Python** and **Streamlit**.  
Runs 100% on your machine — no API keys, no cloud, no cost, completely private.

---

## 📸 Features

- 💬 **Real-time streaming** — responses appear word by word
- 🔄 **Multiple AI models** — switch between llama3, mistral, codellama and more
- ⚙️ **Custom system prompt** — give the AI any personality you want
- 🗑️ **Clear chat** — reset the conversation anytime
- 🔒 **100% Private** — your data never leaves your machine

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Programming language |
| Streamlit | Web UI framework |
| Ollama | Run AI models locally |
| llama3 | Default AI model |

---

## ⚡ Quick Start

### 1. Install Ollama
Download from https://ollama.com and pull a model:
```bash
ollama pull llama3
```

### 2. Clone this repository
```bash
git clone https://github.com/ashreyasureddy/my-chatbot.git
cd my-chatbot
```

### 3. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the app
```bash
# Terminal 1 — Start Ollama
ollama serve

# Terminal 2 — Start the app
streamlit run chat.py
```

### 6. Open in browser
```
http://localhost:8501
```

---

## 🤖 Supported Models

| Model | Best For | Size |
|---|---|---|
| `llama3` | General chat | 4GB |
| `mistral` | Fast & smart replies | 4GB |
| `codellama` | Coding help | 4GB |
| `phi3` | Quick responses | 2GB |
| `gemma` | General use | 5GB |

Download any model with:
```bash
ollama pull <model-name>
```

---

## 💡 System Prompt Examples

Change the AI personality from the sidebar:

**Python Tutor:**
```
You are a Python programming tutor. Explain everything 
in simple terms with code examples.
```

**Career Coach:**
```
You are an expert career coach. Help users with resume 
writing, interview tips, and career advice.
```

**Funny Assistant:**
```
You are a funny assistant who answers every question 
with a joke first, then the real answer.
```

---

## 📋 Requirements

- Python 3.10+
- Ollama 0.3+
- 8GB RAM minimum
- 5GB free disk space

---

## 👨‍💻 Author

Built by **Ashreya Sureddy**  
GitHub: https://github.com/ashreyasureddy

---

## ⭐ If you found this useful, give it a star on GitHub!
