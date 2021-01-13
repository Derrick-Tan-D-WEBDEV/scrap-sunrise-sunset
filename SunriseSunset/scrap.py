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
from datetime import timedelta, date

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

start_dt = date(2015, 12, 20)
end_dt = date(2016, 1, 11)
for dt in daterange(start_dt, end_dt):
    print(dt.strftime("%Y-%m-%d"))

    
def scrap_data():
    PATH = "D:\derrick stuff\chromedriver\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(PATH,options=options)


    #driver get exchange rate
    driver.get("https://www.timeanddate.com/sun/@1780777")
    print("Welcome to Sun Rise scraper")
    time.sleep(10)
    body = driver.find_element_by_xpath('/html/body/div[1]/div[6]/main/article/section[3]/div/div[2]/div/table/tbody')
    raw_data = body.find_elements_by_tag_name("tr")
    count = 1
    for rd in raw_data:
        row = rd.find_elements_by_tag_name("td")
        #print(row[0].text.splitlines())
        temp_data = None
        print('Day ',count)
        print('--------------------')
        for r in row:
            data = r.text.splitlines()
            temp_data = data
            if data[0] != 'Rise':
                print(data[0])
        print('--------------------')

        if temp_data[0] != 'Rise':
            count += 1
# for rate in rates:
#     data = rate.text.splitlines()
#     data_split = data[0].split()
    
#     if "USD" not in data_split:
#         if last_day_last_month.strftime("%d %m %Y") == pd.to_datetime(data_split[0].strip()).strftime("%d %m %Y"):
#             tdy_rate = data_split[1]
#             break
            
#     if "THB100" in data_split:
#         break    

# driver.close()


    # if check_date(last_day_last_month):
    #     print("Same")
    # else:
    #     #insert exchange rate
    #     print("insert")
    #     try:
    #         mydb = mysql.connector.connect(
    #             host="mysql.v-one.my",
    #             user="vone",
    #             password="$ViTrox$",
    #             database="sales_ticket"
    #         )
    #         cursor = mydb.cursor()

    #         sql = "INSERT INTO exchange_rate (rate, date) VALUES (%s, %s)"
    #         val = (tdy_rate,last_day_last_month)

    #         cursor.execute(sql, val)
    #         mydb.commit()
    #     except (Exception) as error:
    #         print("Insert Error: ", error)
    #     finally:
    #         if mydb is not None:
    #             mydb.close()
    #     time.sleep(60)
