import requests
import os
from dotenv import load_dotenv

def air_quality(url):
    a_url = url+"&aqi=yes"
    response = requests.get(a_url)
    a_data = response.json()
    air_q = a_data["current"]["air_quality"]
    print(f"co: {air_q['co']}\nno2: {air_q['no2']}\no3: {air_q['o3']}\nso2: {air_q['so2']}")


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


def current():
    current_url = f"/current.json?key={key}&q={city}"
    url = base_url+current_url
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"What do you want to know?\
              \n 1.Current Temperature of {city}\
              \n 2.Is it day or not night {city}\
              \n 3.Wind Speed in {city}\
                \n 4.Wind direction at {city}\
                \n 5.Humidity\
                \n 6.Precipitation\
                \n 7.Air Quality\
                \n 8.Stop the query")
        
        while(True):
         choice = int(input("Enter your choice(1-8): "))
         if(choice<=8 and choice>0):
            if 1 == choice:
                temp_c = data["current"]["temp_c"]
                temp_f = data["current"]["temp_f"]
                print(f"Current temperature in {city}: {temp_c}°C")
                print(f"Current temperature in {city}: {temp_f}°F")
                # break
            elif 2 == choice:
                phase = data["current"]["is_day"]
                if phase == 0:
                    print("It is night.")
                else:
                    print("It is day.")
                # break
            elif 3 == choice:
                wind_mph = data["current"]["wind_mph"]
                wind_kph = data["current"]["wind_kph"]
                print(f"Wind speed at {city} : {wind_kph} kph")
                print(f"Wind speed at {city} : {wind_mph} mph")
                # break
            elif 4 == choice:
                wind_d = wind(data["current"]["wind_dir"])
                print("Wind Direction: "+wind_d)
                # print(f"Wind direction: {wind_dir}")
                # break
            elif 5 == choice:
                hum = data["current"]["humidity"]
                print(f"Humidity at {city}: hum")
                # break
            elif 6 == choice:
                prep_mm = data["current"]["precip_mm"]
                prep_in = data["current"]["precip_in"]
                print(f"Precipitation in {city}:{prep_mm} millimeters or {prep_in} inches")
                # break
            elif 7 == choice:
                # print(a_url)
                air_quality(url)
            elif 8 == choice:
                print("Code exited.")
                break
    else:
        data = response.json()
        print(data['error']['message'])


def forecast():
    days = int(input("Number of days(maximum 10 days): "))
    alerts = input("Do you want the alerts?(Yes/No): ").lower()
    aqi_ = input("Do you want the air quality?(Yes/No): ").lower()
    f_url = base_url + f"/forecast.json?key={key}&q={city}&days={days}&aqi={aqi_}&alerts={alerts}"
    current()
    astronomy()
    response = requests.get(f_url)
    if response.status_code == 200:
        data = response.json()
        value = data['forecast']['forecastday'][0]
        print(f"Maximum Temperature:{value['day']['maxtemp_c']}°C\nMaximum Temperature:{value['day']['maxtemp_f']}°F")
        print(f"Minimum temperature:{value['day']['mintemp_c']}°C\nMinimum Temperature:{value['day']['mintemp_f']}°F")
        print(f"Average temperature:{value['day']['avgtemp_c']}°C\nAverage Temperature:{value['day']['avgtemp_f']}°F")
        print(f"Maximum wind:{value['day']['maxwind_mph']} mph\nMaximum wind:{value['day']['maxwind_kph']} kph")
        print(f"Condition:{value['day']['condition']['text']}")
        print(f"Total precipitation: {value['day']['totalprecip_in']}\n")
        print(f"Humidity: {value['day']['avghumidity']}")
        value_hour = data['forecast']['forecastday'][0]['hour']
        length = len(value_hour)
        for j in range(0,days):
          for i in range(0,length):
            value_hour = data['forecast']['forecastday'][j]['hour'][i]
            print(f"Time:{value_hour['time']}\nTemperature: {value_hour['temp_c']}\nWind direction:{wind(value_hour['wind_dir'])}\nWind Speed:{value_hour['wind_mph']}\nPressure:{value_hour['pressure_mb']}\
                  \nPrecipitation:{value_hour['precip_mm']}\nHumidity:{value_hour['humidity']}\nFeels like:{value_hour['feelslike_c']}\n")
            # print(len(value_hour))


def astronomy():
    date = input("Enter the date(DD/MM/YY): ")
    astro_url = base_url+f"/astronomy.json?key={key}&q={city}&dt={date}"
    response = requests.get(astro_url)
    if response.status_code == 200:
        astro_data = response.json()
        value = astro_data["astronomy"]["astro"]
        print(f"Sunrise: {value['sunrise']}\nSunset: {value['sunset']}\nMoonrise: {value['moonrise']}\
              \nMoon Set: {value['moonset']}\nMoon Phase: {value['moon_phase']}\nMoon Illumination: {value['moon_illumination']}\
              \nMoon Illuminaton: {value['moon_illumination']}")


def future():
    date = input("Enter the date (Date between 14 days and 300 days from today in the future in yyyy-MM-dd format): ")  
    url = f"http://api.weatherapi.com/v1/future.json?key={key}&q={city}&dt={date}"
    response = requests.get(url)
    if(response.status_code==200):
        data = response.json()
        f_day = data["forecast"]["forecastday"]
        astronomy(date) #function for astro information of the weather.
        forecast(date) #function to be implemented for the information of the weather

if __name__ in "__main__":
    load_dotenv()
    base_url = "http://api.weatherapi.com/v1"
    key = os.environ['key']
    weather = (input("Enter the weather you need: ")).lower()
    city = input("Enter the city: ")
    
    if 'current' in weather:
        current()
    if 'astronomy' in weather:
        astronomy()
    if 'forecast' in weather:
        forecast()
