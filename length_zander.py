# Size limit for zander in centimeters
SIZE_LIMIT = 42

# Ask the user for the length of the zander
zander_length = float(input("Enter the length of the zander in centimeters: "))

# Check if the zander meets the size limit
if zander_length < SIZE_LIMIT:
    # Calculate how many centimeters below the size limit the fish is
    difference = SIZE_LIMIT - zander_length
    print(f"The zander is {difference:.1f} centimeters below the size limit.")
    print("Please release the fish back into the lake.")
else:
    print("The zander meets the size limit. You can keep it!")

