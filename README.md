# EduGenie

## Google Gemini Powered Learning Assistant

EduGenie is a Generative AI based educational assistant.

It provides:

- Question and Answer
- Topic Explanation
- Quiz Generation
- Text Summarization
- Personalized Learning Path

## Technologies

- Python
- FastAPI
- Google Gemini
- HTML
- CSS
- Jinja2
- Uvicorn

## Project Structure

EduGenie/

├── main.py
├── gemini_client.py
├── qna.py
├── explanation_module.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── test_api.py
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

## Installation

Open the EduGenie folder in VS Code.

Create a virtual environment:

python -m venv .venv

Install the dependencies:

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

## API Key

Open the .env file.

Add your Gemini API key:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE

## Run the Application

Run:

.\.venv\Scripts\python.exe -m uvicorn main:app --reload

Open:

http://127.0.0.1:8000

## API Documentation

FastAPI documentation:

http://127.0.0.1:8000/docs

## Health Check

Open:

http://127.0.0.1:8000/health

## Testing

Run:

.\.venv\Scripts\python.exe -m pytest -q