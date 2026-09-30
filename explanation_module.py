from gemini_client import generate_content


def explain_topic(topic: str) -> str:

    prompt = f"""
You are EduGenie, an educational tutor.

Explain the following topic in a very simple and understandable way.

Topic:
{topic}

Follow this structure:

1. Simple Definition
2. Main Explanation
3. Important Points
4. Simple Example
5. Short Summary

Use easy English suitable for a beginner student.
Avoid unnecessary technical words.
"""

    return generate_content(prompt)