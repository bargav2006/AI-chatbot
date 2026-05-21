# 🏏 IPL Cricket Expert Chatbot

A Streamlit chatbot powered by **Groq** (`llama-3.3-70b-versatile`) — ultra-fast responses, completely free tier available.

---

## 📁 Project structure

```
ipl_chatbot/
├── app.py                  ← Main Streamlit app
├── ipl_data.py             ← Teams, winners, records, quick chips
├── ipl_system_prompt.py    ← LLM system prompt
├── requirements.txt        ← streamlit + groq
├── .gitignore
└── .streamlit/
    ├── config.toml         ← IPL gold & navy theme
    └── secrets.toml        ← 🔑 Your Groq API key (not committed)
```

---

## ⚡ Quick start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add your Groq API key
Edit `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_YOUR_KEY_HERE"
```
Get a **free** key at → https://console.groq.com/keys

### 3. Run
```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Community Cloud (free)

1. Push repo to GitHub (secrets.toml is gitignored).
2. Go to https://share.streamlit.io → New app → select `app.py`.
3. Under **Advanced settings → Secrets**, paste:
   ```toml
   GROQ_API_KEY = "gsk_YOUR_KEY_HERE"
   ```
4. Click **Deploy**.

---

## 🔧 Change the model

In `app.py`, update the `model=` parameter:

| Model | Speed | Notes |
|---|---|---|
| `llama-3.3-70b-versatile` | Fast ✅ | Best quality, default |
| `llama3-8b-8192` | Fastest | Lighter, good for simple queries |
| `mixtral-8x7b-32768` | Fast | Larger context window |
| `gemma2-9b-it` | Fast | Google Gemma 2 via Groq |

Full model list → https://console.groq.com/docs/models

---

## 📚 References

| Resource | URL |
|---|---|
| Groq API docs | https://console.groq.com/docs |
| Groq Python SDK | https://github.com/groq/groq-python |
| Streamlit docs | https://docs.streamlit.io |
| IPL official | https://www.iplt20.com |