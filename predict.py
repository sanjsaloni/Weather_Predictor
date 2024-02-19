import requests
import json

base_url = "http://api.weatherapi.com/v1"
key = "7aa90a91f1f44ce2853170509241802"
weather = (input("Enter the weather you need: ")).lower()

if 'current' in weather:
    city = input("Enter the city: ")
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
         choice = int(input("Enter your choice(1-6): "))
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
                wind_dir = data["current"]["wind_dir"]
                if 'S' in wind_dir:
                    print("South")
                elif 'N' in wind_dir:
                    print("North")
                elif 'E' in wind_dir:
                    print("East")
                elif 'W' in wind_dir:
                    print("West")
                elif 'SSW' in wind_dir:
                    print("SouthWest")
                elif 'SSE' in wind_dir:
                    print("SouthEast")
                elif 'NNW' in wind_dir:
                    print("NorthWest")
                elif 'NNE' in wind_dir:
                    print("NorthEast")
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
                a_url = url+"&aqi=yes"
                response = requests.get(a_url)
                data = response.json()
                # print(a_url)
                air_q = data["current"]["air_quality"]
                # co,no2,o3,so2 = air_q.items()
                print(f"co: {air_q['co']}\nno2: {air_q['no2']}\no3: {air_q['o3']}\nso2: {air_q['so2']}")
            elif 8 == choice:
                print("Code exited.")
                break
                
if 'forecast' in weather:
    pass