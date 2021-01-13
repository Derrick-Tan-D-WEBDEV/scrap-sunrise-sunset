from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from sys import exit
from datetime import datetime,timedelta
import dateutil.relativedelta
import psycopg2
import pandas as pd
import mysql.connector

def scrap_data():
    PATH = "your-chrome-driver-path"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(PATH,options=options)


    #driver get exchange rate
    driver.get("https://www.timeanddate.com/sun/@1780777")
    print("Welcome to Sun Rise scraper")
    time.sleep(10)
    body = driver.find_element_by_xpath('/html/body/div[6]/main/article/section[1]/div[2]/table/tbody')
    raw_data = body.find_elements_by_tag_name("tr")

    current_time = ""
    sun_direction = ""
    sun_altitude = ""
    sun_distance = ""
    next_equinox = ""
    sunrise_today = ""
    sunset_today = ""
    for rd in raw_data:
        # row = rd.find_elements_by_tag_name("td")
        # print(row[0].text.splitlines()) 
        # for r in row:
        data = rd.text.splitlines()
        data = data[0]

        if "Current Time:" in data:
            current_time = data.replace('Current Time: ','')
        
        if "Sun Direction:" in data:
            data = data.replace('Sun Direction: ','')
            sun_direction = data.replace('° ENE↑','')

        if "Sun Altitude:" in data:
            data = data.replace('Sun Altitude: ','')
            sun_altitude = data.replace('°','')

        if "Sun Distance:" in data:
            data = data.replace('Sun Distance: ','')
            sun_distance = data.replace(' million km','')

        if "Next Equinox:" in data:
            data = data.replace('Next Equinox: ','')
            next_equinox = data.replace('(Sep. Eq.)','')

        if "Sunrise Today:" in data:
            sunrise_today = data.replace('Sunrise Today: ','')
        
        if "Sunset Today:" in data:
            sunset_today = data.replace('Sunset Today: ', '')

    print(current_time)
    print(sun_direction)
    print(sun_altitude)
    print(sun_distance)
    print(next_equinox)
    print(sunrise_today)
    print(sunset_today)
    
    try: 
        conn = psycopg2.connect(host='your-host',
                            port=5433,
                            user='your-username',
                            password='your-pwd',
                            database='your-db') # To remove slash

        cursor = conn.cursor()
        cursor.execute("INSERT INTO sunrise_sunset(curr_time, sun_direction, sun_altitude, sun_distance, next_equinox, sunrise_today, sunset_today) VALUES(%s, %s, %s, %s, %s, %s, %s)", (current_time, sun_direction, sun_altitude, sun_distance, next_equinox, sunrise_today, sunset_today))
        conn.commit() # <- We MUST commit to reflect the inserted data
        cursor.close()
        conn.close()
        driver.close()
    except Exception as error:
        print(error)

while True:
    scrap_data()
    time.sleep(10)