def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    print("Temperature Converter")
    choice = input("Convert from (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? (C/F): ").upper()

    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid Input")

convert_temperature()
