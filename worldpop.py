import folium
import pandas as pd

df=pd.read_csv('/home/joel1/Udemy/Volcanoes-USA.txt')
avg_lat=df['LAT'].mean()
avg_lon=df['LON'].mean()

gjson_data=open(
    '/home/joel1/udemy/world-geojson-from-ogr.json','r',encoding='utf-8-sig'
)

map1=folium.Map(location=[avg_lat,avg_lon],zoom_start=4,tiles='Stamen Terrain')

def set_mcolor(elev):
    if elev in range(0,1000):
        mcolor='blue'
    elif elev in range(1000,2000):
        mcolor='green'
    elif elev in range(2000,3000):
        mcolor='orange'
    else:
        mcolor='red'
    return mcolor

fg=folium.FeatureGroup(name='USA Volcano Locations')

for name,elev,lat,lng in zip(df['NAME'],df['ELEV'],df['LAT'],df['LON']):
    fg.add_child(folium.Marker(
        [lat, lng],
        popup=name,
        icon=folium.Icon(color=set_mcolor())
    ))

map1.add_child(fg)
map1.add_child(folium.GeoJson(
    gjson_data,
    name='World Population',
    style_function=lambda x: {
        'fillColor':'cyan' if x['properties']['POP2005'] < 25000000 else\
        'green' if 25000000 < x['properties']['POP2005'] < 50000000 else\
        'yellow' if 50000000 < x['properties']['POP2005'] < 75000000 else\
        'orange' if 75000000 < x['properties']['POP2005'] < 100000000 else\
        'red'
        })
    )
map1.add_child(folium.LayerControl())

map1.save('/home/joel1/Udemy/html/WorldPop.html')
