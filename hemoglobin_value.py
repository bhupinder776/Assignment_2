# Get biological gender and hemoglobin value from the user
gender = input("Enter biological gender (male/female): ").strip().lower()
hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

# Determine if the hemoglobin value is low, normal, or high based on gender
if gender == "female":
    if hemoglobin_value < 117:
        print("Hemoglobin value is low.")
    elif 117 <= hemoglobin_value <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Hemoglobin value is low.")
    elif 134 <= hemoglobin_value <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender input.")




# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

while True:
    # Get biological gender and hemoglobin value from the user
    gender = input("Enter biological gender (male/female) or 'exit' to quit: ").strip().lower()

    # Exit condition
    if gender == 'exit':
        break

    hemoglobin_value = float(input("Enter hemoglobin value (g/l): "))

    # Determine if the hemoglobin value is low, normal, or high based on gender
    if gender == "female":
        if hemoglobin_value < 117:
            print("Hemoglobin value is low.")
        elif 117 <= hemoglobin_value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif gender == "male":
        if hemoglobin_value < 134:
            print("Hemoglobin value is low.")
        elif 134 <= hemoglobin_value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid gender input.")


