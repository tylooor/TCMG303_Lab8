#!/usr/bin/python
#This script converts speed from KPH to MPH.
#The conversion formula for kph to mph is :
#1 kilometer = 0.621371192 miles

kph = int(input("Enter KPH: "))
mph =  0.6214 * kph
print("Speed:", kph, "KPH =", mph, "MPH")
if mph > 70:
	print("Slow down! Your were speeding... ")
else:
	print("You are a safe driver!")

