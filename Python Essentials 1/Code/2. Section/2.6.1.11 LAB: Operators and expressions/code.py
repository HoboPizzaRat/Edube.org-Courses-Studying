hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

# calculating added hours
addedHours = dura // 60
dura -= addedHours * 60

# calculating added minutes + hours
addedHours += (mins + dura)//60
mins = (mins + dura) % 60

# calculating the hourtime
hour = (hour+addedHours)%24

# printing time
print(hour, mins, sep=":")

