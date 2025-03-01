# P:
#   Input: An integer representing a minute
#   Output: A string in 24-hour format aka hh:mm format
#   Explicit:
#       The input integer can be negative so -3 will be 23:57
#       Can pretend daylight savings time and standard time don't exist
#       Since the integer is minutes will need to work that into hours
# E:
# print(time_of_day(0) == "00:00")        # True
# print(time_of_day(-3) == "23:57")       # True
# print(time_of_day(35) == "00:35")       # True
# print(time_of_day(-1437) == "00:03")    # True
# print(time_of_day(3000) == "02:00")     # True
# print(time_of_day(800) == "13:20")      # True
# print(time_of_day(-4231) == "01:29")    # True
# D:
#   F-strings with 0 padding
#   dividing minutes into hours if needed
# A:
#   1. Create "hours" variable and calculate if the input integer has hours
#   2. Any leftovers will go into "minutes" variable
#   3. If the input integer is negative, make t hem negative hours and minutes
#   4. Return the hours:minutes variables as a string
# D:
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24
MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR

def time_of_day(delta_minutes):
    while delta_minutes < 0:
        delta_minutes += MINUTES_PER_DAY

    delta_minutes = delta_minutes % MINUTES_PER_DAY
    hours = delta_minutes // MINUTES_PER_HOUR
    minutes = delta_minutes % MINUTES_PER_HOUR

    return f"{hours:02d}:{minutes:02d}"
 
    
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# :(