from utils import generate_response_from_prompt


def get_matching_seasons(country: str):
    seasons_list = []
    error_message = {}

    prompt = (
        f"Generate the seasons of the country {country}. "
        "Only state the season name. No need to state months covered. "
        f"Make sure the seasons are correct for {country}. "
        "Answer in the format of a string of words separated by a comma."
    )

    try:
        seasons_response = generate_response_from_prompt(prompt)
        seasons_list = [season.lower() for season in seasons_response.split(", ")]
    except Exception as e:
        error_message = {
            "message": e._message,
        }

    return (seasons_list, error_message)
