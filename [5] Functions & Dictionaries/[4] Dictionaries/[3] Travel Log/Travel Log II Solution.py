# Starter Code
travel_log = [
    {
        "Country": "France",
        "Cities Visited": ["Paris", "Lille", "Dijon"],
        "Total Visits": 5
    },
    {
        "Country": "Germany",
        "Cities Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits": 12
    }
]


# Write your code below

def add_new_country(country, cities_visited, times_visited):
    new_country = {}
    new_country["Country"] = country
    new_country["Cities Visited"] = cities_visited
    new_country["Total Visits"] = times_visited
    travel_log.append(new_country)

    print("New entry added to travel log!")

add_new_country("Russia", ["Moscow", "St. Petersburg"], 2)

for i in range(len(travel_log)):
    element = travel_log[i]
    print(f"Country Visited: {element["Country"]}")
    print(f"Cities Visited: {" ".join(element["Cities Visited"])}")
    print(f"Times Visited: {element["Total Visits"]}\n")