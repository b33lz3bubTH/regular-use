from mac_osx_dynamic import config 
from time import gmtime, strftime
from datetime import datetime, time
import os
import time as systemTime


def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.utcnow().now()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]



def main():
    current_module = "mac_osx_dynamic"
    wallpapers = config.getWallPaper()
    current_hour = strftime("%H")
    current_min = strftime("%M")

    print("current_hour: ", current_hour)
    print("current_min: ", current_min)

    for timeLapsImage in wallpapers:
        print(timeLapsImage)
        start = time(timeLapsImage[0])
        end = time(timeLapsImage[1])
        res = is_between(f'{current_hour}:{current_min}',(f'{start}:00', f'{end}:00'))
        print("CURRENT TIME: ", start, end)
        if res:
            wall = "feh --bg-fill ./"+ current_module+"/"+timeLapsImage[2]
            print(wall)
            os.system(wall)
    systemTime.sleep(30*60)

while True:    
    main()
