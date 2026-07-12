# 🤖 Smart Research Assistant

An AI-powered Smart Research Assistant built using **Hybrid RAG**, **Groq LLM**, **FAISS**, and **BM25**. The application allows users to upload multiple PDF documents and ask natural language questions to receive context-aware answers with source references.

---

## 🚀 Features

- 📄 Upload multiple PDF documents
- 💬 Chat with PDFs using Natural Language
- 🔍 Hybrid Retrieval (FAISS + BM25)
- 🧠 Conversational Memory
- 📑 Source References for every answer
- 📚 Multi-document Question Answering
- 📝 Document Summarization
- ⚖️ Compare Multiple Documents
- ⚡ Fast responses using Groq LLM
- 🎨 Modern Streamlit User Interface

---

## 🛠 Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### LLM
- Groq (Llama 3)

### Embeddings
- Sentence Transformers
- all-MiniLM-L6-v2

### Retrieval
- FAISS
- BM25

### Libraries
- LangChain
- HuggingFace
- PyPDFLoader

---

## 📂 Project Structure

```
Smart-Research-Assistant/
│
├── app.py
├── config.py
├── database.py
├── chat_manager.py
├── requirements.txt
├── README.md
│
├── llm/
│   └── groq.py
│
├── prompts/
│   └── prompt.py
│
├── utils/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── rag_pipeline.py
│   ├── hybrid_retriever.py
│   ├── query_router.py
│   └── memory.py
│
├── data/
├── vectorstore/
└── styles.css
```

---

## ⚙ Installation

Clone the repository

```bash
git clone <repository-url>
```

Move to project folder

```bash
cd Smart-Research-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
streamlit run app.py
```

---

## 📸 Application Workflow

1. Upload one or more PDF files.
2. Documents are split into chunks.
3. Embeddings are generated.
4. FAISS Vector Store is created.
5. BM25 performs keyword retrieval.
6. Hybrid Retrieval combines semantic and keyword search.
7. Relevant chunks are passed to Groq LLM.
8. The assistant generates answers with source references.

---

## 🎯 Example Questions

- Summarize both documents.
- Compare the uploaded reports.
- What is Artificial Intelligence?
- Explain the report in simple language.
- Give the key findings.
- What challenges are discussed?

---

## 🔮 Future Improvements

- User Authentication
- Persistent Chat History
- Cloud Database Integration
- PDF Highlighting
- Voice-based Interaction
- Image Understanding
- Web Search Integration

---

## 👨‍💻 Author

**Himanshu Bansal**

B.Tech Information Technology

JECRC Foundation, Jaipur

---

## ⭐ If you like this project, consider giving it a star.