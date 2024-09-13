# Conversion factor from inches to centimeters
INCH_TO_CM = 2.54

# Use a while loop to repeatedly ask for input and perform the conversion
while True:
    # Ask the user to enter a length in inches
    inches = float(input("Enter length in inches (enter a negative value to exit): "))

    # Check if the input is negative to exit the loop
    if inches < 0:
        print("Negative value entered. Exiting the program.")
        break

    # Convert inches to centimeters
    centimeters = inches * INCH_TO_CM

    # Print the result
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")
