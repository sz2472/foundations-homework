# Grade: 11.5 / 14

#Shengying Zhao
#May 31, 2016
#Homework 3

# TA-COMMENT: Great work in this section!
countries=['United States', 'China', 'Britain', 'France', 'Greece', 'Egypt', 'Japan']

for country in countries:
    print(country)
countries.sort()
print(countries)
print(countries[0])
print(countries[-2])
countries.remove('Britain')
print(countries)
for country in countries:
    print(country)

tree={'name':'The Cotton Tree', 'species':'Kapok', 'age':103, 'location_name':'Freetown, Sierra Leone', 'latitude':8.47, 'longitude':-13.23}
print(tree['name'], 'is a', tree['age'], 'years old tree that is in', tree['location_name'])
if tree['latitude'] < 40.7128:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is south of NYC')
else:
    print('The tree', tree['name'], 'in', tree['location_name'], 'is north of NYC')
age = input('How old are you?')
difference = int(age) - tree['age']
if difference > 0:
    print('You are', int('difference'), 'years older than', tree['name'])
else:
    print(tree['name'], 'was', int('difference'), 'years older when I was born')

# TA-COMMENT: (-2) There are actually quite a few typos in the next 5 lines of code and the typos are actually preventing your code from running properly when I run your script on the command line. Be careful! And this is less relevant now that we've switched the jupyter notebook, but usually when you are preparing to submit a script, you want to make sure it can run properly from the command line. And if it doesn't run, look at the error you get to figure out how you can fix it. If it says something like, "syntax error", you're probably missing a quotation mark or closing brackets, etc.

cities= [
{name':'Moscow', 'latitude':55.76, 'longitude':37.62},
{'name':'Tehran', 'latitude':35.69, 'longitude':51.39},
{'name':'Falkland Islands', 'latitude':-51.80, 'longitude':-59.52},
{'name':'Seoul', 'latitude':37.57, 'longitude':126.98,
{'name':'Santiago', 'latitude':42.88, 'longitude':-8.54}
]

# TA-COMMENT: (-0.5) Soma also asked for this loop to print "The Falkland Islands are a biogeographical part of the mild Antarctic zone." when it encounters city['name'] == 'Falkland Islands'

for city in cities:
    if city['latitude'] > 0:
        print(city['name'], 'is above the equator')
    else:
        print(city['name'], 'is below the equator')

for city in cities:
    if city['latitude'] > tree['latitude']:
    print(city['name'], 'is north of', tree['name'])
    else:
        print(city['name'], 'is south of', tree['name'])
