import time

def digital_clock():
    try:
        while True:
            current_time = time.strftime("%H:%M:%S")
            print("Current Time:", current_time, end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nClock stopped.")

#Run clock
digital_clock()