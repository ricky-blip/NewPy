# Date and time (Exercise)

import datetime as dt
from typing import AsyncGenerator # call library datetime as dt

print(5*"-" + "How to print Date Today" + 5*"-")
today = dt.date.today()
print(today)

print(5*"-" + "How to print Date Manually" + 5*"-")
dateborn = dt.date(1997,2,19)
print(dateborn)

print(5*"-" + "How to print Date with String" + 5*"-")
print(f"Today is    = {today:%A}")
print(f"Birthday is = {dateborn:%A}")

print("\n" + 5*"=" + "DATETIME BIRTHDAY" + 5*"=")

print("Please type your date month year")
date    = int(input("Date \t:"))
month   = int(input("Month \t:"))
year    = int(input("Year \t:"))

date_birthday = dt.date(year,month,date)
print(f"Your Birthday is : {date_birthday:%A},{date_birthday}")

print("\n" + 5*"=" + "YOUR AGE" + 5*"=")

today = dt.date.today()
ageday = today - date_birthday
agemonth = (ageday.days % 365) // 30
ageyear = ageday.days // 365

print(f"Today is                    : {today}")
print(f"Your Age in day now is      : {ageday}")
print(f"Your Age in month now is    : {agemonth} Months")
print(f"Your Age in year now is     : {ageyear} Years Old")
