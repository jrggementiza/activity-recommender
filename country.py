from pycountry import countries


def get_matching_country(country: str):
    result_country = None
    error_message = {}

    # Handle country code first
    country_code_result = countries.get(alpha_2=country)
    if country_code_result:
        result_country = (
            country_code_result.common_name
            if hasattr(country_code_result, "common_name")
            else country_code_result.name
        )
        return (result_country, error_message)

    try:
        countries.lookup(country)
    except LookupError:
        error_message = {
            "message": f"Country {country} not clear.",
            "detail": "Make sure no typos or extra spaces.",
        }

    # Use Fuzzy Search if not Country Code
    try:
        fuz_result = countries.search_fuzzy(country)
    except LookupError:
        return (result_country, error_message)

    fuzzy_countries = []
    for res in fuz_result:
        fuzzy_countries.append(
            res.common_name.lower() if hasattr(res, "common_name") else res.name.lower()
        )

    error_message = {
        "message": f"Country {country} not clear. Is it any of the following?",
        "detail": fuzzy_countries,
    }

    if len(fuz_result) >= 1 and country in fuzzy_countries:
        result_country = country
        error_message = {}

    return (result_country, error_message)
