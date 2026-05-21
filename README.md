# Research Paper Assistant using RAG

A Retrieval-Augmented Generation (RAG) based research assistant that 
allows users to query research papers using natural language.

## Features

- Upload and process research papers (PDFs)
- Semantic search using vector embeddings
- Context-aware question answering
- Fast document retrieval
- Streamlit-based user interface

## Tech Stack

- Python
- Streamlit
- LangChain
- ChromaDB
- OpenAI / HuggingFace Embeddings
- FAISS / Chroma Vector Store

## Project Structure

```bash
research-rag/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
│
├── data/
│   └── research papers
│
├── utils/
│   ├── embeddings.py
│   ├── llm.py
│   ├── loader.py
│   ├── retriever.py
│   └── splitter.py
│
└── vectordb/
```

## How It Works

1. PDFs are loaded and split into chunks
2. Chunks are converted into embeddings
3. Embeddings are stored in ChromaDB
4. User queries are embedded
5. Similar chunks are retrieved
6. Retrieved context is sent to the LLM
7. LLM generates a contextual answer

## Installation

Clone the repository:

```bash
git clone https://github.com/sao-preksha/Research-RAG.git
cd Research-RAG
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Ingest documents:

```bash
python ingest.py
```

Run application:

```bash
streamlit run app.py
```

## Future Improvements

- Multi-document querying
- Citation generation
- Conversational memory
- Hybrid search
- Research summarization
- PDF upload from UI

## Author

Preksha Sao
