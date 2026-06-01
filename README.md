# 📚 PDF RAG Assistant

An AI-powered PDF Question Answering System built using **Streamlit, FAISS, Sentence Transformers, and Google Gemini**.

Upload a PDF document and ask questions in natural language. The application retrieves the most relevant content from the PDF and generates accurate answers using Retrieval-Augmented Generation (RAG).

---

# 🚀 Features

* 📄 Upload PDF documents
* 💬 ChatGPT-style conversational interface
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* ⚡ Fast similarity search using FAISS
* 🤖 Powered by Google Gemini
* 📝 Chat history support
* 🔄 Automatic PDF processing
* 📚 Context-aware question answering
* 🎯 Relevant chunk retrieval
* 🖥️ Interactive Streamlit UI

---

# 🏗️ System Architecture

```text
                ┌─────────────────┐
                │   Upload PDF    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Extraction │
                │     (PyPDF)     │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Text Chunking   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Embeddings      │
                │ MiniLM-L6-v2    │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ FAISS Vector DB │
                └────────┬────────┘
                         │
                         ▼

            User Question
                    │
                    ▼

         ┌─────────────────────┐
         │ Query Embedding     │
         └──────────┬──────────┘
                    │
                    ▼

         ┌─────────────────────┐
         │ Similarity Search   │
         │     (FAISS)         │
         └──────────┬──────────┘
                    │
                    ▼

         ┌─────────────────────┐
         │ Top Relevant Chunks │
         └──────────┬──────────┘
                    │
                    ▼

         ┌─────────────────────┐
         │ Google Gemini LLM   │
         └──────────┬──────────┘
                    │
                    ▼

         ┌─────────────────────┐
         │ Generated Answer    │
         └─────────────────────┘
```

---

# 🔄 Workflow

### Step 1: Upload PDF

The user uploads a PDF document through the Streamlit interface.

### Step 2: Extract Text

Text is extracted from all PDF pages using PyPDF.

### Step 3: Chunking

Large text is divided into overlapping chunks.

Example:

```text
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

This helps preserve context during retrieval.

### Step 4: Create Embeddings

Each chunk is converted into a numerical vector representation using:

```text
all-MiniLM-L6-v2
```

### Step 5: Store in FAISS

All embeddings are stored inside a FAISS vector index.

### Step 6: User Asks a Question

The user enters a natural language query.

Example:

```text
What are the stages of cognition?
```

### Step 7: Semantic Search

The question is converted into an embedding.

FAISS retrieves the most relevant chunks.

### Step 8: Context Construction

Retrieved chunks are combined into a single context.

### Step 9: Gemini Response Generation

The context and question are sent to Google Gemini.

### Step 10: Final Answer

Gemini generates a context-aware answer based on retrieved information.

---

# 🧠 RAG Pipeline

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embeddings
 ↓
FAISS
 ↓
Question
 ↓
Embedding
 ↓
Retrieval
 ↓
Relevant Context
 ↓
Gemini
 ↓
Answer
```

---

# 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### PDF Processing

* PyPDF

### Embedding Model

* Sentence Transformers
* all-MiniLM-L6-v2

### Vector Database

* FAISS

### Large Language Model

* Google Gemini 2.5 Flash

### Deployment

* Render / Streamlit Cloud / Hugging Face Spaces

---

# 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd pdf-rag-assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your Gemini API key from:

https://aistudio.google.com

---

# ▶️ Run Locally

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
pdf-rag-assistant/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
└── assets/
```

---

# ⚠️ Current Limitations

* Works best with text-based PDFs
* Scanned PDFs are not fully supported
* OCR is not implemented
* Diagram understanding is limited
* Image-heavy PDFs may reduce answer quality

---

# 🔮 Future Improvements

* OCR Support
* Multi-PDF Chat
* Hybrid Search
* Reranking
* Source Citations
* Page References
* Conversational Memory
* Multimodal RAG
* Image Understanding
* Knowledge Base Persistence

---

# 📊 Performance Optimizations

* Cached embedding model
* Session state management
* Overlapping chunk strategy
* FAISS vector indexing
* Retrieval-based context generation

---

# 🎯 Use Cases

* Academic PDFs
* Lecture Notes
* Technical Documentation
* Research Papers
* Company Manuals
* Study Materials
* Knowledge Base Systems

---

# 👨‍💻 Author

Siva Anand

AI | Machine Learning | Generative AI | RAG Systems

---

# ⭐ If you like this project

Give it a star and share your feedback.
