command=""
while command != "quite":
    command = input(">").lower()
    if command == "start":
        print("Car is started...")
    elif command == "Stop":
        print("Car is Stopped")
    elif command == "help":
        print("""
        Start - To Start the Car
        Stop  - To Stop the Car
        Quite - To Quite
        
        """)
else:
    print("I do not understand this")