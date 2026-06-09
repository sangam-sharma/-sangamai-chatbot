# 🤖 SangamAI — Personal AI Assistant

A smart, conversational AI assistant built with **OpenAI GPT**, **LangChain**, and **Streamlit**. SangamAI can answer any question, help with writing, explain concepts, give advice, and much more — all while remembering the context of your conversation.

---

## 🚀 Live Demo

> Run locally by following the steps below

---

## ✨ Features

- 💬 **Conversational Memory** — remembers previous messages in the chat for context-aware responses
- 🧠 **Powered by GPT-3.5** — uses OpenAI's state-of-the-art language model
- 🦜 **LangChain Integration** — manages message history and prompt structure
- ⚡ **Streamlit UI** — clean, fast, and interactive web interface
- 🗑️ **Clear Chat** — reset the conversation anytime from the sidebar
- 🌐 **General Purpose** — ask anything, get helpful and friendly responses

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web UI framework |
| LangChain | LLM framework & memory management |
| OpenAI GPT-3.5 | Language model for responses |
| python-dotenv | Environment variable management |

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/sangam-sharma/-sangamai-chatbot.git
cd -sangamai-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the root folder and add:
```
OPENAI_API_KEY=your_openai_api_key_here
```
> Get your free API key at [platform.openai.com](https://platform.openai.com)

### 4. Run the app
```bash
streamlit run streamlit_app.py
```

### 5. Open in browser
Go to `http://localhost:8501` and start chatting! 🎉

---

## 📁 Project Structure

```
sangamai-chatbot/
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 🧠 How It Works

1. User types a message in the chat input
2. The message is added to the conversation history
3. LangChain builds a full message list including the system prompt and history
4. OpenAI GPT-3.5 generates a response based on the full context
5. The response is displayed and added to memory for future turns

---

## 🔮 Future Improvements

- [ ] Add support for multiple AI models (Gemini, Claude)
- [ ] Upload documents and chat with them (RAG)
- [ ] Voice input and output
- [ ] Deploy on Streamlit Cloud

---

## 👨‍💻 Author

**Sangam Sharma**
- GitHub: [@sangam-sharma](https://github.com/sangam-sharma)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with ❤️ using OpenAI, LangChain, and Streamlit
