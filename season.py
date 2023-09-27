from typing import List

import pandas as pd


def _get_latitude_of_country(country: str) -> float:
    csv_file =  './data/coordinates.csv'
    df = pd.read_csv(csv_file)

    filtered_df = df[df['country'] == country.title()]

    if not filtered_df.empty:
        return filtered_df.iloc[0]['latitude']
    else:
        # Force an error further in the flow
        return 99999


def _get_seasons_of_country(latitude: float) -> List[str]:
    POLAR_SEASONS = ["Long Winter", "Short Summer"]
    TEMPERATE_SEASONS = ["Spring", "Summer", "Autumn", "Winter", "Fall"]
    TROPICAL_SEASONS = ["Wet", "Dry", "Rainy", "Summer"]

    MIN_MAX_LATITUDE_SEASONS = [
        (66.500000, 90.000000, POLAR_SEASONS, "North Pole"),
        (23.500000, 66.400000, TEMPERATE_SEASONS, "Northern Hemisphere"),
        (0.100000, 23.400000, TROPICAL_SEASONS, "Tropic of Cancer"),
        (0.000000, 0.000000, TROPICAL_SEASONS, "Equator"),
        (-23.400000, -0.100000, TROPICAL_SEASONS, "Tropic of Capricorn"),
        (-66.400000, -23.500000, TEMPERATE_SEASONS, "Southern Hemisphere"),
        (-90.000000, -66.500000, POLAR_SEASONS, "South Pole")
    ]
    
    for min_lat, max_lat, seasons, _ in MIN_MAX_LATITUDE_SEASONS:
        
        if min_lat <= latitude <= max_lat:
            return seasons

    return []


def get_matching_seasons(country: str):
    seasons_list = []
    error_message = {}

    latitude = _get_latitude_of_country(country)
    seasons_list = _get_seasons_of_country(latitude)

    if not seasons_list:
        error_message = {
            "message": "season not found."
        }

    return (seasons_list, error_message)
