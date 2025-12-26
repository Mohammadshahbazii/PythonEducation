cities = {
    "Karaj": "Alborz",
    "Tehran": "Tehran", 
    "Fardis": "Alborz",
    "Damavand": "Tehran"
}
reversed_cities = {}

for item in cities.items():
    if item[1] in reversed_cities:
        reversed_cities[item[1]].append(item[0])
    else:
        reversed_cities[item[1]] = [item[0]]

print(reversed_cities)