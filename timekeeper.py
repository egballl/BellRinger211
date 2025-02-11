import time
import datetime
currents = datetime.datetime.now()
currentdays = int(currents.strftime('%d'))
currentdd = int(currents.strftime('%H'))
print("Current Time:", currents)
feb14 = datetime.datetime(2025, 2, 14, 0)
feb14track = int(feb14.strftime('%d'))
feb14trackss = int(feb14.strftime('%H'))
feb14math = feb14track - currentdays
print("Days until Feb 14: ", feb14math)
hours = feb14trackss - currentdd
print("hours until feb14:", hours)

days = feb14math*24
print("Hours until valentines: ", days + hours, "hours")
