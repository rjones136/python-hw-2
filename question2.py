#problem:
#convert centimeters to mickeys
#input: distance in centimeters
#output: distance in mickeys
#process: convert centimeters to millimeters, then multiply by 16 

print("Welcome to the Mickey converter")

centimeters = float(input("Enter distance in centimeters: "))
millimeters = centimeters * 10
mickeys = millimeters * 16

print("Your distance in mickeys is", mickeys)
