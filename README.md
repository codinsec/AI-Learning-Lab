# AI Learning Lab

A comprehensive, structured learning path for becoming a production-ready AI Engineer, GenAI Engineer, and Agentic AI System Builder.

## 🎯 Purpose

This repository is designed to transform you from a developer into a **production-ready AI Engineer**. Unlike tutorial collections or notebook-only learning, this lab focuses on:

- **Engineering intuition** over mathematical proofs
- **Production-ready code** over research experiments
- **System thinking** over isolated examples
- **Real-world applications** over toy problems

## 📚 Learning Path

The curriculum is organized into 7 sequential sections, each building on the previous:

### 01-Python-Math-Fundamentals
**Python & Math Fundamentals** (Months 1-2)

Master modern Python at an AI Engineer level:
- Async/await for IO-bound LLM API calls
- Threading vs Multiprocessing for CPU-bound operations
- Decorators, Context Managers, Type Hints
- NumPy, Pandas, and tensor logic
- Essential linear algebra, calculus, and statistics for AI

### 02-Machine-Learning
**Machine Learning Basics** (Months 3-4)

Understand ML fundamentals without becoming a data scientist:
- Scikit-learn pipelines
- Overfitting/underfitting concepts
- Feature engineering principles
- Train/validation/test separation

### 03-Deep-Learning
**Deep Learning & PyTorch** (Months 3-4)

Build deep learning intuition:
- Tensor lifecycle (CPU ↔ GPU)
- Autograd and training loops
- CNN and Transformer architectures
- Pretraining vs Fine-tuning
- LoRA/PEFT for efficient adaptation

### 04-LLM-Generative-AI
**LLM & Generative AI** (Months 5-6)

Master the foundation of modern AI:
- Prompt engineering (zero-shot, few-shot, CoT)
- Tokenization and context windows
- Cost and latency optimization
- Prompt versioning and management

### 05-RAG-Systems
**RAG Systems** (Months 5-6)

Build production-ready retrieval systems:
- Chunking strategies
- Embedding model selection
- Hybrid search (BM25 + vector)
- Re-ranking with cross-encoders
- Vector databases (Chroma, Pinecone, Weaviate)
- Caching and multi-tenant architectures

### 06-Agentic-AI
**Agentic AI** (Months 7-9)

Build autonomous AI systems:
- Tool calling and function calling
- API orchestration
- LangGraph, CrewAI, AutoGen frameworks
- State and memory management
- Human-in-the-loop patterns

### 07-Production-MLOps
**Production, MLOps & AI Security** (Months 10+)

Ship production AI systems:
- FastAPI model serving
- Streaming responses (SSE)
- Model optimization (quantization, GGUF)
- Monitoring and tracing (LangSmith)
- AI security (prompt injection, jailbreak prevention)
- Docker, Kubernetes, CI/CD

## 🏗️ Repository Structure

```
AI-Learning-Lab/
├── 01-Python-Math-Fundamentals/
│   └── <project-folder>/
│       ├── README.md
│       ├── requirements.txt
│       └── <code files>
├── 02-Machine-Learning/
│   └── <project-folder>/
│       ├── README.md
│       ├── requirements.txt
│       └── <code files>
├── ... (other sections)
├── requirements.txt          # Common dependencies
└── README.md                # This file
```

**⚠️ Important:** The folder structure is **FINAL** and must not be changed. All code must be placed in the appropriate section's subfolder.

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd AI-Learning-Lab
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Navigate to a section:**
   ```bash
   cd 01-Python-Math-Fundamentals/<project-folder>
   pip install -r requirements.txt  # Install section-specific dependencies
   ```

4. **Follow the learning path sequentially:**
   - Start with section 01
   - Complete all projects in a section before moving to the next
   - Read each project's README.md for context and instructions

## 📖 How to Use This Lab

### For Each Section:
1. Read the section's README.md for learning objectives
2. Explore the project subfolders
3. Read each project's README.md
4. Study the code examples
5. Run and experiment with the code
6. Complete any exercises or challenges

### Learning Principles:
- **Sequential progression:** Don't skip ahead
- **Hands-on practice:** Run every example
- **Engineering focus:** Think about production implications
- **Minimal dependencies:** Each project uses only what's necessary

## 🛠️ Technology Stack

- **Language:** Python 3.10+
- **ML/DL:** PyTorch, Scikit-learn
- **LLM:** OpenAI API, Hugging Face Transformers
- **RAG:** LangChain, Vector Databases
- **Agents:** LangGraph, CrewAI
- **Production:** FastAPI, Docker, Kubernetes
- **Monitoring:** LangSmith

## 📝 Project Standards

Every project folder includes:
- **README.md** - Learning objectives, explanations, and how to run
- **requirements.txt** - Python dependencies (minimal and version-pinned)
- **Code files** - Clean, well-commented, production-oriented examples

## ⚠️ Important Rules

1. **Never modify the folder structure** - It's designed for sequential learning
2. **Follow the progression order** - Each section builds on previous knowledge
3. **Keep code minimal** - Focus on learning, not feature bloat
4. **Production mindset** - Think about real-world deployment from day one

## 🤝 Contributing

This is a structured learning lab. If you find errors or have suggestions:
1. Follow the git workflow defined in `.cursorrules`
2. Create feature branches for each section
3. Maintain clean commit history

## 📄 License

See [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Barbaros Kaymak**

Created by [Codinsec](https://codinsec.com) | [info@codinsec.com](mailto:info@codinsec.com)

---

**Remember:** This lab produces **AI Engineers**, not tutorial collectors. Focus on understanding, building, and shipping production systems.

