import streamlit as st
# import leafmap.foliumap as leafmap
import pandas as pd
import folium
from streamlit_folium import st_folium

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

    m = folium.Map(location=[1.3521, 103.8198], zoom_start=16)
    st_data = st_folium(m, width=725)
