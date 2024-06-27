import os
import time
from colorama import Fore, init # type: ignore

init()

def caesar(message, shift_val, is_encryption_on):
    result = ""

    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord ('a')
            shifted_char = chr((ord(char) - base + shift_val) % 26 + base)
            result += shifted_char
        else:
            result += char 
    
    if is_encryption_on:
        print(f"{Fore.GREEN}Orignal Message: {message}\n{Fore.CYAN}Encrypted Message: {result}{Fore.RESET}")
    else:
        print(f"{Fore.GREEN}Encrypted Message: {message}\n{Fore.CYAN}Decrypted Message: {result}{Fore.RESET}")

def user_input(mode):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if mode == 'E':
            print("----- ENCRYPTION MODE -----\n")
            mode = True
        else:
            print("----- DECRYPTION MODE -----\n")
            mode = False

        print("Guide:\n\t1. Program will not accept any empty fields/values\n\t2. Shift factor should be <= 26 and >= -26\n\t3. Entering shift factor as zero will not do anything")

        user_input = str(input("\nEnter the text that needs to be encrypted/decrypted: "))
        shift_val = input("Enter the shift factor: ")

        if len(user_input) == 0 or shift_val == "" or int(shift_val) <= -26 or int(shift_val) >= 26:
            print("Kindly enter the possible inputs. Resetting", end="", flush=True)
            for _ in range(5):
                print(".", end="", flush=True)
                time.sleep(0.5)
            break
        else:
            caesar(user_input, int(shift_val), mode)
        
        break

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----- CAESAR CIPHER -----\n")

    print("Guide:\n\t1. Enter E/e for encrypting text\n\t2. Enter D/d for decrypting text\n\t3. Enter 0 to exit the program")
    
    print("\nDo you want to encrypt (E) or decrypt (D) the message?")
    choice = input("E/e for Encryption, D/d for Decryption: ").upper()

    if choice == '0':
        exit(0)
    elif choice == 'E':
        print("Encryption mode is selected.")
        user_input(choice)
    elif choice == 'D':
        user_input(choice)
    else:
        print("Enter a valid choice.")

    input("\nPress any key to continue...")