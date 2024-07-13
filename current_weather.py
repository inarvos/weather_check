import requests
import json

# Option 1 - Current Weather Information:

def current_weather_info(latitude, longnitude, api_token):

    link = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longnitude}&appid={api_token}"
    resp = requests.get(link)
    weather_data = json.loads(resp.text)

    # Show selected general weather data for requested locations:
    weather_desc_now = weather_data["weather"][0]["description"]
    temperature_now = weather_data["main"]["temp"]
    pressure_now = weather_data["main"]["pressure"]
    wind_speed_now = weather_data["wind"]["speed"]
    wind_deg_now = weather_data["wind"]["deg"]
    temperature_feels_like = weather_data["main"]["feels_like"]
    # Show conditional weather data for requested locations:
    precipitation = weather_data["weather"][0]["main"]

    print(link)
    print(weather_desc_now)
    print(temperature_now)
    print(pressure_now)
    print(wind_speed_now)
    print(wind_deg_now)
    print(temperature_feels_like)
    print(precipitation)
    
    # If raining, get volume:
    if precipitation == "Rain":
        precipitation_type = "rain"
        precipitation = weather_data["current"]["rain"]["1h"]
        precipitation = f"\u2602 {precipitation} mm/h"
    # If snowing, get volume:
    elif precipitation == "Snow":
        precipitation_type = "snow"
        precipitation = weather_data["current"]["snow"]["1h"]
        precipitation = f"\u2744 {precipitation} mm/h"
    else:
        precipitation = None
        precipitation_type = None

    # Convert the wind direction to the corresponding abbreviation:
    def between(value, min_value, max_value):
        return min_value <= value <= max_value

    wind_direction_abbr = wind_deg_now
    if between(wind_direction_abbr, 0, 22):
        wind_direction_abbr = "N"
    elif between(wind_direction_abbr, 23, 67):
        wind_direction_abbr = "NE"
    elif between(wind_direction_abbr, 68, 112):
        wind_direction_abbr = "E"
    elif between(wind_direction_abbr, 113, 157):
        wind_direction_abbr = "SE"
    elif between(wind_direction_abbr, 158, 202):
        wind_direction_abbr = "S"
    elif between(wind_direction_abbr, 203, 247):
        wind_direction_abbr = "SW"
    elif between(wind_direction_abbr, 248, 292):
        wind_direction_abbr = "W"
    elif between(wind_direction_abbr, 293, 337):
        wind_direction_abbr = "NW"
    elif between(wind_direction_abbr, 338, 360):
        wind_direction_abbr = "N"
    # Convert the wind direction to the corresponding arrow:
    wind_direction_arrow = wind_deg_now
    if between(wind_direction_arrow, 0, 22):
        wind_direction_arrow = "\u2191"
    elif between(wind_direction_arrow, 23, 67):
        wind_direction_arrow = "\u2197"
    elif between(wind_direction_arrow, 68, 112):
        wind_direction_arrow = "\u2192"
    elif between(wind_direction_arrow, 113, 157):
        wind_direction_arrow = "\u2198"
    elif between(wind_direction_arrow, 158, 202):
        wind_direction_arrow = "\u2193"
    elif between(wind_direction_arrow, 203, 247):
        wind_direction_arrow = "\u2199"
    elif between(wind_direction_arrow, 248, 292):
        wind_direction_arrow = "\u2190"
    elif between(wind_direction_arrow, 293, 337):
        wind_direction_arrow = "\u2196"
    elif between(wind_direction_arrow, 338, 360):
        wind_direction_arrow = "\u2191"

    return temperature_now, temperature_feels_like, pressure_now, wind_speed_now, wind_deg_now, \
           weather_desc_now, precipitation, precipitation_type, \
           wind_direction_abbr, wind_direction_arrow