from typing import Tuple, List

from pycountry import countries


def get_matching_country(country: str) -> Tuple[str, List[str | None]]:
    result_country = None
    result_options = []
    # TODO: Gracefully handle LookupError for typos or spacing

    # Allow standard country code input
    country_code_result = countries.get(alpha_2=country)
    if country_code_result:
        result_country = country_code_result.common_name if hasattr(country_code_result, 'common_name') else country_code_result.name
        return (result_country, result_options)

    # Use Fuzzy Search if not Country Code
    fuz_result = countries.search_fuzzy(country)
    if len(fuz_result) > 1:
        for res in fuz_result:
            result_options.append(res.common_name if hasattr(res, 'common_name') else res.name)
    else:
        res = fuz_result[0]
        result_country = res.common_name if hasattr(res, 'common_name') else res.name

    return (result_country, result_options)
