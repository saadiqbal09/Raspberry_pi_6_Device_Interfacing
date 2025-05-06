"""
Description:
    This script controls a 16x2 LCD display via I2C on a Raspberry Pi 4.
    It displays the author's name and project details using the RPLCD library.
    The LCD is connected via a PCF8574 expander at I2C address 0x27.

Author Information:
    Developer: SAAD IQBAL CHAUHAN
    Email: saadchavhan2@gmail.com
    Organization: PBR RESEARCH AMRAVATI
    Website: https://pbrresearch.com/
"""
from RPLCD.i2c import CharLCD
import time
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)
lcd.clear()
lcd.write_string("PBR Research")
lcd.cursor_pos = (1, 0); lcd.write_string("RPI PROJECT"); time.sleep(5)