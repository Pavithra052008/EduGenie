from gemini_client import generate_content


def summarize_text(text: str) -> str:

    prompt = f"""
You are EduGenie, an educational summarization assistant.

Summarize the following text for a college student.

Text:
{text}

Instructions:
- Keep the important information.
- Remove unnecessary repetition.
- Use simple English.
- Use bullet points when useful.
- Make the summary easy to study.
- End with a short key-points section.
"""

    return generate_content(prompt)