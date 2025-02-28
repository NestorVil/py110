# P:
#   Input: A floating point number representing degrees between 0 and 360
#   Output: A string representing that angle in degrees, minutes, and seconds

def dms(value):
    degrees = value // 1
    minutes = value % 1 * 60
    seconds = int(minutes % 1 * 60)
    print(degrees, minutes, seconds)
    return (f'{int(degrees)}\u00B0{int(minutes):02d}\'{seconds:02d}"')

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")