import streamlit as st
import leafmap.foliumap as leafmap
import folium
import pydeck as pdk
import pandas as pd

def app():

    st.title("Heatmap")

    # filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
    # m = leafmap.Map(tiles="stamentoner")
    # m.add_heatmap(
    #     filepath,
    #     latitude="latitude",
    #     longitude="longitude",
    #     value="pop_max",
    #     name="Heat map",
    #     radius=20,
    # )
    # m.to_streamlit(height=700)

    # m = leafmap.Map(locate_control=True)
    # m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    # m.add_basemap("ROADMAP")
    # m.to_streamlit(height=700)

    data = {
    'lat': [1.29684825487647, 1.297, 1.298],
    'lon': [103.85253591654006, 103.853, 103.854],
    'time': [12.1, 13.2, 14.3]}

    chart_data = pd.DataFrame(data)

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=1.3521,
            longitude=103.8198,
            zoom=11,
            pitch=30, #camera angle
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=50,
            elevation_scale=0,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            color_range=[
            [0, 0, 255, 100],
            [255, 0, 0, 100]
            ],
            color_domain=[0, 1000],
            tooltip={'text': '@time'}
            ),
        ],
    ))
