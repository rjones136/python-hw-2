#Problem:
#Convert kilometers to smoots
#Input: distance in kilometers
#Output: distance in smoots
#Process: convert kilometers to meters, then meters to smoots

print("welcome to the Smoot converter")

kilometers = float(input("Enter distance in kilometers:"))
meters = kilometers * 1000
smoots = meters / 1.7

print("Your distance in Smoots is", smoots)
