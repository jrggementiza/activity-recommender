import openai

from config import OPENAI_API_KEY


openai.api_key = OPENAI_API_KEY


def get_matching_seasons(country: str):
    prompt = f"Given a {country}, what are that country's seasons. Just the season type, no need to specify months covered. Simplify the season naming. Like Dry, Rainy, Winter, Spring, Summer, Fall. Not Rainy Season, Dry Season, Winter Season. Make sure the seasons are correct for {country}. Expected output examples: 'winter, spring, summer, fall' or 'rainy, dry'"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )

    seasons_response = response.choices[0].text.strip()
    seasons_list = seasons_response.split(', ')

    return seasons_list
