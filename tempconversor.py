temperature = float(input("Enter the actual temperature:"))
scale = str.lower(input("Enter the scale will be converted: "))
newscale = str.lower(input("Enter the new scale: "))

ctof = ((temperature)*(9/5)+32)
ctok = (temperature+273.15)
ftoc = ((temperature-32)*(5/9))
ftok = ((temperature-32)*(5/9)+273.15)
ktoc = (temperature-273.15)
ktof = ((ktoc)*(9/5)+32)


if scale == "celsius" and newscale == "fahrenheit":
    print(temperature,"°C equals", ctof,"°F.");
elif scale == "celsius" and newscale == "kelvin":
    print(temperature,"°C equals", ctok,"K.")
elif scale == "fahrenheit" and newscale == "celsius":
    print(temperature,"°F equals", ftoc,"°C.")
elif scale == "fahrenheit" and newscale == "kelvin":
    print(temperature,"°F equals", ftok,"K.")
elif scale == "kelvin" and newscale == "celsius":
    print(temperature,"K equals", ktoc,"°C.")
elif scale == "kelvin" and newscale == "fahrenheit":
    print(temperature,"K equals", ktof,"°F.")
else:
    print("Enter a valid scale!")



