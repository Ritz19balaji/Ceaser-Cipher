def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift  # Reverse the shift for decryption
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters unchanged
    
    return result

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Tool")
        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        message = input("Enter the message: ")
        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        mode = 'encrypt' if choice == 'e' else 'decrypt'
        result = caesar_cipher(message, shift, mode)
        print(f"\nResult ({mode}ed text): {result}")
        
        another = input("Do you want to process another message? (y/n): ").strip().lower()
        if another != 'y':
            print("Goodbye!")
            break
