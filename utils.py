import openai

from config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY


def generate_response_from_prompt(prompt, max_token=50) -> str:
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=max_token,
        temperature=0.7,
    )

    return response.choices[0].text.strip()
