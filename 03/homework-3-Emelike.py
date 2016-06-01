# EJ (Mercy) Emelike
# May 30, 2016
# Homework 3

#LISTS
# 1)
countries = ['Bulgaria', 'Mexico', 'Peru', 'France', 'Morocco', 'Ghana', 'Armenia']

# 2)
for country in countries:
    print(country)

# 3)
countries.sort()

# 4)
print(countries[0])

#5)
print(countries[len(countries) - 2])

#6
countries.remove('Bulgaria')

#7
for country in countries:
    print(country)

#DICTIONARIES
# 1)
tree = {'name':'Chandelier Tree', 'species':'Coast Redwood', 'age':2000, 'location_name':'Leggett, California', 'latitude': 39.8655, 'longitude': -123.7148}

# 2)
print(tree['name'], "is a", tree['age'], 'year old tree that is in', tree['location_name'])

# 3)
if tree['latitude'] < 40.7128:
    print('The', tree['name'], "in", tree['location_name'], "is south of NYC.")
elif tree['latitude'] > 40.7128:
    print('The', tree['name'], "in", tree['location_name'], "is north of NYC.")

# 4)
user_age = input('How old are you?')

if int(user_age) > tree['age']:
    difference = int(user_age) - tree['age']
    print ('You are', difference, 'years older than', tree['name'])
elif int(user_age) < tree['age']:
    difference = tree['age'] - int(user_age)
    print (tree['name'], 'was', difference, 'years old when you were born.')

# LIST OF DICTIONARIES
# 1)
places =  [{'name':'Moscow', 'latitude': 55.7558, 'longitude': 37.6173},
{'name':'Tehran', 'latitude': 35.6892, 'longitude': 51.3890},
{'name':'Falkland Islands', 'latitude': -51.7963, 'longitude': -59.5236},
{'name':'Seoul', 'latitude': 37.5665, 'longitude': 126.9780},
{'name':'Santiago', 'latitude': -33.4489 , 'longitude': -70.6693}]

# 2)
for place in places:
    print (place['name'])
    if place['latitude'] < 0:
        print (place['name'], 'is below the equator.')
    elif place['latitude'] > 0:
        print (place['name'], 'is above the equator.')
    if place['name'] == 'Falkland Islands':
        print ('The Falkland Islands are a biogeographical part of the mild Antarctic zone.')

# 3)
for place in places:
    if place['latitude'] > tree['latitude']:
        print (place['name'], 'is north of the', tree['name'])
    elif place['latitude'] < tree['latitude']:
        print (place['name'], 'is south of the', tree['name'])
