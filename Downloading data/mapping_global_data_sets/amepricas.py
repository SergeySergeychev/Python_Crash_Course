import pygal

wm = pygal.maps.world.World()
wm.title = 'Nort, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add('North Europe', ['lv'])

wm.render_to_file('americas.svg')
