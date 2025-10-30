import tkinter as tk
from tkinter import messagebox

# --- Morse Code Dictionary ---
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

# --- Core Conversion Logic ---
def text_to_morse(message):
    """
    Converts a text string into its Morse code equivalent.
    """
    morse_code = ""
    for char in message.upper():
        if char == ' ':
            morse_code += " / "
        elif char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + " "
        else:
            # Keep unsupported characters as they are (or skip them)
            # Let's skip them for a cleaner Morse output
            pass
            
    return morse_code.strip()

# --- GUI Functions ---

def handle_conversion():
    """
    Gets text from the input box, converts it, and displays it in the output box.
    """
    # Get text from the input Text widget
    # "1.0" means from the beginning (line 1, char 0)
    # "end-1c" means to the end, minus the 1 trailing newline char
    user_input = input_text.get("1.0", "end-1c")
    
    if not user_input:
        messagebox.showinfo("Empty Input", "Please enter some text to convert.")
        return

    # Perform the conversion
    converted_message = text_to_morse(user_input)
    
    # Update the output Text widget
    # 1. Set state to normal to allow editing
    output_text.config(state="normal")
    # 2. Delete any previous content
    output_text.delete("1.0", "end")
    # 3. Insert the new converted message
    output_text.insert("1.0", converted_message)
    # 4. Set state back to disabled to make it read-only
    output_text.config(state="disabled")

def copy_to_clipboard():
    """
    Copies the content of the output box to the clipboard.
    """
    # Get the text from the output box
    morse_result = output_text.get("1.0", "end-1c")
    if morse_result:
        # Clear the clipboard first
        window.clipboard_clear()
        # Append the new text
        window.clipboard_append(morse_result)
        # Show a confirmation
        messagebox.showinfo("Copied!", "Morse code copied to clipboard.")
    else:
        messagebox.showwarning("Empty Output", "There is no Morse code to copy.")

def clear_fields():
    """
    Clears both the input and output text boxes.
    """
    # Clear the input box
    input_text.delete("1.0", "end")
    
    # Clear the output box
    output_text.config(state="normal")
    output_text.delete("1.0", "end")
    output_text.config(state="disabled")

# --- Set up the main window ---
window = tk.Tk()
window.title("Text-to-Morse Code Converter")
window.geometry("450x400") # Set a reasonable size
window.config(padx=20, pady=20, bg="#f0f0f0") # Add padding and background color

# --- Create and place widgets ---

# 1. Title Label
title_label = tk.Label(
    text="Text to Morse Code", 
    font=("Arial", 18, "bold"), 
    bg="#f0f0f0"
)
title_label.pack(pady=(0, 15))

# 2. Input Label
input_label = tk.Label(
    text="Enter Text:", 
    font=("Arial", 12), 
    bg="#f0f0f0"
)
input_label.pack(anchor="w") # Anchor to the west (left)

# 3. Input Text Box
input_text = tk.Text(
    window, 
    height=5, 
    width=50, 
    font=("Arial", 11),
    borderwidth=2,
    relief="sunken",
    padx=5,
    pady=5
)
input_text.pack(pady=5)

# 4. Button Frame (to hold the buttons side-by-side)
button_frame = tk.Frame(window, bg="#f0f0f0")
button_frame.pack(pady=10)

# 5. Convert Button
convert_button = tk.Button(
    button_frame, 
    text="Convert to Morse", 
    font=("Arial", 10, "bold"),
    command=handle_conversion,
    bg="#4CAF50", # Green
    fg="white",
    padx=10,
    pady=5,
    relief="raised",
    borderwidth=2
)
convert_button.pack(side="left", padx=5)

# 6. Copy Button
copy_button = tk.Button(
    button_frame, 
    text="Copy Result", 
    font=("Arial", 10),
    command=copy_to_clipboard,
    bg="#008CBA", # Blue
    fg="white",
    padx=10,
    pady=5,
    relief="raised",
    borderwidth=2
)
copy_button.pack(side="left", padx=5)

# 7. Clear Button
clear_button = tk.Button(
    button_frame, 
    text="Clear All", 
    font=("Arial", 10),
    command=clear_fields,
    bg="#f44336", # Red
    fg="white",
    padx=10,
    pady=5,
    relief="raised",
    borderwidth=2
)
clear_button.pack(side="left", padx=5)


# 8. Output Label
output_label = tk.Label(
    text="Morse Code Result:", 
    font=("Arial", 12), 
    bg="#f0f0f0"
)
output_label.pack(anchor="w", pady=(10, 0))

# 9. Output Text Box (read-only)
output_text = tk.Text(
    window, 
    height=5, 
    width=50, 
    font=("Arial", 11),
    borderwidth=2,
    relief="sunken",
    padx=5,
    pady=5,
    state="disabled" # Start as read-only
)
output_text.pack(pady=5)

# --- Start the main event loop ---
window.mainloop()
