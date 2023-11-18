# Vscode Installer/Updater for Linux

This Python script automates the process of downloading and installing the Vscode application for Linux systems. It downloads the latest version of Vscode, installs it, resolves any dependencies, and cleans up unnecessary packages and files after installation.

## Prerequisites

Before running this script, ensure you have the following installed:
- Python 3
- `requests` Python module
- `sudo` privileges on your system

## Installation

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:Fredd124/Vscode-Installer-Updater.git
   cd Vscode-Installer-Updater
   ```
2. **Install Python Dependencies**:
   ```bash
   pip install requests
   ```
## Usage   
   Run the script with Python from the terminal:
   ```bash
   sudo python3 vscode_installer_updater.py
   ```
   Note: The script requires sudo privileges to install the Discord .deb package and manage system packages. Make sure to run it in an environment where you have these privileges.
