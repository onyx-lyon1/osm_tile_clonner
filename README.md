# 🗺️ osm_tile_clonner

A simple tool for cloning tiles from OpenStreetMap (OSM) while preserving the structure.

⚠️ **Disclaimer:** Please exercise caution when using this tool to avoid overloading OSM servers. Intensive usage can cause server overload and should be avoided.

## ✨ Features

- Clone OSM tiles while preserving the structure.

## ⚙️ Usage

To use the `osm_tile_clonner` tool, follow these steps:

1. Update the `min_lat`, `max_lat`, `min_lon`, `max_lon`, and `zoom` values in the script according to the desired tile range.

2. Run the script.

```python
python main.py
```

⚠️ **Caution:** Make sure to use the tool responsibly and avoid overloading OSM servers.

## ❗️ Disclaimer

Please note that this tool can potentially overload OSM servers if used intensively. Exercise caution and use it responsibly to prevent any negative impact on server performance.

## 🌍 Community and Support

As this tool is provided without an official repository, community and support channels are not available. Please proceed with caution and seek assistance from relevant OSM communities or resources if needed.

---

# 🛣️ road_creator

A tool that converts .osm files to a graph in JSON format.

## ✨ Features

- Convert .osm files to a graph in JSON format.

## ⚙️ Usage

To use the `road_creator` tool, follow these steps:

1. Add the desired `map.osm` file to the script's directory.    (here is a link to download the area of La Doua : https://download.bbbike.org/osm/extract/planet_4.854259,45.774737_4.889987,45.789342.osm.gz)

2. Run the script.

```python
# Example usage
osm_file = 'map.osm'
osm_data = parse_osm(osm_file)

jsonData = json.dumps(osm_data, indent=4)

# Save the results
with open("graph.json", 'w') as file:
    json.dump(osm_data, file)

# Display the results
# print(jsonData)
```
