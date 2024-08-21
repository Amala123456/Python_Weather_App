from datetime import datetime
import requests
import tkinter as tk
from tkinter import messagebox


# Function to get weather data
def get_weather():
    user_api = '45e9aa4d285329a75612388d8b8f57b2'
    location = city_entry.get()

    complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api}"

    try:
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] == '404':
            messagebox.showerror("Error", "City Not Found! Please check the city name.")
        else:
            temp = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdty = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            pressure = api_data['main']['pressure']
            date_time = datetime.now().strftime("%d %b %Y | %H:%M:%S %p")

            weather_info = (f"Weather Status for - {location.upper()} || {date_time}\n"
                            f"-------------------------------------------------------------\n"
                            f"Current temperature : {temp:.2f}°C\n"
                            f"Current weather description  : {weather_desc}\n"
                            f"Current Humidity      : {hmdty}%\n"
                            f"Current wind speed    : {wind_spd} kmph\n"
                            f"Current pressure      : {pressure} hPa")

            messagebox.showinfo("Weather Prediction", weather_info)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Create the main window
root = tk.Tk()
root.title("Weather Prediction App")
root.geometry("400x200")

# Add a label and entry for city input
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=10)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

# Add a button to trigger the weather prediction
predict_button = tk.Button(root, text="Predict Weather", command=get_weather)
predict_button.pack(pady=20)

# Run the application
root.mainloop()
