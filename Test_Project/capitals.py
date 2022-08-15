countries = input().split(", ")
capitals = input().split(", ")

output = [print(f"{country} -> {capital}") for country, capital in zip(countries, capitals)]

