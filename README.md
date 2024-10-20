# Multi-Wallet Address Copier

A quick and easy way to manage and copy your cryptocurrency wallet addresses from the command line or a simple GUI.

This Python script provides an easy way to store, retrieve, and copy multiple cryptocurrency wallet addresses without the need to log into your wallet applications each time. It's designed for users who manage multiple wallets and want a quick, offline solution for accessing their addresses.

## Features

- Store multiple wallet addresses locally
- Name each wallet for easy identification
- Quickly retrieve any stored wallet address
- Automatically copy addresses to clipboard (if pyperclip is installed)
- Add and remove wallet addresses as needed
- Simple command-line interface
- Basic GUI for easier access
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- pyperclip library for clipboard functionality
- tkinter for GUI functionality (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the `multi_wallet_address_copier.py` and `metamask_gui.py` files.

git clone <https://github.com/wamimi/walletwizardio.git>

cd walletwizardio

2. Ensure you have Python 3 installed. 

   - Linux/macOS:
     ```
     python3 --version
     ```
   - Windows:
     ```
     python --version
     ```

3. Install required libraries:

   - Linux/macOS:
     ```
     pip3 install pyperclip
     ```
   - Windows:
     ```
     pip install pyperclip
     ```

4. If tkinter is not installed (mainly for Linux users):

   - Ubuntu/Debian:
     ```
     sudo apt-get install python3-tk
     ```
   - Fedora:
     ```
     sudo dnf install python3-tkinter
     ```

## Usage

### Command Line Interface

1. Run the script:

   - Linux/macOS:
     ```
     python3 metamask_address_copier.py
     ```
   - Windows:
     ```
     python metamask_address_copier.py
     ```

2. On first run, you'll be prompted to enter a name and address for your first wallet.

3. Use the menu options to:
   - Copy/display a saved wallet address
   - Add a new wallet address
   - Remove a wallet address
   - Exit the program

### Graphical User Interface

1. Run the GUI script:

   - Linux/macOS:
     ```
     python3 metamask_gui.py
     ```
   - Windows:
     ```
     python metamask_gui.py
     ```

2. A window will appear with a button labeled "Run MetaMask Address Copier".

3. Click the button to launch the wallet address copier program.

4. The program will open in a new window, allowing you to interact with it as described in the Command Line Interface section.

## How It Works

- The script stores your wallet addresses in a file named `wallet_addresses.json` in the same directory as the script.
- When you run the script, it checks for this file and loads the addresses if it exists.
- You can add, remove, or view addresses at any time using the menu options.
- If pyperclip is installed, the script will automatically copy the selected address to your clipboard. If not, it will display the address for manual copying.
- The GUI provides a simple interface to launch the main program without needing to use the command line.

## Security Note

This script stores your wallet addresses in plain text on your local machine. While this is generally safe for most users, please be aware of the following:

- Do not use this script on shared or public computers.
- Ensure your computer has appropriate security measures (password protection, encryption, etc.).
- This script does not store or handle private keys or seed phrases. Never share these with anyone or store them in plain text.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

This project is [MIT] licensed.

