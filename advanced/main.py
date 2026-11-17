robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}



while True:
    print("1. View All Settings")
    print("2. Look Up a Setting")
    print("3. Change a Setting")
    print("4. Add a Setting")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        for key, value in robot.items():
            print(f"{key}: {value}")

    elif choice == 2:
        setting = input("Enter a setting to look up: ")
        value = robot.get(setting)
        if value is not None:
            print(f"{setting}: {value}")
        else:
            print("Setting not found.")

    elif choice == 3:
        setting = input("Enter a setting to change: ")
        if setting in robot:
            robot[setting] = input("Enter the new value: ")
        else:
            print("Setting not found.")

    elif choice == 4:
        setting = input("Enter a new setting: ")
        value = input("Enter the value for the new setting: ")
        robot[setting] = value

    elif choice == 5:
        break
