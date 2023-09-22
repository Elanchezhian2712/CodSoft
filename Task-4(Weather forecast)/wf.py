import requests
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def fetch_weather():
    user_input = city_entry.get()
    API_KEY = '12380a31e7ecf6455062b65e82f6e9d4'
    
    # Determine if the input is numeric (likely a zip code)
    if user_input.isnumeric():
        API_URL = f'http://api.weatherstack.com/current?access_key={API_KEY}&query=zip:{user_input}'
    else:
        API_URL = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={user_input}'

    response = requests.get(API_URL)

    if response.status_code == 200:
        data = json.loads(response.text)
        
        if 'current' in data:
            temperature = data['current']['temperature']
            humidity = data['current']['humidity']
            weather_description = data['current']['weather_descriptions'][0]

            result_label.config(text=f"Weather in {user_input}:\n"
                                     f"Temperature: {temperature}°C\n"
                                     f"Humidity: {humidity}%\n"
                                     f"Description: {weather_description}")
        else:
            messagebox.showerror("Error", "Unable to retrieve weather data. 'current' key not found in response.")
    else:
        messagebox.showerror("Error", f"Unable to retrieve weather data. Status code: {response.status_code}")

root = tk.Tk()
root.title("Weather Forecast")
root.attributes('-fullscreen', True)

style = ttk.Style()
style.theme_use("vista")
background_image = tk.PhotoImage(file="C:/Users/Dell/Desktop/CodSoft Intership Python Program/Task-3(Weather forecast)/1.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

city_label = tk.Label(root, text="Enter city name or zip code", font=("Helvetica", 24))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 20), bg="white")
city_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather, font=("Helvetica", 20), bg="lightblue")
fetch_button.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", bg="white", font=("Helvetica", 20))
result_label.pack(pady=10)

root.mainloop()
