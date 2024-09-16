#importing modules
import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

# Function to get notification of weather report
def getNotification():
    cityName = place.get()  # getting input of name of the place from user
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base URL from where we extract weather report
    apiKey = 'd850f7f52bf19300a9eb4b0aa6b80f0d'  # Replace this with your actual API key

    try:
        # Construct the URL to get weather conditions of a city
        url = f"{baseUrl}appid={apiKey}&q={cityName}"
        response = requests.get(url)  # requesting for the content of the URL
        x = response.json()  # converting it into JSON

        if x["cod"] != "404":  # check if city is found
            y = x["main"]  # getting the "main" key from the JSON object

            # getting the "temp" key of y
            temp = y["temp"]
            temp -= 273.15  # converting temperature from Kelvin to Celsius

            # storing the value of the "pressure" key of y
            pres = y["pressure"]

            # getting the value of the "humidity" key of y
            hum = y["humidity"]

            # storing the value of "weather" key in variable z
            z = x["weather"]

            # getting the corresponding "description"
            weather_desc = z[0]["description"]

            # combining the above values as a string 
            info = (f"Here is the weather description of {cityName}:\n"
                    f"Temperature = {temp:.2f}°C\n"
                    f"Atmospheric pressure = {pres} hPa\n"
                    f"Humidity = {hum}%\n"
                    f"Weather description = {weather_desc}")

            # showing the notification 
            notification.notify(
                title="YOUR WEATHER REPORT",
                message=info,
                timeout=10)  # increased timeout to 10 seconds

        else:
            mb.showerror('Error', 'City Not Found')

    except Exception as e:
        mb.showerror('Error', str(e))  # show pop-up message if any error occurred

# Creating the window
wn = Tk()
wn.title("PythonGeeks Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

# Heading label
Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)

# Getting the place name
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

# Button to get notification
btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification)
btn.place(relx=0.4, rely=0.75)

# Run the window till closed by user
wn.mainloop()
