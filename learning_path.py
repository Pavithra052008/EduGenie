from gemini_client import generate_content


def create_learning_path(
    topic: str,
    level: str = "Beginner",
    goal: str = "Learn the basics"
) -> str:

    prompt = f"""
You are EduGenie, a personalized learning assistant.

Create a learning path for:

Topic:
{topic}

Student Level:
{level}

Learning Goal:
{goal}

Create a step-by-step learning roadmap.

Use this structure:

1. Prerequisites
2. Step 1
3. Step 2
4. Step 3
5. Step 4
6. Practice Activities
7. Mini Projects
8. Revision Plan
9. Final Goal

Make the learning path practical and easy to follow.
"""

    return generate_content(prompt)