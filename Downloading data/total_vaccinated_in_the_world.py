import json
import pygal

from get_dict_value import get_value
from country_codes import get_country_code
from pygal.style import LightSolarizedStyle as LCS, NeonStyle as NS

# Load the data into a list.
filename_v = r'vaccination.json'
with open(filename_v) as f:
    vac_data = json.load(f)
cc_vaccinations ={}
for vac_dict in vac_data:
    if vac_dict['Date'] == '2021-08-20 00:00:00':
        country_name = vac_dict['Country Name']
        vaccinated = vac_dict['Total Vaccinations']
        code = get_country_code(country_name)
        if code and vaccinated != None:
            cc_vaccinations[code] = vaccinated


filename_p = r'C:\Users\sserg\Downloading data\mapping_global_data_sets\population_data.json'
with open(filename_p) as f:
    pop_data = json.load(f)
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

cc_perc_of_vac = {}
for cc, vac in cc_vaccinations.items():
    for cc1, pop in cc_populations.items():
        if cc == cc1:
            cc_perc_of_vac[cc] = round((vac*100)/(pop), 1)

print(cc_perc_of_vac)

cc_vac_1, cc_vac_2, cc_vac_3, cc_vac_4 = {}, {}, {}, {}
for cc, vac in cc_perc_of_vac.items():
    if vac < 25:
        cc_vac_1[cc] = vac
    elif vac < 50:
        cc_vac_2[cc] = vac
    elif vac < 75:
        cc_vac_3[cc] = vac
    else:
        cc_vac_4[cc] = vac

print(len(cc_vac_1), len(cc_vac_2), len(cc_vac_3), len(cc_vac_4))

wm_style = NS(fill=True, style=NS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World vaccinated people, by country'
wm.add('0-25%', cc_vac_1)
wm.add('25-50%', cc_vac_2)
wm.add('50-75%', cc_vac_3)
wm.add('75-100%', cc_vac_4)

wm.render_to_file('world_vaccination.svg')
