# TODO: Replace stub w/ util that either
# 1. Freshly calls an LLM
# 2. Gets from cache Country, Season, and Recommendations if alr exist

COUNTRY_SEASON_MAP = {
    "South Korea": ["Autumn", "Spring", "Summer", "Fall"],
    "Philippines": ["Rainy", "Dry"],
}


def get_seasons(country: str, season: str):
    result_season = None
    result_options = []

    country_seasons = COUNTRY_SEASON_MAP.get(country, None)
    if season not in country_seasons:
        result_options = country_seasons
    
    else:
        result_season = country_seasons

    return (result_season, result_options)
