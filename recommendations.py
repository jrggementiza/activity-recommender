from utils import generate_response_from_prompt


def get_recommendations(country: str, season: str):
    prompt = f"""
        Provide recommended activities you can do in {country} during the {season} season.
        Format recommendations so that it is just sentences seperated by a comma
        Important:
        1. Clean up the recommendations for each season in {country} to ensure they align with the appropriate season.
        Remove any recommendations that don't make sense given the season. For example:
        - Recommendations related to winter sports should be removed for tropical countries during the summer season.
        - Recommendations for ice skating should be removed during the hot season.
        - Recommendations for hot soups should be removed during the summer season.
        - It doesn't make sense to go climbing during the rainy season.
        - Ramen doesn't make sense during summer.
        - Ice cream makes sense in the summer.
        2. Make the recommendations actionable relative to the country. Example:
        - Go to Siargao if in the Philippines
        - Take a trip to Ximending if in Taiwan
        - Visit Akihabara if in Japan
    """

    response = generate_response_from_prompt(prompt, 100)
    recommendations_list = response.split(', ')
    return recommendations_list
