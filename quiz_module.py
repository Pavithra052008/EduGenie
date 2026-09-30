from gemini_client import generate_content


def generate_quiz(topic: str, number_of_questions: int = 5) -> str:

    if number_of_questions < 1:
        number_of_questions = 1

    if number_of_questions > 20:
        number_of_questions = 20

    prompt = f"""
You are EduGenie, an educational quiz generator.

Create {number_of_questions} multiple-choice questions
about the following topic:

Topic:
{topic}

For every question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:

Rules:
- Questions must be educational.
- Use clear English.
- Give exactly one correct answer.
- Make incorrect options plausible.
- Include the correct answer and a short explanation.
"""

    return generate_content(prompt)