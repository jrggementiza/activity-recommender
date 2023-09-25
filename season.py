from utils import generate_response_from_prompt


def get_matching_seasons(country: str):
    prompt = (
        f"Generate the seasons of the country {country}. "
        "Only state the season name. No need to state months covered. "
        f"Make sure the seasons are correct for {country}. "
        "Answer in the format of a string of words separated by a comma."
    )
    seasons_response = generate_response_from_prompt(prompt)
    seasons_list = seasons_response.split(", ")

    return [season.lower() for season in seasons_list]
