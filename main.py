import math
import os
import requests

def deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return xtile, ytile

min_zoom = 0
min_lat = 45.77943
min_lon = 4.85877
max_lat = 45.78880
max_lon = 4.88829
max_zoom = 19

# create HTTP user agent
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36'
headers = {'User-Agent': user_agent}

for zoom in range(min_zoom, max_zoom + 1):
    min_x, min_y = deg2num(min_lat, min_lon, zoom)
    max_x, max_y = deg2num(max_lat, max_lon, zoom)
    for x in range(min(min_x, max_x), max(max_x + 1, min_x + 1)):
        for y in range(min(min_y, max_y), max(max_y + 1, min_y + 1)):
            url = f'https://tile.openstreetmap.org/{zoom}/{x}/{y}.png'
            print(url)
            # create folder structure if it doesn't exist
            folder = f'./tiles/{zoom}/{x}'
            os.makedirs(folder, exist_ok=True)
            # download tile
            r = requests.get(url, headers=headers)
            with open(f'{folder}/{y}.png', 'wb') as f:
                f.write(r.content)
