from fastapi import FastAPI, Response, status


from country import get_matching_country
from season import get_matching_seasons
from recommendations import get_recommendations


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def activities(response: Response, country: str = "", season: str = ""):
    if not country or not season:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {
            "message": "Valid country and season both required.",
            "detail": "/?country=country&season=season",
        }

    country, season = country.lower(), season.lower()

    matching_country, error_message = get_matching_country(country)
    if error_message:
        response.status_code = status.HTTP_404_NOT_FOUND
        return error_message

    matching_country = matching_country.lower()

    seasons_list, error_message = get_matching_seasons(matching_country)
    if error_message:
        response.status_code = status.HTTP_424_FAILED_DEPENDENCY
        return error_message

    if season not in seasons_list:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {
            "message": f"Country {matching_country} has no season {season}. Please choose from the following.",
            "detail": seasons_list,
        }

    recommendations, error_message = get_recommendations(matching_country, season)
    if error_message:
        response.status_code = status.HTTP_424_FAILED_DEPENDENCY
        return error_message

    return {
        "country": matching_country,
        "season": season,
        "recommendations": recommendations,
    }
