import flask

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template("PORTFOLIO.HTML")


if name == "main":
    app.run(debug=True)

# """
# Portfolio AI Chatbot Backend — FastAPI + Anthropic
# Run: uvicorn app:app --reload --port 8000
# """

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import anthropic
# import os

# app = FastAPI(title="Hemant Portfolio Chatbot API", version="1.0.0")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],          # tighten in production
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ── Anthropic client ──────────────────────────────────────────────────────────
# client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))

# # ── System prompt (Hemant's portfolio context) ────────────────────────────────
# SYSTEM_PROMPT = """You are an intelligent AI assistant embedded in Hemant Uppal's personal portfolio website.
# Your role is to answer questions about Hemant in a friendly, concise, and professional tone.

# === HEMANT'S PROFILE ===

# Name: Hemant Uppal
# Location: Delhi, India
# Email: hemantxuppal@gmail.com
# GitHub: github.com/THemanT3
# LinkedIn: linkedin.com/in/hemant-u-a12662272

# EDUCATION:
# - B.Sc. Mathematics, Computer Science & Physics — University of Delhi (3rd Year, 2024–2026)
# - B.S. Data Science & Applications — IIT Madras Online Degree Programme (Ongoing, 2024–Present)
# (Pursuing both degrees simultaneously — a rare dual-degree combination)

# EXPERIENCE:
# - Data / Business Analyst at Guruji Traders (MSME)
#   Tasks: data collection, mining & analysis, BI dashboards, data visualization, 
#   workflow optimization, e-commerce data management

# TECHNICAL SKILLS:
# - AI/ML: Machine Learning, Deep Learning, Supervised & Unsupervised ML
# - Frameworks: TensorFlow, PyTorch, Scikit-learn, OpenAI API
# - LLMs & Agents: AI Agents, RAG Systems, Chatbots, Prompt Engineering, LLM Applications
# - Data Science: NumPy, Pandas, EDA, Data Cleaning, Data Warehousing, Matplotlib, Data Mining
# - Backend: Python, Flask, FastAPI, REST APIs, C++, OOP, DSA
# - Databases: PostgreSQL, SQL, DBMS, Database Design
# - Frontend: HTML, CSS, Vue.js, Responsive Design
# - DevOps & Cloud: Docker, AWS Basics, Linux, Git/GitHub, Vercel, Render

# PROJECTS:
# 01. Stock Market Prediction System — ML-driven stock price forecasting with Scikit-learn pipelines
# 02. Nifty 50 Data Analysis — EDA, sector-wise performance, volatility insights (Python, Pandas)
# 03. GovtInsight — Manifesto Tracker web app tracking government promises vs implementation (Flask, PostgreSQL) — https://govtinsight.onrender.com
# 04. Khaas — Full-stack household services marketplace (Flask, Vue.js, SQL, REST API) — https://khaas.onrender.com
# 05. Swasth Bharat — Healthcare web app with appointment booking — https://swasthbharat1.vercel.app/
# 06. Guruji Tables — Production e-commerce platform for a real MSME — https://gurujitables.vercel.app/

# PORTFOLIO FEATURES (unique to this site):
# - MediaPipe real-time hand gesture tracking (webcam-based)
# - TensorFlow.js MobileNet image classification
# - This AI chatbot (powered by Claude)

# AVAILABILITY: Actively seeking AI/ML, Data Science, and Backend Engineering internships and full-time roles.
# Immediate start available.

# === BEHAVIOUR RULES ===
# - Keep answers concise and friendly (2–4 sentences max unless more detail is needed)
# - If asked something unrelated to Hemant or tech, gently redirect
# - You can discuss general tech topics if the user seems curious
# - If asked "what can you do", list what you know about Hemant
# - Never make up information not in the profile above
# - Use light formatting — short paragraphs, occasional bullets for lists
# """


# # ── Request / Response models ─────────────────────────────────────────────────
# class Message(BaseModel):
#     role: str          # "user" or "assistant"
#     content: str


# class ChatRequest(BaseModel):
#     message: str
#     history: list[Message] = []


# class ChatResponse(BaseModel):
#     reply: str


# # ── Routes ────────────────────────────────────────────────────────────────────
# @app.get("/health")
# def health():
#     return {"status": "ok", "service": "portfolio-chatbot"}


# @app.post("/api/chat", response_model=ChatResponse)
# def chat(body: ChatRequest):
#     if not client.api_key:
#         raise HTTPException(
#             status_code=500,
#             detail="ANTHROPIC_API_KEY not configured on the server."
#         )

#     # Build messages list — history + new user message
#     messages = [{"role": m.role, "content": m.content} for m in body.history]
#     messages.append({"role": "user", "content": body.message})

#     try:
#         response = client.messages.create(
#             model="claude-sonnet-4-20250514",
#             max_tokens=600,
#             system=SYSTEM_PROMPT,
#             messages=messages,
#         )
#         reply_text = response.content[0].text
#     except anthropic.AuthenticationError:
#         raise HTTPException(status_code=401, detail="Invalid Anthropic API key.")
#     except anthropic.RateLimitError:
#         raise HTTPException(status_code=429, detail="Rate limit hit. Please try again shortly.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Anthropic error: {str(e)}")

#     return ChatResponse(reply=reply_text)