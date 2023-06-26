import streamlit as st
import leafmap.foliumap as leafmap
import osmnx as ox
import folium
from streamlit_folium import st_folium, folium_static


def app():
    st.title("Connect AI")

    st.markdown(
        """
    Welcome to Connect AI! Where we connect you with your dates iykwim

    """
    )

    # m = leafmap.Map(locate_control=True)
    # m = leafmap.Map(center=(1.3521, 103.8198), zoom=12)
    # m.add_basemap("ROADMAP")
    # m.to_streamlit(height=700)

    PLACE_NAME = 'Singapore'
    G = ox.graph_from_place(PLACE_NAME, network_type='drive')
    m = ox.plot_graph_folium(G)
    st_data = st_folium(m, width=700)
