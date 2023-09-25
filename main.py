from fastapi import FastAPI

from country import get_matching_country
from season import get_matching_seasons
from recommendations import get_recommendations


app = FastAPI()


@app.get("/")
async def activities(country: str = "", season: str = ""):
    if not country or not season:
        return {
            "message": "Valid country and season both required.",
            "detail": "/?country=country&season=season",
        }

    country, season = country.lower(), season.lower()

    matching_country, error_message = get_matching_country(country)
    if error_message:
        return error_message

    matching_country = matching_country.lower()

    seasons_list, error_message = get_matching_seasons(matching_country)
    if error_message:
        return error_message

    if season not in seasons_list:
        return {
            "message": f"Country {matching_country} has no season {season}. Please choose from the following.",
            "options": seasons_list,
        }

    recommendations, error_message = get_recommendations(matching_country, season)
    if error_message:
        return error_message

    return {
        "country": matching_country,
        "season": season,
        "recommendations": recommendations,
    }
