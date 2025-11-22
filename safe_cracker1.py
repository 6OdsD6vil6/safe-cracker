#!/usr/bin/env python3
import random
import time
import sys
import os

# Bank list
BANKS = [
    "Wells Fargo",
    "Bank Of America",
    "Chase",
    "Citi Bank",
    "U.S. Branch Bank",
    "Truist",
    "Capitol One",
    "TD Bank",
    "Citizens Bank",
    "Fifth Third Bank",
    "M&T Bank",
    "Huntington Bank",
    "American Express",
    "KeyBank"
]

def clear_screen():
    """Clear the terminal screen."""
    os.system('clear' if os.name == 'posix' else 'cls')

def typewriter_effect(text, delay=0.03):
    """Simulate typing effect for text."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def flicker_banks():
    """Simulate flickering through banks and selecting one."""
    print("\n[*] Initializing bank breach protocol...")
    time.sleep(1)
    
    # Flickering effect
    for _ in range(20):
        bank = random.choice(BANKS)
        amount = random.randint(1000, 50000)
        sys.stdout.write(f"\r[+] Scanning: {bank} - Balance: ${amount:,}")
        sys.stdout.flush()
        time.sleep(0.1)
    
    # Select a bank
    selected_bank = random.choice(BANKS)
    sys.stdout.write(f"\r[+] TARGET ACQUIRED: {selected_bank} - VULNERABILITY FOUND")
    sys.stdout.flush()
    print("\n")
    
    return selected_bank

def get_user_amount():
    """Get transfer amount from user."""
    while True:
        try:
            amount = input("[+] Enter transfer amount ($1,000 - $9,500): $")
            amount = int(amount.replace(",", ""))
            if 1000 <= amount <= 9500:
                return amount
            else:
                print("[!] Amount must be between $1,000 and $9,500")
        except ValueError:
            print("[!] Invalid amount. Enter numbers only.")

def get_bitcoin_wallet():
    """Get Bitcoin wallet address from user."""
    while True:
        wallet = input("[+] Enter destination Bitcoin wallet: ").strip()
        if wallet and len(wallet) >= 26:  # Basic Bitcoin address validation
            return wallet
        else:
            print("[!] Invalid Bitcoin address format")

def simulate_transfer(amount, wallet, bank):
    """Simulate the transfer process."""
    print("\n[*] Establishing secure connection to bank servers...")
    time.sleep(2)
    
    print("[*] Bypassing firewall...")
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print(" SUCCESS")
    
    print("[*] Exploiting vulnerability in transaction system...")
    time.sleep(1.5)
    
    print("[*] Initiating wire transfer protocol...")
    time.sleep(1)
    
    print(f"\n[+] Transferring ${amount:,} from {bank}")
    print(f"[+] Destination: {wallet}")
    print("\n[*] Processing...")
    
    # Progress bar
    for i in range(101):
        sys.stdout.write(f"\r[{i}%] ")
        sys.stdout.flush()
        time.sleep(0.02)
    
    print("\n\n[+] Transfer complete!")
    print("[+] Funds have been successfully moved to the specified wallet")
    print("[+] Covering tracks and erasing logs...")
    time.sleep(1)
    print("[+] Session terminated")

def main():
    clear_screen()
    
    # ASCII Art Title
    title = """
    ████████╗███████╗ ██████╗██╗  ██╗███████╗████████╗
    ╚══██╔══╝██╔════╝██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝
       ██║   █████╗  ██║     █████╔╝ █████╗     ██║   
       ██║   ██╔══╝  ██║     ██╔═██╗ ██╔══╝     ██║   
       ██║   ███████╗╚██████╗██║  ██╗███████╗   ██║   
       ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   
                                                    
                 C R A C K E R   V1.0
    """
    print(title)
    
    typewriter_effect("[*] System initialized", 0.05)
    typewriter_effect("[*] Connecting to banking network...", 0.05)
    time.sleep(1)
    
    # Main execution
    selected_bank = flicker_banks()
    amount = get_user_amount()
    wallet = get_bitcoin_wallet()
    simulate_transfer(amount, wallet, selected_bank)
    
    print("\n[+] Operation complete. Exiting...")
    time.sleep(2)
    clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[!] Operation aborted by user")
        sys.exit(1)
