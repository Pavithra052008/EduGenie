import os
import time
from dotenv import load_dotenv
from google import genai


# Load .env
load_dotenv()


# Gemini API Key
API_KEY = os.getenv("GEMINI_API_KEY")


# Try models one by one
MODELS = [
    "gemini-3.7-flash",
    "gemini-3.8-flash",
    "gemini-3.6-flash",
    "gemini-3.5-flash",
    "gemini-3.5-flash-lite"
]


def get_client():
    """
    Create Gemini client.
    """

    if not API_KEY:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Please add your Gemini API key to the .env file."
        )

    return genai.Client(
        api_key=API_KEY.strip()
    )


def generate_content(prompt: str) -> str:
    """
    Generate response from Gemini.

    Tries multiple models and retries temporary
    503/429/network errors.
    """

    client = get_client()

    last_error = None

    for model in MODELS:

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=prompt
                )

                if response.text:
                    return response.text.strip()

                raise ValueError(
                    f"Empty response from {model}"
                )

            except Exception as error:

                last_error = error

                error_text = str(error)

                temporary_error = (
                    "503" in error_text
                    or "UNAVAILABLE" in error_text
                    or "429" in error_text
                    or "RESOURCE_EXHAUSTED" in error_text
                    or "SSL" in error_text
                    or "EOF" in error_text
                    or "Connection" in error_text
                )

                if temporary_error:

                    if attempt < 2:
                        wait_time = 2 ** attempt
                        time.sleep(wait_time)
                        continue

                    break

                raise error


    raise RuntimeError(
        "Gemini is temporarily unavailable. "
        f"Last error: {last_error}"
    )