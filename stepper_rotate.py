# stepper_rotate.py
"""
Description:
    This script drives a 28BYJ-48 stepper motor with a ULN2003 driver connected to a
    Raspberry Pi 4. It rotates the motor approximately 360 degrees (512 steps) using
    a predefined step sequence. GPIO.BOARD numbering is used for physical pins.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""

import RPi.GPIO as GPIO  # Import RPi.GPIO library to control Raspberry Pi GPIO pins
import time  # Import time library for adding delays

# Clean up any previously used GPIO configurations to ensure a fresh start
GPIO.cleanup()

# Set GPIO numbering mode to BOARD, using physical pin numbers (1-40)
GPIO.setmode(GPIO.BOARD)

# Define pins for ULN2003 driver inputs: IN1=Pin 11, IN2=Pin 13, IN3=Pin 15, IN4=Pin 19
pins = [11, 13, 15, 19]

# Configure each pin as an output to control the stepper motor coils
for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

# Step sequence for 28BYJ-48 stepper motor (8 half-steps for smooth rotation)
sequence = [
    [1, 0, 0, 1],  # Step 1: Energize coils 1 and 4
    [1, 0, 0, 0],  # Step 2: Energize coil 1
    [1, 1, 0, 0],  # Step 3: Energize coils 1 and 2
    [0, 1, 0, 0],  # Step 4: Energize coil 2
    [0, 1, 1, 0],  # Step 5: Energize coils 2 and 3
    [0, 0, 1, 0],  # Step 6: Energize coil 3
    [0, 0, 1, 1],  # Step 7: Energize coils 3 and 4
    [0, 0, 0, 1]   # Step 8: Energize coil 4
]

# Function to rotate the stepper motor
def step_motor(steps, delay=0.001):
    # Repeat for the specified number of steps (512 steps ~ 360 degrees)
    for _ in range(steps):
        # Iterate through each step in the sequence
        for step in sequence:
            # Set each pin (IN1-IN4) according to the current step's pattern
            for i in range(4):
                GPIO.output(pins[i], step[i])
            # Pause briefly to control rotation speed (0.001s per step)
            time.sleep(delay)

# Rotate the motor approximately 360 degrees (512 steps)
step_motor(512)  # ~360 degrees

# Clean up GPIO configurations to reset all used pins
GPIO.cleanup()