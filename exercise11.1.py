def get_city_country(city, country):
    return f"{city}, {country}".title()

def test_city_country():
    formatted = get_city_country("santiago", "chile")
    assert formatted == "Santiago, Chile"