import tkinter as tkntr
from tkinter import simpledialog
from geopy.geocoders import Nominatim

import current_weather
import three_hours_forecast



api_token = "f76451990c428c8c1dfd3b5b1e33fcde"



while True:
    options_window = tkntr.Tk()
    options_window.withdraw()
    choice = simpledialog.askstring(title="Weather", prompt="Please choose an option: 1 or 2")

    if choice == '1':
        location_window = tkntr.Tk()
        location_window.withdraw()
        user_location = simpledialog.askstring(title="Weather",
                                               prompt="Location:",
                                               initialvalue="City, Country")
        if user_location == "City, Country":
            user_location = "London, GB"
        elif user_location is None:
            continue

        locator = Nominatim(user_agent="Weather_APP")
        geo_location = locator.geocode(user_location)
        if geo_location is None:
            error_message = tkntr.messagebox.showerror(title=f"Error", message="Invalid location.")
            continue
        user_latitude = geo_location.latitude
        user_longitude = geo_location.longitude

        temperature_now, temperature_feels_like, pressure_now, wind_speed_now, wind_deg_now, \
        weather_desc_now, precipitation, precipitation_type, wind_direction_abbr, \
        wind_direction_arrow = current_weather.current_weather_info(user_latitude, user_longitude, api_token)

        # If rain:
        if precipitation_type == "rain":
            weather_info = tkntr.messagebox.showinfo(title=f"Weather {user_location}",
                                                  message=f"{user_location} \n"
                                                          f"Temperature: {temperature_now}°C\n"
                                                          f"Feels Like: {temperature_feels_like}°C.\n"
                                                          f"Condition: {weather_desc_now}.\n"
                                                          f"{precipitation}\n"
                                                          f"Wind: {wind_speed_now}m/s {wind_direction_abbr}({wind_direction_arrow})\n"
                                                          f"Pressure: {pressure_now}hPa")
        # If snow:
        elif precipitation_type == "snow":
            weather_info = tkntr.messagebox.showinfo(title=f"Weather {user_location}",
                                                  message=f"{user_location} \n"
                                                          f"Temperature: {temperature_now}°C\n"
                                                          f"Feels Like: {temperature_feels_like}°C.\n"
                                                          f"Condition: {weather_desc_now}.\n"
                                                          f"{precipitation}\n"
                                                          f"Wind: {wind_speed_now}m/s {wind_direction_abbr}({wind_direction_arrow})\n"
                                                          f"Pressure: {pressure_now}hPa")
        else:
            weather_info = tkntr.messagebox.showinfo(title=f"Weather {user_location}",
                                                  message=f"{user_location} \n"
                                                          f"Temperature: {temperature_now}°C\n"
                                                          f"Feels Like: {temperature_feels_like}°C.\n"
                                                          f"Condition: {weather_desc_now}.\n"
                                                          f"Wind: {wind_speed_now}m/s {wind_direction_abbr}({wind_direction_arrow})\n"
                                                          f"Pressure: {pressure_now}hPa")
 
 
 
    if choice == '2':
        location_window = tkntr.Tk()
        location_window.withdraw()
        user_location = simpledialog.askstring(title="Next Hour Forecast",
                                               prompt="Location:",
                                               initialvalue="City, Country")
        if user_location == "City, Country":
            user_location = "London, GB"
        elif user_location is None:
            continue

        locator = Nominatim(user_agent="Weather_APP")
        geo_location = locator.geocode(user_location)
        if geo_location is None:
            error_message = tkntr.messagebox.showerror(title=f"Error", message="Invalid location.")
            continue
        user_latitude = geo_location.latitude
        user_longitude = geo_location.longitude

        temperature_per_hour, feels_like_per_hour, pressure_per_hour, wind_speed_per_hour, wind_deg_per_hour, \
        weather_desc_per_hour, hourly_precipitation, hourly_precipitation_type, \
        hourly_wind_direction_abbr, hourly_wind_direction_arrow = three_hours_forecast.three_hours_forecast_info(user_latitude, user_longitude, api_token)

        # If rain:
        if hourly_precipitation_type == "rain":
            weather_info = tkntr.messagebox.showinfo(title=f"Next Hour Forecast {user_location}",
                                                  message=f"Next Hour Forecast {user_location} \n"
                                                          f"Temperature: {temperature_per_hour}°C\n"
                                                          f"Feels Like: {feels_like_per_hour}°C.\n"
                                                          f"Condition: {weather_desc_per_hour}.\n"
                                                          f"{hourly_precipitation}\n"
                                                          f"Wind: {wind_speed_per_hour}m/s {hourly_wind_direction_abbr}({hourly_wind_direction_arrow})\n"
                                                          f"Pressure: {pressure_per_hour}hPa")

        # If snow:
        elif hourly_precipitation_type == "snow":
            weather_info = tkntr.messagebox.showinfo(title=f"Next Hour Forecast {user_location}",
                                                  message=f"Next Hour Forecast {user_location}\n"
                                                          f"Temperature: {temperature_per_hour}°C\n"
                                                          f"Feels Like: {feels_like_per_hour}°C.\n"
                                                          f"Condition: {weather_desc_per_hour}.\n"
                                                          f"{hourly_precipitation}\n"
                                                          f": {wind_speed_per_hour}m/s {hourly_wind_direction_abbr}({hourly_wind_direction_arrow})\n "
                                                          f"Pressure: {pressure_per_hour}hPa")

        else:
            weather_info = tkntr.messagebox.showinfo(title=f"Next Hour Forecast {user_location}",
                                                  message=f"Next Hour Forecast {user_location}\n"
                                                          f"Temperature: {temperature_per_hour}°C\n"
                                                          f"Feels Like: {feels_like_per_hour}°C.\n"
                                                          f"Condition: {weather_desc_per_hour}.\n"
                                                          f"Wind: {wind_speed_per_hour}m/s {hourly_wind_direction_abbr}({hourly_wind_direction_arrow})\n"
                                                          f"Pressure: {pressure_per_hour}hPa")



    # Cancel button:
    if choice is None:
        exit("The program has ended.")



    # Input check:
    if choice != '1' and choice != '2':
        error_message = tkntr.messagebox.showerror(title=f"Error", message="Invalid option.")