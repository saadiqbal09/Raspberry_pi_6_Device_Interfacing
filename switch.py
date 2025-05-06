"""
Description:
    This script monitors four toggle switches connected to a Raspberry Pi 4. It prints
    'Switch X ON!' when a switch is ON (connected to GND) and 'Switch X OFF!' when OFF.
    GPIO.BOARD numbering is used with internal pull-up resistors. The state is checked
    every 0.1 seconds. Note: Pins 38, 37, 33 conflict with LCD pins in other scripts.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""

import RPi.GPIO as GPIO  # Import RPi.GPIO library to control Raspberry Pi GPIO pins
import time  # Import time library for adding delays

# Clean up any previous GPIO configurations to ensure a fresh start
GPIO.cleanup()

# Set GPIO numbering mode to BOARD, using physical pin numbers (1-40)
GPIO.setmode(GPIO.BOARD)

# Define pins for four toggle switches
switch_pins = [38, 36, 37, 33]

# Setup each switch pin as input with internal pull-up resistor
for pin in switch_pins:
    try:
        # Configure pin as input with pull-up (HIGH when switch is OFF, LOW when ON)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    except Exception as e:
        # Print error if pull-up setup fails
        print(f"Error setting up pin {pin}: {e}")
        # Fallback: Try setting up without pull-up resistor
        try:
            GPIO.setup(pin, GPIO.IN)
            print(f"Set up pin {pin} without pull-up resistor")
        except:
            # Print error if fallback setup fails
            print(f"Could not set up pin {pin}")

# Read switch states in a loop
try:
    while True:
        # Iterate through each switch pin
        for i, pin in enumerate(switch_pins):
            try:
                # Check if switch is ON (LOW, connected to GND)
                if GPIO.input(pin) == GPIO.LOW:
                    print(f"Switch {i+1} ON!")
                else:
                    # Switch is OFF (HIGH, due to pull-up)
                    print(f"Switch {i+1} OFF!")
            except Exception as e:
                # Print error if reading pin fails
                print(f"Error reading pin {pin}: {e}")
        # Print separator line between sets of readings
        print("-" * 20)
        # Pause for 0.1 seconds before next reading
        time.sleep(0.1)
except KeyboardInterrupt:
    # Handle manual interruption (Ctrl+C)
    GPIO.cleanup()
    print("Program terminated")
finally:
    # Ensure GPIO pins are reset on exit
    GPIO.cleanup()
    print("GPIO cleaned up")