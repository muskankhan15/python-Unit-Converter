while True:
    print("""
    ---- UNIT CONVERTER + CALCULATOR ----

    UNIT CONVERTER
    1. Kilometers to Miles
    2. Celsius to Fahrenheit
    3. Kilograms to Pounds
    4. km/h to m/s
    5. m/s to km/h
    6. Minutes to Hours
    7. Hours to Minutes

    CALCULATOR
    8. Addition
    9. Subtraction
    10. Multiplication

    11. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print("Miles:", km * 0.621371)

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", (c * 9/5) + 32)

    elif choice == "3":
        kg = float(input("Enter kilograms: "))
        print("Pounds:", kg * 2.20462)

    elif choice == "4":
        kmh = float(input("Enter speed in km/h: "))
        print("Speed in m/s:", kmh / 3.6)

    elif choice == "5":
        ms = float(input("Enter speed in m/s: "))
        print("Speed in km/h:", ms * 3.6)

    elif choice == "6":
        minutes = float(input("Enter minutes: "))
        print("Hours:", minutes / 60)

    elif choice == "7":
        hours = float(input("Enter hours: "))
        print("Minutes:", hours * 60)

    elif choice == "8":
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print("Result:", num1 + num2)

    elif choice == "9":
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print("Result:", num1 - num2)

    elif choice == "10":
        num1 = float(input("Enter num1: "))
        num2 = float(input("Enter num2: "))
        print("Result:", num1 * num2)

    elif choice == "11":
        print("Exit")
        break

    else:
        print("Invalid choice. Please try again.")
