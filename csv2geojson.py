import json
import pandas as pd
df=pd.read_csv('oss_site.csv')
geojson_data={
    "type":"FeatureCollection",
    "features":[]
}

for index, row in df.iterrows():
    x=row['township_name_en']
    if x=='Latha':
        feature={"type":"Feature",
        "geometry":{
            "type":"Point",
            "coordinates":[row['longitude'],row['latitude']]
        },
        "properties":{"township":row['township_name_en'],"type":row['type'],'identifier':row['identifier'],"marker-color": "#8000ff",
        "marker-size": "medium","marker-symbol": "circle"}
        
        }
    elif x=='Lanmadaw':
        feature={"type":"Feature",
        "geometry":{
            "type":"Point",
            "coordinates":[row['longitude'],row['latitude']]
        },
        
        "properties":{"township":row['township_name_en'],"type":row['type'],'identifier':row['identifier'],"marker-color": "#ff0000",
        "marker-size": "medium","marker-symbol": "circle"}
        }
        
    geojson_data['features'].append(feature)
    with open('output.geojson','w') as f:
        f.write(json.dumps(geojson_data))