import json

features = []

with open("points.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        
        if not line or line.startswith("lat"):
            continue
        
        parts = line.split(",")
        
        lat = float(parts[0])
        lon = float(parts[1])
        name = parts[2]
        pop = int(parts[3])
        area = float(parts[4])
        
        density = round(pop / area, 2)
        
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat] 
            },
            "properties": {
                "name": name,
                "population": pop,
                "area_sqkm": area,
                "pop_density": density
            }
        }
        features.append(feature)

geojson_data = {
    "type": "FeatureCollection",
    "features": features
}

with open("stations.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson_data, f, ensure_ascii=False, indent=4)
print('تم')