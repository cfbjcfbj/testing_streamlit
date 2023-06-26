import streamlit as st
import folium
from streamlit_folium import folium_static
import h3
import branca.colormap as cm #testing

def app():
    st.title("Connect AI")

    st.markdown(
        """
        Welcome to Connect AI! Where we connect you with your dates
        """
    )

    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    color_scale = cm.LinearColormap(['green', 'yellow', 'red', 'purple'], vmin=0, vmax=120) #testing

    hexagons = {
        '8a652636062ffff': 0,
        '8a6526360197fff': 11.600000000000001,
        '8a652636051ffff': 13.700000000000001,
        '8a6526360777fff': 3.7096248711548725,
        '8a6526360767fff': 7.340706024792129,
        # Add more hexagons here...
    }

    for h3_index, time in hexagons.items():
        geo_boundary = h3.h3_to_geo_boundary(h3_index, geo_json=False)

        color = color_scale(time) #testing

        folium.Polygon(
            locations=geo_boundary,
        color=None, #testing
        fill=True,
        fill_color=color, #testing
        fill_opacity=0.6,
        popup=f'Time: {time:.2f} min' #testing
        ).add_to(map)

    folium_static(map)

if __name__ == "__main__":
    app()
