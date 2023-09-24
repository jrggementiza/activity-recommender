from fastapi import FastAPI

from country import get_matching_country
from season import get_matching_seasons
from recommendations import get_recommendations


app = FastAPI()


@app.get("/")
def seasons(country: str, season: str):
    # Intercept error if no country or season and standardize the response

    matching_country, country_options = get_matching_country(country)
    if not matching_country:
        return {
            "message": f"Country {country} unclear. Is it any of the following?",
            "options": country_options,
        }

    # TODO: Handle typecase formatting
    seasons_list: list = get_matching_seasons(matching_country)
    if season not in seasons_list:
        return {
            "message": f"Country {matching_country} has no season {season}. Please choose from the following.",
            "options": seasons_list,
        }

    recommendations = get_recommendations(matching_country, season)

    return {
        "country": matching_country,
        "season": season,
        "recommendations": recommendations
    }
