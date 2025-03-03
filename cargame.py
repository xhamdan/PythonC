command=""
started = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
        print("Car Already Started!")
    else:
        started = True
        print("Car is started...")
    elif command == "stop":
        print("Car is Stopped")
    elif command == "help":
        print("""
        Start - To Start the Car
        Stop  - To Stop the Car
        Quite - To Quit
        
        """)
    elif command =="quit":
        break
else:
    print("Oops - I do not understand this")
