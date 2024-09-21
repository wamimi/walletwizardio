#!/usr/bin/env python3

import os
import json

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

def clear_screen():
    os.system('clear' if os.name != 'nt' else 'cls')

def save_addresses(addresses):
    with open('wallet_addresses.json', 'w') as f:
        json.dump(addresses, f)

def load_addresses():
    try:
        with open('wallet_addresses.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def copy_to_clipboard(text):
    if CLIPBOARD_AVAILABLE:
        pyperclip.copy(text)
        return True
    return False

def main():
    addresses = load_addresses()
    
    while True:
        clear_screen()
        print("Multi-Wallet Address Copier")
        print("===========================")
        
        if addresses:
            print("Saved wallet addresses:")
            for name, address in addresses.items():
                print(f"- {name}: {address}")
            
            print("\n1. Copy/display a wallet address")
            print("2. Add a new wallet address")
            print("3. Remove a wallet address")
            print("4. Exit")
            
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == '1':
                name = input("Enter the name of the wallet to copy/display: ")
                if name in addresses:
                    print(f"\nWallet address for {name}:")
                    print(addresses[name])
                    if copy_to_clipboard(addresses[name]):
                        print("Address copied to clipboard!")
                    else:
                        print("Please copy the address manually.")
                else:
                    print(f"No wallet found with the name {name}")
                input("Press Enter to continue...")
            elif choice == '2':
                name = input("Enter a name for the new wallet: ")
                address = input("Enter the wallet address: ")
                addresses[name] = address
                save_addresses(addresses)
                print(f"Wallet {name} added successfully.")
                input("Press Enter to continue...")
            elif choice == '3':
                name = input("Enter the name of the wallet to remove: ")
                if name in addresses:
                    del addresses[name]
                    save_addresses(addresses)
                    print(f"Wallet {name} removed successfully.")
                else:
                    print(f"No wallet found with the name {name}")
                input("Press Enter to continue...")
            elif choice == '4':
                break
            else:
                input("Invalid choice. Press Enter to try again...")
        else:
            print("No wallet addresses saved.")
            name = input("Enter a name for your first wallet: ")
            address = input("Enter the wallet address: ")
            addresses[name] = address
            save_addresses(addresses)

    print("Thank you for using Multi-Wallet Address Copier!")

if __name__ == "__main__":
    main()