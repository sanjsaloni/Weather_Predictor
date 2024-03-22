import requests
import streamlit as st
import os
import pandas as pd

st.set_page_config(page_icon = "🔮",page_title = "Astronomy")
st.markdown("# Astronomy")

def astronomy(base_url,city,key):
    date = st.date_input("Enter the date(DD/MM/YY): ")
    astro_url = base_url+f"/astronomy.json?key={key}&q={city}&dt={date}"
    response = requests.get(astro_url)
    if response.status_code == 200:
        astro_data = response.json()
        value = astro_data["astronomy"]["astro"]
        col1, col2 , col3 = st.columns(3)
        with col1:
           st.write("Sunrise:sun_with_face:")
           st.write(value['sunrise'])
        with col2:
           st.write("Sunset🌇")
           st.write(value['sunset'])
        with col3:
           st.write("Moonrise🌙")
           st.write(value['moonrise'])
        col4, col5, col6 = st.columns(3)
        with col4:
           st.write("Moonset🌌")
           st.write(value['moonset'])
        with col5:
           st.write("Moon Phase🌔")
           st.write(value['moon_phase'])
        with col6:
           st.write("Moon Illumination🌝")
           st.write(value['moon_illumination'])
        # print(f"Sunrise: {value['sunrise']}\nSunset: {value['sunset']}\nMoonrise: {value['moonrise']}\
            #   \nMoon Set: {value['moonset']}\nMoon Phase: {value['moon_phase']}\nMoon Illumination: {value['moon_illumination']}\
            #   \nMoon Illuminaton: {value['moon_illumination']}")

if __name__ in "__main__":
 city = st.text_input(":round_pushpin: Enter the city")
# pre = st.button("")
 base_url = os.environ['base_url']
 key = os.environ['key']
#  current_url = f"/current.json?key={key}&q={city}"
#  url = base_url+current_url
 astronomy(base_url,city,key)
#  response = requests.get(url)