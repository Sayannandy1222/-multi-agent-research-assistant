<div align="center">

# 🚀 Multi-Agent Research Assistant

### Production-Grade Multi-Agent AI Research System built with LangGraph, FastAPI, Groq LLM, Tavily Search, Redis, Docker, GitHub Actions & Railway

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-blueviolet?style=for-the-badge)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Railway](https://img.shields.io/badge/Deployed-Railway-7B3FE4?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

### Intelligent AI Research powered by autonomous collaborating agents.

</div>

---

# 📌 Overview

The **Multi-Agent Research Assistant** is a production-ready AI application that autonomously researches complex topics by coordinating multiple specialized AI agents through a LangGraph workflow.

Instead of relying on a single LLM prompt, the system decomposes complex research problems into smaller tasks, delegates those tasks to specialized agents, gathers evidence from the web, synthesizes findings, and produces structured executive reports.

The project demonstrates modern AI engineering practices including:

- Multi-Agent Orchestration
- Graph-based AI Workflows
- Retrieval-Augmented Generation (RAG)
- Production FastAPI APIs
- Redis-based Caching
- Docker Containerization
- CI/CD Automation
- Cloud Deployment

---

# ✨ Features

## 🤖 Planner Agent

Responsible for:

- Understanding user intent
- Breaking complex research into smaller sub-problems
- Creating structured research plans

---

## 🔎 Researcher Agent

Responsible for:

- Searching the internet using Tavily Search API
- Extracting high-quality information
- Removing irrelevant content
- Producing structured research findings

---

## 📝 Writer Agent

Responsible for:

- Synthesizing all findings
- Eliminating duplicate information
- Producing executive-quality reports
- Formatting professional research summaries

---

## ⚡ LangGraph Workflow

The application uses LangGraph to orchestrate autonomous agent collaboration.

```
                 User Question
                       │
                       ▼
               Planner Agent
                       │
          Generates Research Plan
                       │
                       ▼
             Researcher Agent
      (Parallel Information Gathering)
                       │
                       ▼
                Writer Agent
                       │
                       ▼
              Final Research Report
```

---

# 🏗 Architecture

```
                   ┌──────────────────────┐
                   │      FastAPI API     │
                   └──────────┬───────────┘
                              │
                              ▼
                    LangGraph Workflow
                              │
     ┌──────────────┬──────────┴──────────┬──────────────┐
     ▼              ▼                     ▼
 Planner Agent  Research Agent      Writer Agent
     │              │                     │
     │              ▼                     │
     │        Tavily Search API           │
     │                                    │
     └──────────────┬─────────────────────┘
                    ▼
              Final Research Report
                    │
                    ▼
               Redis Cache
```

---

# ⚙ Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.12 |
| API Framework | FastAPI |
| AI Framework | LangGraph |
| LLM | Groq |
| Search Engine | Tavily Search |
| Validation | Pydantic |
| Cache | Redis |
| Deployment | Railway |
| CI/CD | GitHub Actions |
| Containerization | Docker |
| Testing | Pytest |

---

# 📂 Project Structure

```
app/
│
├── agents/
│   ├── planner.py
│   ├── researcher.py
│   └── writer.py
│
├── api/
│
├── cache/
│
├── core/
│
├── models/
│
├── prompts/
│
├── tools/
│
├── workflows/
│
└── main.py

tests/

Dockerfile

docker-compose.yml

requirements.txt

README.md
```

---

# 🚀 API Endpoints

## Root

```
GET /
```

Returns API information.

---

## Health Check

```
GET /health
```

Response

```json
{
  "status": "healthy",
  "service": "Multi-Agent Research Assistant"
}
```

---

## Research Endpoint

```
POST /research
```

Example Request

```json
{
    "question":"Compare OpenAI and Anthropic"
}
```

Example Response

```json
{
    "question":"Compare OpenAI and Anthropic",
    "report":"...",
    "cached":false
}
```

---

# ⚡ Caching

Redis is used to cache generated reports.

Benefits:

- Faster repeated queries
- Reduced LLM cost
- Lower API latency
- Better scalability

---

# 🐳 Docker

Run locally

```bash
docker compose up --build
```

---

# ☁ Cloud Deployment

The application is deployed on Railway.

Deployment includes:

- Docker
- Automatic GitHub Deployment
- Production Environment Variables
- Health Monitoring

---

# 🔄 CI/CD Pipeline

Every push to the **main** branch automatically triggers GitHub Actions.

Pipeline Steps

- Checkout Repository
- Setup Python
- Install Dependencies
- Execute Unit Tests
- Validate Docker Build
- Production Deployment

---

# 🧪 Testing

Run locally

```bash
pytest
```

Includes

- API Tests
- Workflow Tests
- Agent Tests
- Health Endpoint Tests

---

# 📈 Production Deployment

## Railway Deployment

![Railway Deployment](assets/railway-deployment-success.png)

---

## GitHub Actions

![GitHub Actions](assets/github-actions-success.png)

---

## Workflow History

![Workflow History](assets/github-actions-history.png)

---

# 🔮 Roadmap

- Streaming Responses (SSE)
- Multi-LLM Support
- PDF Report Export
- Vector Database Integration
- Agent Memory
- Human-in-the-loop Approval
- Async Agent Execution
- Observability Dashboard
- Multi-Tenant Authentication

---

# 💡 Engineering Highlights

This project demonstrates:

- Production-grade FastAPI development
- Multi-Agent AI architecture
- Graph-based workflow orchestration
- Retrieval-Augmented AI systems
- Cloud-native deployment
- Containerization
- Automated CI/CD
- Software engineering best practices

---

# 👨‍💻 Author

**Sayan Nandy**

AI Engineer • Generative AI • Multi-Agent Systems • LLM Applications • AI Infrastructure

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐

It helps the project reach more developers.

---