def celsius_to_fahrenheit(degrees_celsius):
    return [round((degree * 9/5) + 32, 2) for degree in degrees_celsius]


degrees_celsius = [39.2, 36.5, 37.3, 37.8]
result = celsius_to_fahrenheit(degrees_celsius)
print(result)
