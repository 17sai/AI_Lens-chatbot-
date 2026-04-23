# 🧠 AI News Chatbot

A real-time AI-powered news chatbot that scrapes live news data, stores it locally, retrieves relevant information based on user queries, and generates structured responses using an LLM.

---

## 🚀 Overview

The **AI News Chatbot** is an end-to-end intelligent system that enables users to query the latest news across multiple categories such as sports, business, technology, and India.

Instead of relying on static datasets, the system dynamically scrapes news from online sources, ensuring up-to-date and relevant information. It combines **web scraping, database storage, retrieval-based context generation, and LLM-powered responses** into a single seamless application.

---

## ❓ Problem Statement

Traditional news platforms provide static browsing experiences where users must manually search and filter content.

This project aims to solve:

* ❌ Difficulty in quickly accessing relevant news
* ❌ Lack of conversational interfaces for news querying
* ❌ Dependency on outdated or static datasets
* ❌ Inefficient filtering across categories

### ✅ Solution

Build an **AI-powered chatbot** that:

* Accepts natural language queries
* Retrieves relevant news dynamically
* Provides structured, concise responses
* Works in real-time with continuously updated data

---

## 🏗️ Architecture

<img width="753" height="1024" alt="image" src="https://github.com/user-attachments/assets/786a3326-3b2d-4905-8518-7ae69490669a" />

### 🔁 Data Flow

1. News is scraped from Times of India
2. Data is stored in a SQLite database
3. User enters a query
4. MCP decides to use the news retrieval tool
5. Retriever fetches relevant articles
6. Context is passed to LLM
7. LLM formats structured response
8. Response is displayed in Streamlit UI

---

## ⚙️ Tech Stack

### 🖥️ Frontend

* Streamlit

### ⚙️ Backend (Integrated in App)

* Python

### 🧠 AI / LLM

* Groq API (LLaMA 3 / Mixtral models)

### 🗄️ Database

* SQLite

### 🌐 Web Scraping

* Requests
* BeautifulSoup

### 🔧 Other Tools

* dotenv (for API key management)
* Git & GitHub
* Hugging Face Spaces (Deployment)

---

## ✨ Features

* 🔍 Natural language news querying
* 📰 Real-time news scraping
* 📂 Category-based filtering (Sports, Business, Technology, India)
* ⚡ Fast retrieval using keyword expansion
* 🤖 LLM-powered structured responses
* 🔗 Clickable news links
* 💬 Chat-style interface
* ☁️ Deployed on Hugging Face

---

## 📦 Project Structure

```
AI_LENS/
│
├── app/
│   ├── database.py
│   ├── scraper.py
│   ├── retriever.py
│   ├── mcp.py
│   ├── functions.py
│   ├── llm.py
│   └── __init__.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Deployment

The application is deployed using **Hugging Face Spaces** with Streamlit.

---

## 🔮 Future Improvements

* 🔄 Auto-refresh news without user interaction
* 🌍 Multi-source news aggregation
* 🧾 Article summarization
* 📊 Trending topics dashboard
* 🧠 Improved semantic search (embeddings)

---

## 📌 Key Learnings

* End-to-end AI system design
* Retrieval-Augmented Generation (RAG) concepts
* LLM grounding to prevent hallucination
* Real-time data pipeline integration
* Deployment of AI applications

---

## 👨‍💻 Author

Developed by **Sai Santosh**

---
