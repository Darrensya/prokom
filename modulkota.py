def get_city_country(city, country, population=""):
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    return result.title()