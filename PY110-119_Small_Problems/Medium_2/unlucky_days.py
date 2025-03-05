# P:
#   Input: An integer representing a year
#   Output: An integer representing the number of Friday the 13ths in that year
#   Explicit:
#       The year will always be after 1752 (not caring for pre-gregorian calander)
#       Will probably need datetime module
# E:
    # print(friday_the_13ths(1986) == 1)      # True
    # print(friday_the_13ths(2015) == 3)      # True
    # print(friday_the_13ths(2017) == 2)      # True
# D:
#   The datetime module
# A: supplied by launchschool
#   1. Iterate over the months of the given year
#   2. For each month, get the day that falls on the 13th
#   3. Count the 13ths that fall on a friday
#   4. Return the count


import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13)
                   for month in range(1, 13)]

    count = 0
    for day in thirteenths:
        if day.weekday() == 4:
            count += 1

    return count

print(friday_the_13ths(1986) == 1)      # True