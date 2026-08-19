from datetime import timedelta
from datetime import date
from datetime import datetime

# timedetla calculates the total time elapsed given the arguments
# weeks = passed weeks
# days = passed days
# hours = passed hours
delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

# you can multiply the time delta like any other arithmetic operator
delta2 = delta * 2
print(delta2)

# you can add time delta to the date object and it 
# will apply time difference to it
d = date(2019, 10, 4) + delta2
print(d)

# you can be more specific with your arguments 
# and also apply hours and minutes to it.
dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)

delta3 = timedelta(seconds=300)
delta3 *= 3
print(delta3)