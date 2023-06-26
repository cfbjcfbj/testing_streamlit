import streamlit as st
import folium
import geopandas as gpd
import leafmap.foliumap as leafmap
import osmnx as ox

def app():
    st.title("Connect AI")

    st.markdown(
        """
    Welcome to Connect AI! Where we connect you with your dates

    """
    )

    m = leafmap.Map(locate_control=True)
    m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
