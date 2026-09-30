from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import create_learning_path


# ==========================================
# Create FastAPI Application
# ==========================================

app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)


# ==========================================
# Templates and Static Files
# ==========================================

templates = Jinja2Templates(directory="templates")

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ==========================================
# Request Models
# ==========================================

class TextRequest(BaseModel):
    text: str


class QuizRequest(BaseModel):
    topic: str
    number_of_questions: int = 5


class LearningPathRequest(BaseModel):
    topic: str
    level: str = "Beginner"
    goal: str = "Learn the basics"


# ==========================================
# Home Page
# ==========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ==========================================
# Health Check
# ==========================================

@app.get("/health")
async def health():

    return {
        "status": "running",
        "application": "EduGenie"
    }


# ==========================================
# Q&A
# ==========================================

@app.post("/qa")
async def qa(request: TextRequest):

    try:

        if not request.text.strip():
            return {
                "success": False,
                "feature": "Q&A",
                "error": "Please enter a question."
            }

        result = answer_question(request.text)

        return {
            "success": True,
            "feature": "Q&A",
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "feature": "Q&A",
            "error": str(e)
        }


# ==========================================
# Explanation
# ==========================================

@app.post("/explain")
async def explain(request: TextRequest):

    try:

        if not request.text.strip():
            return {
                "success": False,
                "feature": "Explanation",
                "error": "Please enter a topic."
            }

        result = explain_topic(request.text)

        return {
            "success": True,
            "feature": "Explanation",
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "feature": "Explanation",
            "error": str(e)
        }


# ==========================================
# Quiz
# ==========================================

@app.post("/quiz")
async def quiz(request: QuizRequest):

    try:

        if not request.topic.strip():
            return {
                "success": False,
                "feature": "Quiz",
                "error": "Please enter a quiz topic."
            }

        if request.number_of_questions < 1:
            request.number_of_questions = 1

        if request.number_of_questions > 20:
            request.number_of_questions = 20

        result = generate_quiz(
            request.topic,
            request.number_of_questions
        )

        return {
            "success": True,
            "feature": "Quiz",
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "feature": "Quiz",
            "error": str(e)
        }


# ==========================================
# Summary
# ==========================================

@app.post("/summarize")
async def summarize(request: TextRequest):

    try:

        if not request.text.strip():
            return {
                "success": False,
                "feature": "Summary",
                "error": "Please enter some text to summarize."
            }

        result = summarize_text(request.text)

        return {
            "success": True,
            "feature": "Summary",
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "feature": "Summary",
            "error": str(e)
        }


# ==========================================
# Learning Path
# ==========================================

@app.post("/learn/recommendations")
async def learning_path(request: LearningPathRequest):

    try:

        if not request.topic.strip():
            return {
                "success": False,
                "feature": "Learning Path",
                "error": "Please enter a learning topic."
            }

        result = create_learning_path(
            request.topic,
            request.level,
            request.goal
        )

        return {
            "success": True,
            "feature": "Learning Path",
            "result": result
        }

    except Exception as e:

        return {
            "success": False,
            "feature": "Learning Path",
            "error": str(e)
        }