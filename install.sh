# nano install.sh
# Author: SAAD IQBAL CHAUHAN
# Email: saadchavhan2@gmail.com
# Organization: PBR RESEARCH AMRAVATI
# Website: https://pbrresearch.com/
# Date: April 22, 2025 Updated :- 29/04/25

# Description:
# This script automates the setup of a Python virtual environment and the installation
# of the RPLCD library for controlling an I2C LCD display (e.g., 16x2 with PCF8574 backpack)
# on a Raspberry Pi. It installs required tools, creates a virtual environment in ~/Demo/venv,
# installs RPLCD and its dependencies (e.g., smbus2), and provides instructions for running
# a Python script (lcd.py). The script is designed for new users and includes error
# handling and user feedback.

# Exit on any error
set -e

echo "Starting RPLCD setup for I2C LCD on Raspberry Pi..."

# Step 1: Update system and install required tools
echo "Updating package list and installing python3-venv, python3-full..."
sudo apt update
sudo apt install -y python3 python3-venv
echo "Tools installed successfully."
sleep 0.5
# Step 2: Create a virtual environment
# Navigate to ~/Demo, create if it doesn't exist
echo "Creating project directory ~/Demo..."
mkdir -p ~/Demo
cd ~/Demo
echo "Creating virtual environment in ~/Demo/venv..."
python3 -m venv venv
echo "Virtual environment created."
sleep 0.5
# Step 3: Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
echo "Virtual environment activated. Prompt should show '(venv)'."
sleep 0.5
# Step 4: Install RPLCD
echo "Installing RPLCD library..."
pip install --upgrade pip
pip install RPLCD
echo "RPLCD installed."
sleep 0.5
# Step 5: Verify RPLCD installation
echo "Verifying RPLCD installation..."
pip show RPLCD
pip install smbus2
echo "If you see version (e.g., 1.3.1) and path (~/Demo/venv/lib/python3.X/site-packages), installation is successful."
sleep 0.5
echo " NOW YOU CAN RUN THE SCRIPT "
