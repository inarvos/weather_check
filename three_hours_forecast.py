import requests
import json

# Option 2: Three hours Forecast:

def three_hours_forecast_info(latitude, longitude, api_token):

    link = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_token}"
    resp = requests.get(link)
    forecast_data = json.loads(resp.text)

    # Show selected general weather data for requested locations:
    weather_desc_per_three_hours = forecast_data["list"][1]["weather"][0]["description"]
    temperature_per_three_hours = forecast_data["list"][1]["main"]["temp"]
    pressure_per_three_hours = forecast_data["list"][1]["main"]["pressure"]
    wind_speed_per_three_hours = forecast_data["list"][1]["wind"]["speed"]
    wind_deg_per_three_hours = forecast_data["list"][1]["wind"]["deg"]
    feels_like_per_three_hours = forecast_data["list"][1]["main"]["feels_like"]
    # Show conditional weather data for requested locations:
    hourly_precipitation= forecast_data["list"][1]["weather"][0]["main"]

    print(link)
    print(weather_desc_per_three_hours)
    print(temperature_per_three_hours)
    print(pressure_per_three_hours)
    print(wind_speed_per_three_hours)
    print(wind_deg_per_three_hours)
    print(feels_like_per_three_hours)
    print(hourly_precipitation)

    # If raining, get volume:
    if hourly_precipitation == "Rain":
        hourly_precipitation = forecast_data["list"][1]["rain"]["3h"]
        hourly_precipitation = f"\u2602 {hourly_precipitation} mm/h"
        hourly_precipitation_type = "rain"
    # If snowing, get volume:
    elif hourly_precipitation == "Snow":
        hourly_precipitation = forecast_data["list"][1]["snow"]["3h"]
        hourly_precipitation = f"\u2744 {hourly_precipitation} mm/h"
        hourly_precipitation_type = "snow"
    else:
        hourly_precipitation = None
        hourly_precipitation_type = None

    # Convert the wind direction to the corresponding abbreviation:
    def between(value, min_value, max_value):
        return min_value <= value <= max_value

    hourly_wind_direction_abbr = wind_deg_per_three_hours
    if between(hourly_wind_direction_abbr, 0, 22):
        hourly_wind_direction_abbr = "N"
    elif between(hourly_wind_direction_abbr, 23, 67):
        hourly_wind_direction_abbr = "NE"
    elif between(hourly_wind_direction_abbr, 68, 112):
        hourly_wind_direction_abbr = "E"
    elif between(hourly_wind_direction_abbr, 113, 157):
        hourly_wind_direction_abbr = "SE"
    elif between(hourly_wind_direction_abbr, 158, 202):
        hourly_wind_direction_abbr = "S"
    elif between(hourly_wind_direction_abbr, 203, 247):
        hourly_wind_direction_abbr = "SW"
    elif between(hourly_wind_direction_abbr, 248, 292):
        hourly_wind_direction_abbr = "W"
    elif between(hourly_wind_direction_abbr, 293, 337):
        hourly_wind_direction_abbr = "NW"
    elif between(hourly_wind_direction_abbr, 338, 360):
        hourly_wind_direction_abbr = "N"
    # Convert the wind direction to the corresponding arrow:
    hourly_wind_direction_arrow = wind_deg_per_three_hours
    if between(hourly_wind_direction_arrow, 0, 22):
        hourly_wind_direction_arrow = "\u2191"
    elif between(hourly_wind_direction_arrow, 23, 67):
        hourly_wind_direction_arrow = "\u2197"
    elif between(hourly_wind_direction_arrow, 68, 112):
        hourly_wind_direction_arrow = "\u2192"
    elif between(hourly_wind_direction_arrow, 113, 157):
        hourly_wind_direction_arrow = "\u2198"
    elif between(hourly_wind_direction_arrow, 158, 202):
        hourly_wind_direction_arrow = "\u2193"
    elif between(hourly_wind_direction_arrow, 203, 247):
        hourly_wind_direction_arrow = "\u2199"
    elif between(hourly_wind_direction_arrow, 248, 292):
        hourly_wind_direction_arrow = "\u2190"
    elif between(hourly_wind_direction_arrow, 293, 337):
        hourly_wind_direction_arrow = "\u2196"
    elif between(hourly_wind_direction_arrow, 338, 360):
        hourly_wind_direction_arrow = "\u2191"

    return temperature_per_three_hours, feels_like_per_three_hours, pressure_per_three_hours, wind_speed_per_three_hours, wind_deg_per_three_hours, \
           weather_desc_per_three_hours, hourly_precipitation, hourly_precipitation_type, \
           hourly_wind_direction_abbr, hourly_wind_direction_arrow