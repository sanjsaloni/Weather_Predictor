import streamlit as st
import os
import requests

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

def forecast(base_url,key,city):
    days = st.text_input("Number of days(maximum 10 days): ")
    alerts = st.text_input("Do you want the alerts?(Yes/No): ").lower()
    aqi_ = st.text_input("Do you want the air quality?(Yes/No): ").lower()
    f_url = base_url + f"/forecast.json?key={key}&q={city}&days={days}&aqi={aqi_}&alerts={alerts}"
    # current()
    # astronomy()
    response = requests.get(f_url)
    if response.status_code == 200:
        data = response.json()
        value = data['forecast']['forecastday'][0]
        col1,col2 = st.columns(2)
        col3,col4=st.columns(2)
        col5,col6 = st.columns(2)
        col1.metric(f"Maximum Temperature:",f"{value['day']['maxtemp_c']}°C")
        col2.metric(f"Maximum Temperature:",f"{value['day']['maxtemp_f']}°F")
        col3.metric(f"Minimum temperature:",f"{value['day']['mintemp_c']}°C")
        col4.metric(f"Minimum Temperature:",f"{value['day']['mintemp_f']}°F")
        # col3.metric(f"Average temperature:{value['day']['avgtemp_c']}°C",f"Average Temperature:{value['day']['avgtemp_f']}°F")
        # col4.metric(f"Maximum wind:{value['day']['maxwind_mph']} mph",f"Maximum wind:{value['day']['maxwind_kph']} kph")
        # st.columns(f"Condition:{value['day']['condition']['text']}")
        col5.metric(f"Total precipitation:",f" {value['day']['totalprecip_in']}☔")
        col6.metric(f"Humidity:",f" {value['day']['avghumidity']}")
        value_hour = data['forecast']['forecastday'][0]['hour']
        length = len(value_hour)
        for j in range(0,int(days)):
          for i in range(0,length):
            value_hour = data['forecast']['forecastday'][j]['hour'][i]
            st.write(f"Time:{value_hour['time']}\nTemperature: {value_hour['temp_c']}\nWind direction:{wind(value_hour['wind_dir'])}\nWind Speed:{value_hour['wind_mph']}\nPressure:{value_hour['pressure_mb']}\
                  \nPrecipitation:{value_hour['precip_mm']}\nHumidity:{value_hour['humidity']}\nFeels like:{value_hour['feelslike_c']}\n")
            # print(len(value_hour))

if __name__ in "__main__":
 st.set_page_config(page_icon="📈", page_title= "Forecast")
 st.markdown("# Forecast")
 st.sidebar.header("# Forecast")
 city = st.text_input(":round_pushpin: Enter the city")
# pre = st.button("")
 base_url = os.environ['base_url']
 key = os.environ['key']
 current_url = f"/current.json?key={key}&q={city}"
 url = base_url+current_url
 response = requests.get(url)
 if response.status_code == 200:
        data = response.json()
        forecast(base_url,key,city)
