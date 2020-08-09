import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
print(percent)
print(battery)
print(plugged)