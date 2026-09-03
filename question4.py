#problem:
#convert degrees Celsius to the Kelvin temperature scale
#input: temperature in celsius 
#output: temperature Kelvin
#process: add 273.15 to the celsius temperature

print("Welcome to the Celsius to Kelvin converter")

celsius = float(input("Enter temperature in celsius: "))
kelvin = celsius + 273.15

print("Your temperature in kelvin is", kelvin)
