# -Knowledge-Assistant-RAG-Based-Chatbot

# RAG Chatbot with LangChain, Hugging Face, and Streamlit

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that combines **semantic search** over your own data with the reasoning capabilities of a **language model** (LLM). It intelligently routes user queries either to a knowledge retriever (e.g., for factual or document-based answers) or to a generative model (e.g., for creative or open-ended queries).

---

## 📚 What This Project Is About

In traditional chatbots, either you're limited to the knowledge in the documents or rely entirely on an LLM that may hallucinate. This hybrid chatbot solves that by combining the best of both:

- 🧠 **Retrieval-Based QA**: Answers factual/document-based queries using vector search over custom documents.
- ✨ **LLM-Based QA**: Handles creative, abstract, or open-ended queries using a Hugging Face-hosted LLM.

This project can serve as:
- A personal knowledge assistant
- A documentation query tool
- A customer service prototype
- A boilerplate for more advanced agentic workflows

---

## 🛠️ Technologies Used

| Tech            | Purpose                                      |
|-----------------|----------------------------------------------|
| **LangChain**   | RAG pipeline, chains, and prompt management  |
| **Hugging Face**| Hosted LLMs via Inference API                |
| **FAISS**       | Vector similarity search                     |
| **HuggingFace** | For embeddings                      |
| **Streamlit**   | Web interface for chat interaction           |
| **dotenv**      | Securely load API keys from `.env` file      |
| **Python**      | Backend and integration logic                |

---

## ⚙️ How It Works

### 1. 📥 Input Query
User submits a query via the Streamlit chat UI.

### 2. 🚦 Query Routing
The system routes the query to:
- **RetrieverQA** if it's factual (e.g., "What is LangChain?")
- **LLM** if it's generative (e.g., "Write a poem about AI")

### 3. 📄 Vector Search (if factual)
The retriever searches custom documents using FAISS and embeddings to find the most relevant context.

### 4. 🤖 LLM Inference
Based on the route:
- Hugging Face model generates the response using its API
- LangChain chains format and parse the output

### 5. 💬 Response
Streamlit displays the answer to the user.

---
