import folium
import pandas as pd

df = pd.read_csv('/home/joel1/Udemy/Volcanoes-USA.txt')
avg_lat=df["LAT"].mean()
avg_lon=df["LON"].mean()

map1=folium.Map(location=[avg_lat,avg_lon],zoom_start=6,tile='Stamen Terrain')

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
    
for name,elev,lat,lng in zip(df['NAME'],df['ELEV'],df['LAT'],df['LON']):
    folium.Marker(
        [lat, lng],
        popup=name,
        icon=folium.Icon(color=set_mcolor(elev))
        ).add_to(map1)

map1.save('/home/joel1/Udemy/html/Volcanos.html')
