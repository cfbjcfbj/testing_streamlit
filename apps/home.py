import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

# 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

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

    data = {
    'lat': [1.29684825487647, 1.297, 1.298],
    'lon': [103.85253591654006, 103.853, 103.854],
    'time': [12.1, 13.2, 14.3]}

    chart_data = pd.DataFrame(data)

    # Create the HexagonLayer configuration
    hexagon_layer = {
        "data": chart_data,
        "radius": 50,
        "elevation_scale": 0,
        "elevation_range": [0, 1000],
        "pickable": True,
        "extruded": True,
        "get_position": "[lon, lat]",
        "color_range": [
            [0, 0, 255, 100],  # Start color (blue with 100 alpha)
            [255, 0, 0, 100]   # End color (red with 100 alpha)
        ],
        "color_domain": [0, 1000],  # Minimum and maximum values for the color scale
        "tooltip": {"text": "@time{%f}"}  # Display time values on hover with desired formatting
    }

    # Add the HexagonLayer to the map
    m.add_hexagon_layer(hexagon_layer)

    # Display the map in Streamlit
    m.to_streamlit(height=700)
