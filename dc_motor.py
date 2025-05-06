"""
Description:
    This script controls a DC motor via an L298N driver connected to a Raspberry Pi 4.
    It runs the motor forward at full speed for 2 seconds, then stops. GPIO.BOARD
    numbering is used for physical pin assignments. External power is required for the motor.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""

import RPi.GPIO as GPIO # Import RPi.GPIO library to control Raspberry Pi 
import time  # Import time library for adding delays
#Clean up all the ports you've used.
GPIO.cleanup()
# Set GPIO numbering mode to BOARD, using physical pin numbers (1-40)
GPIO.setmode(GPIO.BOARD)
# Define L298N input pins: IN1 on Pin 16, IN2 on Pin 18
in1, in2 = 16, 18
# Configure IN1 (Pin 16) as an output to control motor direction
GPIO.setup(in1, GPIO.OUT)
# Configure IN2 (Pin 18) as an output to control motor direction
GPIO.setup(in2, GPIO.OUT)
# Set IN1 to HIGH (3.3V) and IN2 to LOW (0V) to run motor forward
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
print("The DC Motor is moving in FORWARD DIRECTION.")
# Keep motor running for 2 seconds
time.sleep(2)
# Set IN1 to LOW (0V) and IN2 to HIGH (3.3V) to run motor reversed
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
print("The DC Motor is moving in REVERSED DIRECTION.")
# Keep motor running for 2 seconds
time.sleep(2)
# Set IN1 and IN2 to LOW to stop the motor
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
print("The DC Motor is STOP.")
#Clean up all the ports you've used.
GPIO.cleanup()