# Multi-Wallet Address Copier

A quick question, how do you copy your wallet address(s)? Whenever you need to paste them somewhere? Personally, I always have to log into metamask or a certain wallet, copy the wallet address, then paste it. Or, if its wriiten somewhere, then i will have to manually copy it from there. Quite a long process if you ask me - Enter walletwizardio, a simple script.

This Python script provides an easy way to store, retrieve, and copy multiple cryptocurrency wallet addresses without the need to log into your wallet applications each time. It's designed for users who manage multiple wallets and want a quick, offline solution for accessing their addresses.

## Features

- Store multiple wallet addresses locally
- Name each wallet for easy identification
- Quickly retrieve any stored wallet address
- Automatically copy addresses to clipboard (if pyperclip is installed)
- Add and remove wallet addresses as needed
- Simple command-line interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Requirements

- Python 3.6 or higher
- (Optional) pyperclip library for clipboard functionality

## Installation

1. Clone this repository or download the `multi_wallet_address_copier.py` file.

git clone <https://github.com/yourusername/multi-wallet-address-copier.git>

cd multi-wallet-address-copier

2. Ensure you have Python 3 installed. You can check your Python version by running:

python3 --version (note this is on Linux)

3. Install pyperclip for clipboard functionality:

pip3 install pyperclip

## Usage

1. Run the script:

python3 multi_wallet_address_copier.py

2. On first run, you'll be prompted to enter a name and address for your first wallet.

3. Use the menu options to:
   - Copy/display a saved wallet address
   - Add a new wallet address
   - Remove a wallet address
   - Exit the program

## How It Works

- The script stores your wallet addresses in a file named `wallet_addresses.json` in the same directory as the script.
- When you run the script, it checks for this file and loads the addresses if it exists.
- You can add, remove, or view addresses at any time using the menu options.
- If pyperclip is installed, the script will automatically copy the selected address to your clipboard. If not, it will display the address for manual copying.

## Security Note

This script stores your wallet addresses in plain text on your local machine. While this is generally safe for most users, please be aware of the following:

- Do not use this script on shared or public computers.
- Ensure your computer has appropriate security measures (password protection, encryption, etc.).
- This script does not store or handle private keys or seed phrases. Never share these with anyone or store them in plain text.

## Contributing

Contributions, issues, and feature requests are welcome!

## License

This project is [MIT] licensed.
