import serial 

#define the serial port. mine is ttyACM0 on my pi.
ser = serial.Serial('/dev/ttyACM0', 115200) #the baud rate for my uno r4 wifi is this, change based on yours
try: 
    while True: 
        line = ser.readline().decode().strip() #reads from the serial port 
        print("Received:", line) 
except KeyboardInterrupt: ser.close() #close serial port on Ctrl C

