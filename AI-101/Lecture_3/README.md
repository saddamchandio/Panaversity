# Lecture 3 — NEPRA Grid Code AI Assistant v2

## Live App

**https://huggingface.co/spaces/saddamchandio/NEPRA-Grid-Code-AI-Assistantv2**

---

## Description

The **NEPRA Grid Code AI Assistant v2** is a RAG-based (Retrieval-Augmented Generation) AI application that allows power sector engineers and compliance professionals to query Pakistan's **NEPRA Grid Code 2023** in natural language.

Instead of manually searching through hundreds of clauses, users type their question and receive a precise, source-verified answer citing the exact **clause number and page number** from the Grid Code document.

---

## How It Works

1. The NEPRA Grid Code 2023 PDF is chunked, embedded using `all-MiniLM-L6-v2`, and stored in a **ChromaDB** vector database.
2. On each query, the **top-5 most relevant chunks** are retrieved from the vector store.
3. A **LangChain HistoryAwareRetriever** reformulates follow-up questions using conversation history before retrieval.
4. The retrieved chunks are passed to **ChatGroq (openai/gpt-oss-20b)** with a system instruction to cite clause and page references.
5. The response is displayed in a **Streamlit** chat interface with full conversation history.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit 1.52.0 |
| LLM | ChatGroq — openai/gpt-oss-20b |
| Embeddings | sentence-transformers / all-MiniLM-L6-v2 |
| Vector Store | ChromaDB |
| Orchestration | LangChain 0.2.6 |
| Deployment | Hugging Face Spaces (Docker) |

---

## Files in This Folder

| File | Description |
|---|---|
| `L3_NEPRA_Grid_Code_AI_Report.docx` | Full development report — prompt iterations, architecture decisions, bugs, and solutions |
| `Lecture 3 Task.pdf` | Original assignment requirements |

---

## Real-World Problem Solved

Grid Code compliance queries are a daily operational need at System Operators, Distribution Companies, and transmission entities in Pakistan. Manual search takes 15–30 minutes per query. This assistant reduces it to under 10 seconds with source-verified answers.
