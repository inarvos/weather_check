import tkinter as tkntr
from tkinter import simpledialog
from geopy.geocoders import Nominatim

import current_weather



api_token = ""



while True:
    options_window = tkntr.Tk()
    options_window.withdraw()
    choice = simpledialog.askstring(title="Weather", prompt="Please choose an option: 1")

    if choice == '1':
        location_window = tkntr.Tk()
        location_window.withdraw()
        user_location = simpledialog.askstring(title="Weather",
                                               prompt="Location:",
                                               initialvalue="City, Country")
        if user_location == "City, Country":
            user_location = "London, UK"
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

    # Cancel button:
    if choice is None:
        exit("The program has ended.")

    # Input check:
    if choice != '1':
        error_message = tkntr.messagebox.showerror(title=f"Error", message="Invalid option.")