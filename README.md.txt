# 🤖 SalesMind AI Enterprise

An AI-powered Business Intelligence Platform built using **Generative AI, Retrieval-Augmented Generation (RAG), Local LLMs, and Interactive Analytics**.

SalesMind AI helps businesses analyze sales data, generate executive reports, and query company knowledge using natural language.

---

# 🚀 Features

- 📊 Interactive Sales Dashboard
- 💬 AI Business Analyst
- 📚 Company Knowledge Assistant (RAG)
- 📄 PDF Upload & Semantic Search
- 🧠 ChromaDB Vector Database
- 🤖 Local LLM using Ollama + Qwen3
- 📄 AI Executive Report Generator
- 📥 PDF Report Export
- 🎯 Multi-page Streamlit Interface

---

# 🏗 System Architecture

```
            Sales CSV
                 │
                 ▼
        Sales Analytics Engine
                 │
                 ▼
         AI Business Analyst
                 │
                 ▼
          Ollama (Qwen3)

────────────────────────────────

            Company PDF
                 │
                 ▼
           PDF Loader
                 │
                 ▼
         Text Splitter
                 │
                 ▼
      HuggingFace Embeddings
                 │
                 ▼
            ChromaDB
                 │
                 ▼
            RAG Retriever
                 │
                 ▼
          Ollama (Qwen3)
```

---

# 🛠 Tech Stack

## Programming

- Python

## Frontend

- Streamlit

## AI / LLM

- Ollama
- Qwen3
- LangChain

## RAG

- ChromaDB
- Sentence Transformers
- PyPDF

## Data

- Pandas
- NumPy

## Reports

- ReportLab

---

# 📂 Project Structure

```
SalesMind_AI/

├── app.py
├── ui_pages/
├── modules/
├── vector_db/
├── notebooks/
├── requirements.txt
└── README.md
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/naitiksoni14/SalesMind-AI.git
```

Go inside the folder

```bash
cd SalesMind-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 🎯 Key AI Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Vector Databases
- Semantic Search
- Local LLM Deployment
- Prompt Engineering
- AI Business Analysis
- Executive Report Generation

---

# 📸 Screenshots

(Add screenshots here after deployment.)

---

# 🔮 Future Improvements

- SQL Database Integration
- Multi-user Authentication
- Cloud Deployment
- Chat History
- Voice Assistant
- Dashboard Forecasting
- AI Agents

---

# 👨‍💻 Author

**Naitik Soni**

Aspiring Generative AI Engineer

GitHub:
https://github.com/naitiksoni14
