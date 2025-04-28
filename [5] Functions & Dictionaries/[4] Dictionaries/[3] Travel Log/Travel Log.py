# Starter Code

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}


# Write your code below

# TODO Complete the tasks below!
"""
» Create a dictionary to store the cities that were visited for each capital.
» Inside the dictionary also add another key-value pair to store the total visits as an input.
» Create another list named travel_log, but nest two dictionaries representing
the country and its information.
» Add an entry to the list travel_log and add a country, some cities, and the total visits
"""

travel_log = {
    "France": {
        "Cities Visited": ["Paris", "Lille", "Dijon"],
        "Total Visits": 5
    },
    "Germany": {
        "Cities Visited": ["Berlin", "Hamburg", "Stuttgart"],
        "Total Visits": 12
    },
}

