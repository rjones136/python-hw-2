#problem:
#convert degrees farenheit to the Kelvin temperature scale
#input: temperature in farenheit 
#output: temperature Kelvin
#process: convert farenheit to Celsius, then add 273.15 

print("Welcome to the Farenheit to Kelvin converter")

farenheit = float(input("Enter temperature in Farenheit: "))
celsius = (farenheit - 32) * 5 / 9
kelvin = celsius + 273.15

print("Your temperature in kelvin is", kelvin)

