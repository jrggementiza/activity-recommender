from utils import generate_response_from_prompt


def get_matching_seasons(country: str):
    prompt = f"Given a {country}, what are that country's seasons. Just the season type, no need to specify months covered. Simplify the season naming. Like Dry, Rainy, Winter, Spring, Summer, Fall. Not Rainy Season, Dry Season, Winter Season. Make sure the seasons are correct for {country}. Expected output examples: 'winter, spring, summer, fall' or 'rainy, dry'"

    seasons_response = generate_response_from_prompt(prompt)
    seasons_list = seasons_response.split(', ')

    return seasons_list
