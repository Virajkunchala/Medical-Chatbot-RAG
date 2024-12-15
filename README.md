# Building Agentic RAG with LlamaIndex and Gemini

## 🚀 Project Overview
This project demonstrates how to build an **Agentic Retrieval-Augmented Generation (RAG)** system using **LlamaIndex** for structured data retrieval and **Gemini** for advanced large language model (LLM) capabilities. By combining these tools, the system integrates dynamic data retrieval with agentic multi-step reasoning to solve complex queries in real time.

## 🧠 Key Features
- **Retrieval-Augmented Generation (RAG):** Leverages LlamaIndex to retrieve relevant context from external knowledge sources.
- **Agentic Behavior:** Utilizes a multi-agent architecture for task delegation and reasoning.
- **Real-Time Insights:** Supports dynamic querying and response generation with up-to-date knowledge.
- **Domain-Specific Expertise:** Fine-tuned for use cases in fields like healthcare, finance, and education.

## 🔧 Technologies Used
- **LlamaIndex:** Efficiently indexes and retrieves structured and unstructured data.
- **Gemini LLM:** Provides state-of-the-art language understanding and reasoning capabilities.
- **Python:** The primary programming language for development.

---

## 🛠️ Setup Instructions
Follow these steps to set up the project locally.

### Prerequisites
1. Python 3.8 or higher
2. Git

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo-name/agentic-rag-llamaindex-gemini.git
   cd agentic-rag-llamaindex-gemini
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**
   Create a `.env` file in the root directory and add the following:
   ```env
   LLAMA_INDEX_API_KEY=your_llamaindex_api_key
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. **Run the Application:**
   ```bash
   python main.py
   ```

6. **Access the Frontend:**
   Open `http://localhost:8501` in your browser to interact with the application.

---

## 🏗️ Project Architecture
```
├── data/
│   ├── knowledge_base/       # Raw data and documents for indexing
├── src/
│   ├── agents/               # Multi-agent logic and configurations
│   ├── index/                # LlamaIndex setup and query handlers
│   ├── llm/                  # Gemini API integration
│   ├── api/                  # FastAPI routes for backend
│   ├── ui/                   # Streamlit frontend
│   └── utils/                # Helper functions and utilities
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .env                      # Environment variables
```

---

## 📝 Usage Guide

### Step 1: Data Ingestion
1. Place your raw documents (e.g., PDFs, CSVs, text files) in the `data/knowledge_base/` directory.
2. Use LlamaIndex to preprocess and index the data:
   ```bash
   python src/index/create_index.py
   ```

### Step 2: Querying the System
Interact with the system via the Streamlit frontend or FastAPI endpoints:
- **Streamlit Interface:**
  Open the app in your browser to ask questions interactively.
- **API Endpoint:**
  Send a POST request to the `/query` endpoint with your query.
  ```bash
  curl -X POST http://localhost:8000/query -d '{"query": "What is the impact of X?"}'
  ```

### Step 3: Multi-Agent Workflow
Agents dynamically retrieve data, reason over it, and generate responses based on task-specific logic defined in `src/agents/`.
