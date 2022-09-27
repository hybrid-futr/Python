import requests
from bs4 import BeautifulSoup 
import pandas as pd

#SCRAPE THE PAGE
#Download the web page containing the forecast
#Create a BeautifulSoup class to parse parse the page. I used 'lxml' instead of 'html.parser'
#Find the 'div' ID 'seven-day-forecast-list' and assign to 'seven-day'
#In 'seven_day' find each individual forecast item ('tombstone-container') and locate Tonight's forecast
#Assign 'forecast_items[2]' to 'tonight' variable
#Extract and print
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.0536&lon=-118.2454#.YxediC2B2Ls")
soup = BeautifulSoup(page.content, 'lxml') #'pip3 install lxml' if not installed
seven_day = soup.find(id="seven-day-forecast-list")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[2]
print(tonight.prettify())

#EXTRACT FROM PERIOD
#The name of the forecast item ('period-name')
#The short decription ('short-desc')
#The temperature('temp')
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print('\n', period, '\n', short_desc, '\n', temp)

#EXTRACT FROM OBJECT
#Create a bs4 'img' object and pass the 'title' attribute
img = tonight.find("img")
desc = img['title']
print('\n', desc)

#EXTRACT ALL INFORMATION
#Select all items with the class 'period-name' inside an item with the class 'tombstone-container'
#Use a list comprehension to call the 'get_text' method on each BeautifulSoup object
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print('\n', periods,'\n', short_desc, '\n', temps, '\n', descs)

#USE PANDAS 
#print(len(periods), len(short_descs), len(temps), len(descs))
#I omitted "temp" because of the 'ValueError: All arrays must be of the same length' error. See print(len('...') above.
weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    #"temp": temps,
    "desc":descs
})
print('\n', weather)

#EXPORT CSV
#Export csv to Desktop with index, i.e. no index = FALSE
weather.to_csv('jaimeramirez\Desktop\weatherscrape.csv')
