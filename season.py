from utils import generate_response_from_prompt


def get_matching_seasons(country: str):
    seasons_list = []
    error_message = {}

    prompt = (
        # Base Whispers
        f"Generate the seasons of the country {country}. "
        f"Make sure the seasons are correct for {country}."
        # Format Whispers
        "No need to mention dates covered."
        "Only answer in comma separated single words."
        # Sample Whispers
        "Examples are 'dry, rainy' for tropical countries and 'Winter, Spring, Summer, Fall' temperate countries."
    )

    try:
        seasons_response = generate_response_from_prompt(prompt, 200)
        seasons_list = [season.lower() for season in seasons_response.split(", ")]
    except Exception as e:
        error_message = {
            "message": e._message,
        }

    return (seasons_list, error_message)
