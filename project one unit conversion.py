def pounds_to_kg(pounds):
    return pounds * 0.45359237

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def feet_to_meters(feet):
    return feet * 0.3048

def inches_to_cm(inches):
    return inches * 2.54

def miles_to_km(miles):
    return miles * 1.60934


def main():
    while True:
        # The menu
        print("Choose a unit conversion: ")
        print("1. Pounds to Kilograms")
        print("2. Fahrenheit to Celsius")
        print("3. Feet to Meters")
        print("4. Inches to Centimeters")
        print("5. Miles to Kilometers")
        print("0. Exit")

        # user choice
        choice = input("Enter your choice of converter (1-5 or 0 to exit): ")

        if choice == '0':
            print("Bai Bai :3!")
            break 


        if choice in ['1', '2', '3', '4', '5']:
            quantity = float(input("Enter the quantity to convert: "))

            # Conversion
            if choice == '1':
                print(f"{quantity} pounds is {pounds_to_kg(quantity):.2f} kilograms.")
            elif choice == '2':
                print(f"{quantity} Fahrenheit is {fahrenheit_to_celsius(quantity):.2f} Celsius.")
            elif choice == '3':
                print(f"{quantity} feet is {feet_to_meters(quantity):.2f} meters.")
            elif choice == '4':
                print(f"{quantity} inches is {inches_to_cm(quantity):.2f} centimeters.")
            elif choice == '5':
                print(f"{quantity} miles is {miles_to_km(quantity):.2f} kilometers.")
        else:
            print("Invalid choice, womp womp... Please try again :)")


if __name__ == "__main__":
    main()