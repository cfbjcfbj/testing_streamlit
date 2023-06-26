import streamlit as st
# import leafmap.foliumap as leafmap
import pandas as pd
import folium
from streamlit_folium import st_folium
from h3 import h3
import branca.colormap as cm

def app():
    st.title("Connect AI")

    st.markdown(
        """
    Welcome to Connect AI! Where we connect you with your dates

    """
    )

    # m = leafmap.Map(locate_control=True)
    # m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    # m.add_basemap("ROADMAP")
    # m.to_streamlit(height=700)

    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    hexagons = {'8a652636062ffff': 0,
 '8a6526360197fff': 11.600000000000001,
 '8a652636051ffff': 13.700000000000001,
 '8a6526360777fff': 3.7096248711548725,
 '8a6526360767fff': 7.340706024792129,
 '8a65263603b7fff': 10.1,
 '8a652636004ffff': 11.000000000000002,
 '8a6526360327fff': 11.9,
 '8a6526360a8ffff': 12.500000000000002,
 '8a652636016ffff': 13.4,
 '8a6526360b97fff': 14.6,
 '8a65263608e7fff': 15.8,
 '8a652636082ffff': 16.7,
 '8a6526360837fff': 17.3,
 '8a65263609affff': 18.2,
 '8a652636075ffff': 2.17246238660944,
 '8a65263602b7fff': 7.709854303609152,
 '8a6526360757fff': 0.7428047897331684,
 '8a652636059ffff': 22.9,
 '8a6526362847fff': 24.7,
 '8a65263628effff': 25.6,
 '8a652636212ffff': 26.5,
 '8a6526362187fff': 28.0,
 '8a6526362547fff': 29.2,
 '8a652636250ffff': 30.099999999999998}

    color_scale = cm.LinearColormap(['green', 'yellow', 'red', 'purple'], vmin=0, vmax=120)

    # Now plot the hexagons
    for h3_index, time in hexagons.items():
    # Convert H3 index to geo boundary (latitude and longitude)
        geo_boundary = h3.h3_to_geo_boundary(h3_index, geo_json=False)



    # Compute color based on the time
        color = color_scale(time)

    # Add polygon to the map
        folium.Polygon(
            locations=geo_boundary,
            color=None,
            fill=True,
            fill_color=color,
            fill_opacity=0.6,
        #popup=f'Time: {time:.2f} min'
        ).add_to(map)

# Add color scale to the map
    map.add_child(color_scale)

# Display the map
    map
