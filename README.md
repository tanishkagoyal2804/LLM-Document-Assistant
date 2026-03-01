# 📄 LLM-Powered AI Assistant for Documents

An AI-powered document assistant that allows users to upload documents (PDFs) and ask natural language questions about the content.  
The system uses Retrieval-Augmented Generation (RAG) to provide accurate, context-aware answers.

---

## 🚀 Project Overview

This project enables users to:

- Upload one or multiple PDF documents
- Extract and process document content
- Generate vector embeddings
- Store embeddings using FAISS
- Ask questions in natural language
- Get AI-generated answers based only on document content

The system ensures context-aware and document-grounded responses using a Retrieval-Augmented Generation pipeline.

---

## 🧠 Technologies Used

- Python
- Streamlit (Frontend UI)
- LangChain
- OpenAI API
- FAISS (Vector Store)
- PyPDF
- dotenv

---

## 🏗 Project Architecture

1. Document Upload (PDF)
2. Text Extraction
3. Text Chunking
4. Embedding Generation
5. Vector Storage (FAISS)
6. Similarity Search
7. LLM-based Answer Generation

---

## 📂 Project Structure
LLM-Document-Assistant/
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── .env
├── data/
└── README.md
## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Add OpenAI API Key

Create a `.env` file:


OPENAI_API_KEY=your_api_key_here


### 5️⃣ Run Application


python -m streamlit run app.py


Open browser at:


http://localhost:8501


---

## 📊 Features

- ✅ Multi-document upload support
- ✅ Intelligent chunking strategy
- ✅ Vector similarity search
- ✅ Context-aware responses
- ✅ Clean Streamlit interface
- ✅ Secure API key handling with dotenv

---

## 🎯 Business Use Case

This system can be used for:

- Legal document analysis
- Academic research assistance
- Policy document review
- Internal company knowledge base
- Resume and CV analysis
- Enterprise document Q&A systems

---

## 📈 Key Highlights

- Implemented Retrieval-Augmented Generation (RAG)
- Reduced hallucination by grounding responses in document context
- Built scalable vector storage using FAISS
- Designed interactive UI using Streamlit

---

![screenshot](https://github.com/tanishkagoyal2804/LLM-Document-Assistant/blob/master/Screenshot%202026-03-01%20163656.png)
![screenshot](https://github.com/tanishkagoyal2804/LLM-Document-Assistant/blob/master/Screenshot%202026-03-01%20163745.png).
![screenshot](https://github.com/tanishkagoyal2804/LLM-Document-Assistant/blob/master/Screenshot%202026-03-01%20163755.png)

👩‍💻 Author

Tanishka Goyal  
