 Chapter 11/217 city functions.py

def city_country(city, country, population=None):
    """Return a string like 'Santiago, Chile' or
    'Santiago, Chile - population 5000000' when population is provided.
    """
    city_part = f"{city}, {country}"
    if population is not None:
        return f"{city_part} - population {population}".title()
    return city_part.title()
