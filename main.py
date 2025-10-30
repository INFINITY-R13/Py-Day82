# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '!': '-.-.--', '@': '.--.-.', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', "'": '.----.'
}

def text_to_morse(message):
    """
    Converts a text string into its Morse code equivalent.
    
    Args:
        message (str): The text string to be converted.

    Returns:
        str: The Morse code representation of the input string.
              Letters are separated by a single space.
              Words are separated by ' / '.
              Unsupported characters are skipped.
    """
    morse_code = ""
    # Convert the message to uppercase as Morse code is case-insensitive
    for char in message.upper():
        if char == ' ':
            # Add a word separator
            # We add a space before and after '/' to distinguish it from letter spaces
            morse_code += " / "
        elif char in MORSE_CODE_DICT:
            # Add the Morse code for the character, followed by a space
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            # You can choose to handle unsupported characters differently,
            # e.g., morse_code += '? '
            # For this version, we'll just skip them.
            pass
            
    # .strip() removes any trailing space from the end
    return morse_code.strip()

def main():
    """
    Main function to run the Morse Code Converter program.
    """
    print("--- Text to Morse Code Converter ---")
    print("Enter your message, and I will convert it to Morse code.")
    print("Words are separated by ' / ' and letters by a single space.")
    print("--------------------------------------\n")

    is_running = True
    while is_running:
        # Get user input
        user_input = input("Enter your message: ")
        
        if not user_input:
            print("You didn't enter anything. Please try again.")
            continue
            
        # Perform the conversion
        converted_message = text_to_morse(user_input)
        
        # Display the result
        print(f"\nYour message: {user_input}")
        print(f"Morse Code:   {converted_message}\n")
        
        # Ask to continue
        while True:
            choice = input("Would you like to convert another message? (yes/no): ").strip().lower()
            if choice == 'no' or choice == 'n':
                is_running = False
                break
            elif choice == 'yes' or choice == 'y':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    print("\nThank you for using the Morse Code Converter. Goodbye!")

# Run the main program
if __name__ == "__main__":
    main()
