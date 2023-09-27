from typing import List


def _get_latitude_of_country(country: str) -> float:
    return


def _get_seasons_of_country(latitude: float) -> List[str]:
    MIN_MAX_LATITUDE_SEASONS = [
        (66.500000, 90.000000, ["Long Winter", "Short Summer"], "North Pole"),
        (23.500000, 66.400000, ["Spring", "Summer", "Autumn", "Winter"], "Northern Hemisphere"),
        (0.100000, 23.400000, ["Wet", "Dry"], "Tropic of Cancer"),
        (0.000000, 0.000000, ["Wet", "Dry"], "Equator"),
        (-23.400000, -0.100000, ["Wet", "Dry"], "Tropic of Capricorn"),
        (-66.400000, -23.500000, ["Spring", "Summer", "Autumn", "Winter"], "Southern Hemisphere"),
        (-90.000000, -66.500000, ["Long Winter", "Short Summer"], "South Pole")
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
