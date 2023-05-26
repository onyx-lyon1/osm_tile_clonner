import json
import xml.etree.ElementTree as ET
from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert coordinates to radians
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])

    # Earth's radius in meters
    radius = 6371000

    # Calculate the distance using the Haversine formula
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c

    return distance


def parse_osm(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    nodes = {}
    ways = []
    print("Parsing nodes...")
    # Parse nodes
    for node_elem in root.iter('node'):
        node_id = int(node_elem.attrib['id'])
        lat = float(node_elem.attrib['lat'])
        lon = float(node_elem.attrib['lon'])
        nodes[node_id] = {'id': node_id, 'lat': lat, 'lon': lon, 'connected_nodes': []}
    print("Parsing ways...")
    # Parse ways
    for way_elem in root.iter('way'):
        way_id = way_elem.attrib['id']
        way_nodes = [int(nd_elem.attrib['ref']) for nd_elem in way_elem.iter('nd')]
        ways.append({'id': way_id, 'nodes': way_nodes})
    print("Creating connections...")
    # Create connections between nodes
    for way in ways:
        for i in range(len(way['nodes']) - 1):
            current_node_id = way['nodes'][i]
            next_node_id = way['nodes'][i + 1]

            current_node = nodes.get(current_node_id)
            next_node = nodes.get(next_node_id)

            if current_node and next_node:
                current_node['connected_nodes'].append({
                    'id': next_node_id,
                    'distance': calculate_distance(
                        current_node['lat'], current_node['lon'],
                        next_node['lat'], next_node['lon']
                    )
                })
                next_node['connected_nodes'].append({
                    'id': current_node_id,
                    'distance': calculate_distance(
                        next_node['lat'], next_node['lon'],
                        current_node['lat'], current_node['lon']
                    )
                })

    #remove nodes with no connections
    print("Removing nodes with no connections...")
    for node in list(nodes.values()):
        if len(node['connected_nodes']) == 0:
            del nodes[node['id']]

    return list(nodes.values())


# Exemple d'utilisation
osm_file = 'map.osm'
osm_data = parse_osm(osm_file)

jsonData = json.dumps(osm_data, indent=4)

# sauvegarde les resultats
with open("graph.json", 'w') as file:
    json.dump(osm_data, file)

# Affichage des résultats
# print(jsonData)
