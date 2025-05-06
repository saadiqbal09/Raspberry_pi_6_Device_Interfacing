"""
Description:
    This script controls a servo motor via a Raspberry Pi 4 using PWM on physical pin 32 (GPIO 12).
    It moves the servo to 0, 90, and 180 degrees with delays, using BOARD numbering.
    Requires an external power supply for the servo.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""
import RPi.GPIO as GPIO  # Import RPi.GPIO library to control Raspberry Pi GPIO pins
import time  # Import time library for adding delays
# Set GPIO numbering to BOARD mode (physical pin numbers 1-40)
GPIO.setmode(GPIO.BOARD) 
# Define pin 32, set as output, initialize PWM at 50Hz
servo_pin = 32; GPIO.setup(servo_pin, GPIO.OUT); pwm = GPIO.PWM(servo_pin, 50)
# Start PWM, set 2% duty cycle (0 degrees), wait 2 seconds
pwm.start(0); pwm.ChangeDutyCycle(2); time.sleep(2) 
# Set 7.5% duty cycle (90 degrees), wait 2 seconds 
pwm.ChangeDutyCycle(7.5); time.sleep(2) 
# Set 12% duty cycle (180 degrees), wait 2 seconds
pwm.ChangeDutyCycle(12); time.sleep(2)  
# Stop PWM and clean up GPIO configurations
pwm.stop(); GPIO.cleanup()  