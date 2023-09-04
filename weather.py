from tkinter import *
from PIL import Image, ImageTk
import requests

# function

def getImage(icon):
    img2 = Image.open("./img/"+icon+".png")
    img2 = img2.resize((70, 70))
    photo2 = ImageTk.PhotoImage(img2)
    canvas.delete('all')
    canvas.create_image(0, 0, anchor='nw', image=photo2)
    canvas.image = photo2


def getWeather(city):
    key = "dbe32dfd769b2c24783829769321409d"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weatherData = response.json()
   
    try:
        l5['text'] = ""
        l11['text'] =str(weatherData['main']['temp'])+" °C"
        l22['text'] = str(weatherData['main']['humidity'])+" %"
        l33['text'] =str(weatherData['wind']['speed'])+" km/h"
        l44['text'] =weatherData['weather'][0]['description']
        l6['text'] = weatherData['name']
        icon = weatherData['weather'][0]['icon']
        getImage(icon)
    except:
        l11['text'] = ""
        l22['text'] = ""
        l33['text'] = ""
        l44['text'] = ""
        l6['text'] = ""
        canvas.delete('all')
        l5['text'] = "Please Enter The Correct City Name !"
    

root = Tk()
root.geometry("900x600")

# key
# dbe32dfd769b2c24783829769321409d
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

# image
img = Image.open("weather.png")
img = img.resize((900, 600))
photo = ImageTk.PhotoImage(img)
bgImg = Label(root, image=photo)
bgImg.pack()

# Frame
f = Frame(root, bd=4, bg="#233142")
f.place(x=250, y=131, height=40, width=400)

# entry
cityName = StringVar()
input = Entry(f, width=21, font="lucida 17 bold",
              justify="center", bg="#eaeaea", textvariable=cityName)
input.grid(row=0, column=0, sticky=W)

# button
b = Button(f, font="lucida 13 bold", bg="#f05d23", fg="#eaeaea",
           text="get weather", bd=2, command=lambda: getWeather(input.get()))
b.grid(row=0, column=1, padx=8)

# 4 labels

l1 = Label(root, text="Temperature", bg="#0c005a",
           fg="#eaeaea", font="lucida 20 bold")
l1.place(x=70, y=210, height=50, width=170)
l11 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 20 bold")
l11.place(x=70, y=400, height=50, width=170)

l2 = Label(root, text="Humidity", bg="#0c005a",
           fg="#eaeaea", font="lucida 20 bold")
l2.place(x=268, y=210, height=50, width=170)
l22 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 20 bold")
l22.place(x=268, y=400, height=50, width=170)

l3 = Label(root, text="Wind Speed", bg="#0c005a",
           fg="#eaeaea", font="lucida 20 bold")
l3.place(x=463, y=210, height=50, width=170)
l33 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 20 bold")
l33.place(x=463, y=400, height=50, width=170)

l4 = Label(root, text="Description", bg="#0c005a",
           fg="#eaeaea", font="lucida 20 bold")
l4.place(x=657, y=210, height=50, width=170)
l44 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 18 bold")
l44.place(x=657, y=400, height=50, width=170)

# exception
l5 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 20 bold")
l5.place(x=142, y=520, height=50, width=600)

# img "./img/"+icon+'.png'

# weather name
l6 = Label(root, text="", bg="#0c005a", fg="#eaeaea", font="lucida 20 bold")
l6.place(x=620, y=30, height=60, width=170)


# canvas
canvas = Canvas(root, bg="light blue")
canvas.place(x=800, y=30, height=60, width=70)

root.mainloop()
