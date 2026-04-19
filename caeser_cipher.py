def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using Caesar Cipher algorithm.
    
    Args:
        text (str): The text to encrypt/decrypt
        shift (int): The number of positions to shift
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    # Input validation
    if not isinstance(text, str):
        raise ValueError("Text must be a string")
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer")
    if mode not in ['encrypt', 'decrypt']:
        raise ValueError("Mode must be either 'encrypt' or 'decrypt'")
    
    result = ""
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Calculate the new position
            new_pos = (ord(char) - base + shift) % 26
            # Convert back to character
            result += chr(base + new_pos)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def get_valid_shift():
    """Get a valid shift value from the user."""
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            print("Shift value must be between 1 and 25.")
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_text():
    """Get a valid text input from the user."""
    while True:
        text = input("Enter the text: ").strip()
        if text:
            return text
        print("Text cannot be empty. Please try again.")

def main():
    print("Caesar Cipher Program")
    print("--------------------")
    
    while True:
        try:
            print("\n1. Encrypt")
            print("2. Decrypt")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '3':
                print("Goodbye!")
                break
                
            if choice not in ['1', '2']:
                print("Invalid choice. Please try again.")
                continue
                
            text = get_valid_text()
            shift = get_valid_shift()
            
            mode = 'encrypt' if choice == '1' else 'decrypt'
            result = caesar_cipher(text, shift, mode)
            
            print(f"\n{mode.capitalize()}ed text: {result}")
            
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try again.")

if __name__ == "__main__":
    main() 
