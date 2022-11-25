mlb_team = {
    'Colorado' : 'Rockies',
    'Boston'   : 'Red Sox',
    'Minnesota': 'Twins',
    'Milwaukee': 'Brewers',
    'Seattle'  : 'Mariners'
}
mlb_team = dict([
    ('Colorado', 'Rockies'),
    ('Boston', 'Red Sox'),
    ('Minnesota', 'Twins'),
    ('Milwaukee', 'Brewers'),
    ('Seattle', 'Mariners')
])
mlb_team = dict(
    Colorado='Rockies',
    Boston='Red Sox',
    Minnesota='Twins',
    Milwaukee='Brewers',
    Seattle='Mariners'
)
# print(mlb_team['Minnesota'])
# print(mlb_team['Boston'])
mlb_team['Kansas city'] = 'Royals'
mlb_team['Seattle'] = 'Seacats'
del mlb_team['Seattle']
# print(mlb_team)

# d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
# print(d)

person = {}
# print(type(person))
person['fname'] = 'Joe'
person['lname'] = 'Fonebone'
person['age'] = 51
person['spouse'] = 'Edna'
person['children'] = ['Ralph', 'Betty', 'Joey']
person['pets'] = {'dog': 'Fido', 'cat': 'Sox'}

# print(person['fname'])
# print(person['lname'])
# print(person['age'])
# print(person['spouse'])
# print(person['children'][:])
# print(person['pets']['dog'])

# print('Milwaukee' in mlb_team)
# print('Toronto' in mlb_team)
# print('Toronto' not in mlb_team)
# print(len(mlb_team))

# d.clear()
# print(d)

# d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
# print(d)
# print(d.get(0))
# print(d.get('5'))
# list(d.items())
# print(list(d.items()))
# print(list(d.items())[0][0])
# print(d)

# print(list(d.items()))
# print(list(d.keys()))
# print(list(d.values()))

# d.pop('z', -1)
# print(d.popitem())
# print(d)

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd':400}
# d1.update(d2)
print(d1)
# d1.update([('b', 200), ('d', 400)])
print(d1)
d1.update(b=200, d=400)
print(d1)
