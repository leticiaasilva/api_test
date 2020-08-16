import requests
import json

URL = 'https://swapi.dev/api/starships/'
r = requests.get(url=URL)
data = r.json()
list_of_print = []
distance_in_mega_lights = 1000000


def calculate_required_stops(distance):
    for i in data['results']:
        consumables = i['consumables']
        MGLT = int(i['MGLT'])
        hours_to_travel = distance / MGLT
        days_to_calculate = hours_to_travel / 24
        consumable_days = 0
        if 'month' in consumables:
            consumable_days = int(consumables[0]) * 30
        elif 'year' in consumables:
            consumable_days = int(consumables[0]) * 365
        elif 'week' in consumables:
            consumable_days = int(consumables[0]) * 7
        elif 'day' in consumables:
            consumable_days = int(consumables[0]) * 1
        stops = days_to_calculate / consumable_days
        result = i['name'] + ': ' + str(int(stops))
        list_of_print.append(result)
    return list_of_print


def show_amount_of_stops(distance):
    calculate_required_stops(distance)
    for i in list_of_print:
        print(i)


show_amount_of_stops(distance_in_mega_lights)

