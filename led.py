"""
Description:
    This script controls an LED connected to a Raspberry Pi , making it blink
    every second (1s ON, 1s OFF). It uses GPIO.BOARD numbering for physical pin
    assignments and runs indefinitely until manually stopped.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""
import RPi.GPIO as GPIO  # Import GPIO library for Raspberry Pi
import time  # Import time library for delays

# Set GPIO numbering to BOARD (physical pin numbers)
GPIO.setmode(GPIO.BOARD)

# Define LED pin as physical Pin 29,31,33,35
led_pin = [29,31,33,35]
blink_duration = 0.5  # Duration for ON and OFF states in seconds

try:
    # Configure Pin 12 as an output
    GPIO.setup(led_pin, GPIO.OUT)
    print(f"LED control started on Pin {led_pin}. Press Ctrl+C to stop.")

    # Run infinite loop to blink the LED
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn LED ON
        time.sleep(blink_duration)
        GPIO.output(led_pin, GPIO.LOW)   # Turn LED OFF
        time.sleep(blink_duration)

except RuntimeError as e:
    print(f"GPIO error: {e}")
except KeyboardInterrupt:
    print("\nProgram terminated by user")
finally:
    # Clean up GPIO pins on exit
    GPIO.cleanup()
    print("GPIO cleaned up")