from utils import generate_response_from_prompt


def get_recommendations(country: str, season: str):
    recommendations_list = []
    error_message = {}

    prompt = (
        # Base Whispers
        f"Give 5 recommended activities you can do in {country} during the {season} season."
        f"Ensure the 5 recommended activities are correct for {country}."
        # Format Whispers
        "Answer in comma separated activities"
        "Strictly follow this response format:"
        # Positive Examples
        "visit gardens by the bay, flower viewing at national orchid garden, hiking at MacRitchie nature trail"
        "Example: 'Go to Siargao, Coffee at Tagaytay, Bike ride in Nuvali' for the Philippines."
        # Negative Examples
        "Ensure recommended activities makes sense given the season provided."
        "Hot soup during summer does not make sense"
        "Ice cream during winter does not make sense"
        "Hiking during rainy does not make sense"
    )

    try:
        response = generate_response_from_prompt(prompt, 300)
        recommendations_list = response.split(", ")
    except Exception as e:
        error_message = {
            "message": e._message,
        }

    return (recommendations_list, error_message)
