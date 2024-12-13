import json

# Open and load the JSON file
with open('Jikan.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
print(data)

## print all anime that have a score greater than 9.0

# for anime in data['data']:
#         if anime['score'] > 9.0:
#             print(anime['title'])

## Print all anime that stopped airing before 2015

for anime in data['data']:
        if anime['year'] < 2015:
            print(anime['title'])