import tkinter as tk
from pip._vendor import requests
import datetime
from tkinter import *
from tkinter import *
splash_win= Tk()
splash_win.title("Splash Screen Example")
splash_win.geometry("400x400")
splash_win.configure(bg='#fa2a55')
splash_win.overrideredirect(True)
splash_label= Label(splash_win, text= """Welcome!
Stay home! stay safe!""", fg= "white",background="#fa2a55", 
font= ('Pacificio', 30),anchor="w").pack(pady=20)
def mainWin():
   splash_win.destroy()
splash_win.after(4000, mainWin)
def getCovidData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases']) 
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    affected_countries= str(json_data['affectedCountries'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text = "Total Cases: "+total_cases+
        "\n"+"Total Deaths: "+total_deaths+
        "\n"+"Today Cases: "+today_cases+
        "\n"+"Today Deaths "+today_deaths+
        "\n"+"Today Recovered: "+today_recovered+
        "\n"+"Affected countries:  "+affected_countries)
    

    a=str(date)
    label2.config(text="last updated  :  "+ a,bg="black",foreground="#FFF",font=z) 
canvas = tk.Tk()
border_color = Frame(canvas, background="red")
label = Label(border_color, text="This is a Label widget", bd=5)
canvas.geometry("400x400")
canvas.title("Corona Analysis")
canvas.configure(bg='#fa2a55',bd=8)
z=("Pacifico",15)
f = ("Pacifico",20)
label = tk.Label(canvas, font = f,bg="black",foreground="white")
label.pack(pady=20)
button = tk.Button(canvas, font = f,text = "Load",command = getCovidData,bd=7,width=15,height=0,bg="black",foreground="#FFF")
button.pack(pady = 20)
label2 = tk.Label(canvas, font = 15)
label2.pack()
getCovidData()
canvas.mainloop()
