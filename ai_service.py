
import requests


# --------------------------------------------------
# Groq API Configuration
# --------------------------------------------------

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

MODEL_NAME = "openai/gpt-oss-20b"


# --------------------------------------------------
# Generate AI Response
# --------------------------------------------------

def generate_response(system_prompt, user_input, api_key):
    """Generate an AI response using the Groq API."""

    if not api_key:
        raise ValueError(
            "Groq API key is missing. Check secrets.toml."
        )

    try:
        response = requests.post(
            GROQ_API_URL,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL_NAME,
                "messages": [
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_input,
                    },
                ],
                "stream": False,
            },
            timeout=90,
        )

        if response.status_code != 200:
            raise RuntimeError(
                f"Groq API error ({response.status_code}): "
                f"{response.text[:500]}"
            )

        result = response.json()

        content = (
            result.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
        )

        if not content or not content.strip():
            raise RuntimeError(
                "Groq returned an empty response."
            )

        return content.strip()

    except requests.exceptions.Timeout as exc:
        raise RuntimeError(
            "The Groq API took too long to respond."
        ) from exc

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(
            "Could not connect to the Groq API. "
            "Check your internet connection."
        ) from exc

    except ValueError as exc:
        if str(exc).startswith("Groq API key"):
            raise

        raise RuntimeError(
            "The Groq API returned an invalid response."
        ) from exc
