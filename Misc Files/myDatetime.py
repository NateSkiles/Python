import datetime

x = datetime.datetime.now()

#print year and date
print(x.year)
print(x.strftime("%A")) #strfime() method formats date objects into strings

#create a date
y = datetime.datetime(2020, 5, 17) #hour, minute, second, microsecond, tz
print(y)

#my datetime format
print(x.strftime("%x %A  %B %Y"))
