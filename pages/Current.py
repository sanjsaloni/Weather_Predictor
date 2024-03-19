import streamlit as st
import requests
import os
# import sys
# sys.path.append('../../')
# import main.predict as pd 
# import predict as pd
# sys.path.insert(0, "Users\Sanjay Sahoo\A_projects\Weather_Prediction")
# from predict import wind
st.set_page_config(page_icon = ":cloud:",page_title = "Current Weather")
st.markdown("# Weather Today")
st.sidebar.markdown("# Current")

def air_quality(url):
    a_url = url+"&aqi=yes"
    response = requests.get(a_url)
    a_data = response.json()
    air_q = a_data["current"]["air_quality"]
    col1, col2, col3, col4 = st.columns(4)
    with col1:
         st.write("Carbon Monoxide")
         st.write(f"{air_q['co']}")
    with col2:
         st.write("Nitrogen Dioxide")
         st.write(f"{air_q['no2']}")
    with col3:
         st.write('Nitrate ')
         st.write(f"{air_q['o3']}")
    with col4:
         st.write("Suplur Dioxide")
         st.write(f"{air_q['so2']}")

def wind(wind_dir):
                fi=""
                if 'S' in wind_dir:
                    fi=("South")
                elif 'N' in wind_dir:
                    fi=("North")
                elif 'E' in wind_dir:
                    fi=("East")
                elif 'W' in wind_dir:
                    fi=("West")
                elif 'SSW' in wind_dir:
                    fi=("SouthWest")
                elif 'SSE' in wind_dir:
                    fi=("SouthEast")
                elif 'NNW' in wind_dir:
                    fi="NorthWest"
                elif 'NNE' in wind_dir:
                    fi=("NorthEast")
                return fi
if __name__ in "__main__":
 city = st.text_input(":round_pushpin: Enter the city")
# pre = st.button("")
 base_url = os.environ['base_url']
 key = os.environ['key']
 current_url = f"/current.json?key={key}&q={city}"
 url = base_url+current_url
 response = requests.get(url)
 if response.status_code == 200:
        data = response.json()
        # '''st.write(f"What do you want to know?\
        #       \n 1.Current Temperature of {city}\
        #       \n 2.Is it day or not night {city}\
        #       \n 3.Wind Speed in {city}\
        #         \n 4.Wind direction at {city}\
        #         \n 5.Humidity\
        #         \n 6.Precipitation\
        #         \n 7.Air Quality\
        #         \n 8.Stop the query")'''
        a1 = st.checkbox(f'Current Temperature of {city}')
        a2 = st.checkbox(f'Is it day or not night {city}')
        a3 = st.checkbox(f'Wind Speed in {city}')
        a4 = st.checkbox(f'Wind direction at {city}')
        a5 = st.checkbox(f'Humdity')
        a6 = st.checkbox(f'Precipitation')
        a7 = st.checkbox(f'Air Quality')
        # while(True):
        #  choice = int(input("Enter your choice(1-8): "))
        #  if(choice<=8 and choice>0):
        if a1:
                temp_c = data["current"]["temp_c"]
                temp_f = data["current"]["temp_f"]
                col1, col2, col3 = st.columns(3)
                col1.metric(f"Current temperature in {city}",f"{temp_c}°C")
                col2.metric(f"Current temperature in {city}" ,f"{temp_f}°F")
                # break
        if a2:
                phase = data["current"]["is_day"]
                if phase == 0:
                    st.write("It is night:moon:")
                else:
                    st.write("It is day:sun_with_face:")
                # break
        if a3:
                wind_mph = data["current"]["wind_mph"]
                wind_kph = data["current"]["wind_kph"]
                st.write(f"Wind speed at {city} : {wind_kph} kph")
                st.write(f"Wind speed at {city} : {wind_mph} mph")
                # break
        if a4:
                # pd.wind()
                wind_d = wind(data["current"]["wind_dir"])
                st.write("Wind Direction: "+ wind_d)
                # print(f"Wind direction: {wind_dir}")
                # break
        if a5:
                hum = data["current"]["humidity"]
                st.write(f"Humidity at {city}: {hum}")
                # break
        if a6:
                prep_mm = data["current"]["precip_mm"]
                prep_in = data["current"]["precip_in"]
                st.write(f"Precipitation in {city}: {prep_mm} millimeters or {prep_in} inches")
                # break
        if a7:
                # print(a_url)
                air_quality(url)
        # elif a8:
                # print("Code exited.")
            # break
 else:
        data = response.json()
        # st.write("Please enter the city")

