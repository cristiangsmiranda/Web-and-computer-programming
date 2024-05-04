def wind_chill():
    choose = ""
    while choose.lower() != "no":
        V = 5
        choice = input("Fahrenheit or Celsius (F/C)? ")
        temperature = int(input("What is the temperature? "))
        if choice.lower() == "c":
            temperature = (temperature * 1.8) + 32
            print(f"the temperature in fahrenheit is: {temperature:.1f} degrees. ")
        while V <= 60:
            Wind_Chill_f = 35.74 + (0.6215 * temperature) - 35.75 * (V ** 0.16) + (0.4275 * temperature) * (V ** 0.16)
            print(f"At temperature:{temperature}F, and wind speed {V} mph, the windchill is: {Wind_Chill_f:.2f}F ")
            V += 5
        choose = input("Do your want to continue? (yes/no) ")
wind_chill()