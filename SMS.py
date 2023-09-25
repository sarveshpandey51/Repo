import RPi.GPIO as GPIO
import time

# Define GPIO pin numbers
relay_pin = 11  # GPIO pin connected to the relay
sensor_pin = 6   # GPIO pin connected to the soil sensor

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        water = GPIO.input(sensor_pin)  # Read the soil sensor input

        if water == GPIO.HIGH:
            GPIO.output(relay_pin, GPIO.LOW)  # Turn off the relay
        else:
            GPIO.output(relay_pin, GPIO.HIGH)  # Turn on the relay

        time.sleep(0.4)  # Delay for stability

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Cleanup GPIO settings when the script exits
