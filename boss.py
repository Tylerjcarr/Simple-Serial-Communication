import serial
import time

#define the serial port. mine is ttyACM0 on my pi.
ser = serial.Serial('/dev/ttyACM0', 115200) #the baud rate for my uno r4 wifi is this, change based on yours
try:
    while True:
        #input to turn the LED on
        ser.write(b'on\n')
        print("LED turned on") #on the pi end to now that it sent the command, not needed though
        time.sleep(1)  #2 second delay
        
        #input to turn off LED
        ser.write(b'off\n')
        print("LED turned off")
        time.sleep(1)  #2 second delay

        # Send command to make the LED blink
        ser.write(b'blink\n')
        print("LED blinking")
        time.sleep(2)  # Wait for 5 seconds
except KeyboardInterrupt:
    ser.close()  #close serial port on Ctrl C
