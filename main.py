from fastapi import FastAPI

from country import get_country

app = FastAPI()


@app.get("/")
def seasons(country: str, season: str):
    # Intercept error if no country or season and standardize the response

    matching_country, options = get_country(country)
    if not matching_country:
        return {
            "message": f"Country {country} unclear. Is it any of the following?",
            "options": options,
        }

    return {
        "country": matching_country,
        "season": season,
    }
