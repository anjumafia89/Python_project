#Speed Comparison
# Develop a program that takes two speeds (in km/h and mph), converts them to the same unit, and checks which one is faster.
speed_kph = float(input("Enter speed in km/h: "))
speed_mph = float(input("Enter speed in mph: "))

#(1 mph = 1.60934 km/h)
converted_speed_mph = speed_mph * 1.60934

if speed_kph > converted_speed_mph:
    print("Speed in km/h is faster.")
elif converted_speed_mph > speed_kph:
    print("Speed in mph is faster.")
else:
    print("Both speeds are equal.")