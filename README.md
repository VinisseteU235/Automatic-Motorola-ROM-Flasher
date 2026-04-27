# Automatic Motorola ROM Flasher

A Python-based automation tool designed to streamline the process of flashing Stock or Custom ROMs on Motorola devices using ADB and Fastboot.

## 🚀 Features
- **Automated Workflow:** Executes complex terminal commands (wipe, flash partitions) in the correct sequence.
- **Safety First:** Includes basic checks to ensure the device is recognized before starting.
- **Linux Optimized:** Built and tested on Arch Linux, but compatible with most distributions.
- **Time Saving:** Reduces manual input errors and speeds up the flashing process for technicians.

## 🛠️ Prerequisites
- Python 3
- ADB and Fastboot (Android Platform Tools) installed and added to your PATH.
- A Motorola device with an unlocked bootloader.

## 📖 How to Use
1. Clone this repository:
   `git clone https://github.com/VinicinU235/Automatic-Flashing-Motorola-ROM.git`
2. Place your ROM files in the designated folder.
3. Run the script:
   `python flash_script.py`

## ⚠️ Disclaimer
**Use at your own risk.** Flashing firmware can lead to bricked devices if not done correctly. I am not responsible for any damage caused by this script.
