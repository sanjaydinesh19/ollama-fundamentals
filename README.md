# 🧠 Ollama Fundamentals

A hands-on learning repository showcasing how to use [Ollama](https://ollama.com/) with Python for building local LLM applications.  
Includes examples of custom model usage, API integration, document RAG, and smart categorization.

---

## 📁 Project Structure

```
OLLAMA/
├── Scripts/
│ ├── 0_Custom_ModelFile.py # Basic config file for a custom Ollama model
│ ├── 1_ollama_api_call.py # Call Ollama via REST API
│ ├── 2_ollama_python_library.py # Use the Ollama Python 
│ ├── 3_ollama_custom_model.py # Load and use a custom model
│ ├── 4_ollama_categorizer.py # Categorize a grocery list using LLM
│ └── 5_ollama_pdf_rag.py # PDF-based RAG (Retrieval-Augmented Generation)
├── data/
│ ├── grocery_list.txt
│ ├── categorized_grocery_list.txt
│ └── DBMS.pdf
├── Image/
│ └── Image1.jpg
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sanjaydinesh19/ollama-fundamentals.git
cd ollama-fundamentals
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3.Install Dependencies
```bash
pip install -r requirements.txt
```

### 4.Start Ollama locally
Install Ollama from `https://ollama.com` and start it:
```bash
ollama run llama3.2
```

### 5. Tutorial to follow along
YouTube Link:
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/GWB9ApTPTv4)](https://www.youtube.com/watch?v=GWB9ApTPTv4)