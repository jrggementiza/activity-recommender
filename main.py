from fastapi import FastAPI

from country import get_country
from season import get_seasons

app = FastAPI()


@app.get("/")
def seasons(country: str, season: str):
    # Intercept error if no country or season and standardize the response

    matching_country, country_options = get_country(country)
    if not matching_country:
        return {
            "message": f"Country {country} unclear. Is it any of the following?",
            "options": country_options,
        }

    # TODO: Handle typecase formatting
    matching_season, season_options = get_seasons(matching_country, season)
    if not matching_season:
        return {
            "message": f"Country {matching_country} has no season {season}. Please choose from the following.",
            "options": season_options,
        }

    return {
        "country": matching_country,
        "season": season,
    }
