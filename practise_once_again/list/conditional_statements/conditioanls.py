"""
x = 0
y = 5
if x < y:
    print('yes_1')
if y < x:
    print('yes_2')
if x:
    print('yes_3')
if y:
    print('yes_4')
if x or y:
    print('yes_5')
if x and y:
    print('yes_6')
if 'aul' in 'grault':
    print('yes_7')
if 'foo' in ['foo', 'bar', 'baz']:
    print('yes_8')

if 'bar' in ['bar', 'baz', 'qux']:
    print(1)
print('After conditional')

if 'foo' in ['foo', 'bar', 'baz']:
    print ('Outer condition is true')

    if 10 > 20:
        print('Inner condition 1')

    print('Between inner conditions')

    if 10 < 20:
        print('Inner condition 2')

    print('End of outer condition')
print('After outer condition')

x = 120

if x < 50:
    print('first suite')
else:
    print('second suite')

name ='Joe'

if name == 'Fred':
    print('Hello Fred')
elif name == 'Alex':
    print('Hello Alex')
elif name == 'Jo':
    print('Hello Joe')
elif name == 'Arnold':
    print('Hello Arnold')
elif name == 'Fred':
    print('Hello Fred')
else:
    print("I don't know who you are!")


name = {
    'Fred': 'Hello Fred',
    'Xander': 'Hello Xander',
    'Joe': 'Hello Joe',
    'Arnold': 'Hello Arnold',
}

print(name.get('Joe', "I don't know who you are!"))
print(name.get('Rick', "I don't know who you are!"))


if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
if var:
    print("This won't happen")
# if 'f' in 'foo': print('1'); print('2'); print('3')

if 'z' in 'foo': print('1'); print('2'); print('3')


raining = False
print( "Let's go to the", 'beach' if not raining else 'library')
raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')


a = 5
b = 0
if a > b:
    m = a
else:
    m = b
print(m)

a = 5
b = 0

m = a if a > b else b
print(m)

x  = y = 40
z = 1 + x if x > y else y + 2
print(z)

x = y = 40
z = (1 + x) if x > y else (y + 2)

x = 0
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
)
print(s)
"""
if True:
    pass

print('foo')
