def add_time(start_h, time, optional = False ):
    initial = []
    initial2 = []
    impu_time = []
    hour = ""
    hour_pm = ""
    minutes = ""
    indi = 0
    day = 0
    week = 0
    alternative = ""
    other = " "
    days = ["Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday","Sunday"]
    impu_time = time.split(":")
    initial = start_h.split(" ")
    initial2 = initial[0].split(":")
    if initial[1] == "PM":
        initial2[0] = int(initial2[0]) + 12
    hour = int(impu_time[0]) + int(initial2[0])
    minutes = int(impu_time[1]) + int(initial2[1])
    if minutes > 60:
        hour += 1
        minutes = minutes - 60
        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)
    if hour > 24:
        day += hour//24
        hour = hour - (day * 24)
    if day == 1:
        other = "(next day)"
    elif day > 1:
        other = "(" + str(day) + " days later)"
    else:
        other = ""
    if optional != False:
        optional = optional.title()
        indi = days.index(optional) + day
        if indi > 6:
            week = indi - 6
            alternative = days[week]
        else:
            alternative = days[indi]
    if optional == False:
        if hour > 12:
            hour_pm = hour - 12
            print("{}:{} PM {}".format(hour_pm, minutes, other))
        elif hour == 12:
            print("{}:{} PM {}".format(hour, minutes, other))
        elif hour == 0:
            print("{}:{} AM {}".format(12, minutes, other))
        else:
            print("{}:{} AM {}".format(hour, minutes, other))
    else:
        if hour > 12:
            hour_pm = hour - 12
            print("{}:{} PM, {} {}".format(hour_pm, minutes, alternative, other))
        elif hour == 12:
            print("{}:{} PM {} {}".format(hour, minutes, alternative, other))
        elif hour == 0:
            print("{}:{} AM {} {}".format(12, minutes, alternative, other))
        else:
            print("{}:{} AM, {} {}".format(hour, minutes, alternative,other))


add_time("12:10 PM", "100:59", "MONDAY")

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
