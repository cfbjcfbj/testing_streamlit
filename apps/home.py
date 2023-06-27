import streamlit as st
import folium
from streamlit_folium import st_folium
import h3
import branca.colormap as cm


# Global variables to store latitude and longitude
clicked_lat = None
clicked_lon = None

def handle_click(event):
    global clicked_lat, clicked_lon
    clicked_lat, clicked_lon = event.lat, event.lng
    st.info(f"Clicked coordinates: Latitude={clicked_lat}, Longitude={clicked_lon}")

def app():
    st.title("Connect AI")

    st.markdown(
        """
        Welcome to Connect AI! Where we connect you with your dates
        """
    )

    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    # Add click event handler
    map.add_child(folium.LatLngPopup(callback=handle_click))

    color_scale = cm.LinearColormap(['green', 'yellow', 'red', 'purple'], vmin=0, vmax=120)

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

        color = color_scale(time)

        folium.Polygon(
            locations=geo_boundary,
        color=None,
        fill=True,
        fill_color=color,
        fill_opacity=0.6,
        popup=f'Time: {time:.2f} min'
        ).add_to(map)

    st_folium(map, width=1400, height=700)

        # Display the clicked coordinates

    st.write(f"Latitude: {clicked_lat}")
    st.write(f"Longitude: {clicked_lon}")



if __name__ == "__main__":
    app()
