import requests
from datetime import datetime

class weather:
    def __init__(self):
        self.__api="e86c09aafe879f62953d2b305847b54d"
        self.__units='metric'
        self.__lang='en'
        self.__city=''
        self.__data=''
    
    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self,userLang):
        self.__lang=userLang

    @property
    def city(self):
        return self.__city
    
    @city.setter
    def city(self,userCity):        
        self.__city=userCity

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self,data):
        self.__data=data

    def userInterface(self):
        try:
            self.city=input("Input city name: ")
            self.lang=input("Select output language: 'en' for English, 'ru' for Russian etc. (default English): ")
            r=requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':self.__city,'units':self.__units,'lang':self.__lang,'APPID':self.__api})
            self.data=r.json()
        except:
            print("Error")
        if self.lang=='ru':
            self.outputRu() 
        else:
            self.outputEn()

    def outputEn(self): 
        try:         
            dateTime=datetime.fromtimestamp(self.data['dt']).strftime('%Y-%m-%d %I:%M:%S %p')
            print("Update time:",dateTime)
            print("City:",self.data['name'])
            print("Country:",self.data['sys']['country'])
            print("Temperature:",'{0:+3.0f}'.format(self.data['main']['temp']))
            print("Weather:",self.data['weather'][0]['description'].capitalize())
            print("Wind:",self.data['wind']['speed'],'m/s')
        except:
            print("Something wrong")

    def outputRu(self):  
        try:        
            dateTime=datetime.fromtimestamp(self.data['dt']).strftime('%d/%m/%Y %H:%M')
            print("Время обновления:",dateTime)
            print("Город:",self.data['name'])
            print("Код страны:",self.data['sys']['country'])
            print("Температура:",'{0:+3.0f}'.format(self.data['main']['temp']))
            print("Погода:",self.data['weather'][0]['description'].capitalize())
            print("Ветер:",self.data['wind']['speed'],'м/с')
        except:
            print("Что-то не так")
            

a=weather()
a.userInterface()
