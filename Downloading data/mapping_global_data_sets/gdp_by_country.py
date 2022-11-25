import json
import pygal

from country_codes import get_country_code

from pygal.style import SaturateStyle as SaS, RotateStyle as RS

# Load the data into a list.
filename ='gdp_by_country_2.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP data.
cc_GDP = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2008:
        country_name = gdp_dict['Country Name']
        gdp_value = int(float(gdp_dict['GDP(US)']))
        code = get_country_code(country_name)
        if code:
            cc_GDP[code] = gdp_value
print(cc_GDP)
# Group the countries into 4 gdp ranks.
cc_gdp_1, cc_gdp_2, cc_gdp_3, cc_gdp_4 = {}, {}, {}, {}
for cc, gdp in cc_GDP.items():
    if gdp < 25_000_000_000:
        cc_gdp_1[cc] = gdp
    elif gdp < 100_000_000_000:
        cc_gdp_2[cc] = gdp
    elif gdp < 1_000_000_000_000:
        cc_gdp_3[cc] = gdp
    else:
        cc_gdp_4[cc] =gdp

wm_style = RS('#609f86')
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World GDP in 2008, by Country"
wm.add('0-25 bn', cc_gdp_1)
wm.add('25-100 bn', cc_gdp_2)
wm.add('100-1000 bn', cc_gdp_3)
wm.add('>1000 bn', cc_gdp_4)

wm.render_to_file('world_GDP_rate.svg')
