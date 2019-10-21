#coding:utf-8
import folium
import pandas as pd


flags = pd.DataFrame({
    'number':['1','2','3','4','5','6','7','8','9','10','11','12'],
    'latitude':[35.028309,46.469391,39.758949,41.015137,24.466667,3.140853,
                9.005401,-3.989038,52.377956,41.085651,57.790001,31.205753],
    'longtude':[135.753082,30.740883,-84.191605,28.979530,54.366669,101.693207,
                38.763611,-79.203560,4.897070,-73.858467,-152.407227,29.924526]
})

flag_map = folium.Map(location=[35.028309, 135.753082], zoom_start=9)

for i, r in flags.iterrows():
    folium.Marker(location=[r['latitude'], r['longtude']], popup=r['number']).add_to(flag_map)

flag_map