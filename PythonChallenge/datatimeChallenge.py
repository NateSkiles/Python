"""
The Portland-based company you work for just opened two new branches. One is in 
New York City, the other in London. They need a very simple program to find out 
if the branches are open or closed. The hours of both branches are 9:00 a.m.-5:00 
p.m. in their own time zone.

Create a script that will find out the current times in the Portland HQ and NYC 
and London branches. Then, compare that time with each branch's hours to see if 
they are open or closed.

Print out to the screen the three branches and whether they are open or closed.
"""
import datetime
import pytz


def formatTime(myTime):  # Format our time to readable a readable output
    return myTime.strftime("%H:%M")


def officeHours(x):
    x = datetime.datetime.strptime(formatTime(x), "%H:%M")  # Store time, as string
    start = datetime.datetime.strptime("9:00", "%H:%M")     # Open time as a string
    end = datetime.datetime.strptime("17:00", "%H:%M")      # Close time as string
    # If x is within the limits of 9am-5pm: return True; else return false
    if start <= x <= end:
        return True
    else:
        return False


def openClose(localTime):
    if officeHours(localTime):  # If officeHours is True, print open
        print('Office is open!')
    else:
        print('Office is closed.')


time = pytz.utc.localize(datetime.datetime.utcnow())    # Current UTC time
pdxTime = time.astimezone(pytz.timezone('America/Los_Angeles'))     # Convert datetime objects into..
nycTime = time.astimezone(pytz.timezone('America/New_York'))        # aware objects with timezones..
ldnTime = time.astimezone(pytz.timezone('Europe/London'))           # local to office branches

print('Portland Office:')
print('Local time:', (formatTime(pdxTime)))
print(openClose(pdxTime))

print('New York Office:')
print('Local time:', (formatTime(nycTime)))
print(openClose(nycTime))

print('London Office:')
print('Local time:', (formatTime(ldnTime)))
print(openClose(ldnTime))
