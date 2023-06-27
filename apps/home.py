import streamlit as st
import folium
from streamlit_folium import st_folium
import h3
import branca.colormap as cm

# TESTING
def get_pos(lat,lng):
    return lat,lng

def app():
    st.title("Connect AI")

    st.markdown(
        """
        Welcome to Connect AI! Where we connect you with your dates
        """
    )

    map = folium.Map(location=[1.3521, 103.8198], zoom_start=12, tiles="CartoDB Positron")

    # Add click event handler
    map.add_child(folium.LatLngPopup())
    map.add_child(folium.ClickForMarker())

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

    # TESTING
    data = get_pos(map['last_clicked']['lat'],map['last_clicked']['lng'])
    # TESTING
    if data is not None:
        st.write(data)



if __name__ == "__main__":
    app()
