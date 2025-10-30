#!/usr/bin/env python3
"""
Py-Day82 Project: Text to Morse Code Converter (GUI Version)
A GUI-based Python program that converts text strings into Morse code.
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading
import time

# Morse code dictionary mapping letters, numbers, and common punctuation
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}


def text_to_morse(text):
    """
    Convert a text string to Morse code.
    
    Args:
        text (str): The input text to convert
        
    Returns:
        str: The Morse code representation with spaces between letters
             and ' / ' between words
    """
    morse_code = []
    
    for char in text.upper():
        if char == ' ':
            morse_code.append('/')
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            # Skip unsupported characters
            continue
    
    return ' '.join(morse_code)


def morse_to_text(morse):
    """
    Convert Morse code back to text.
    
    Args:
        morse (str): The Morse code string to convert
        
    Returns:
        str: The decoded text
    """
    # Create reverse dictionary
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    
    # Split by ' / ' for words and ' ' for letters
    words = morse.split(' / ')
    decoded_words = []
    
    for word in words:
        letters = word.split(' ')
        decoded_letters = []
        
        for letter in letters:
            if letter in reverse_dict:
                decoded_letters.append(reverse_dict[letter])
        
        decoded_words.append(''.join(decoded_letters))
    
    return ' '.join(decoded_words)


class MorseConverterGUI:
    """GUI class for the Morse Code Converter application."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Morse Code Converter")
        self.root.geometry("800x600")
        self.root.configure(bg='#2c3e50')
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.setup_ui()
        
    def setup_ui(self):
        """Set up the user interface."""
        # Main frame
        main_frame = tk.Frame(self.root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🔊 MORSE CODE CONVERTER 🔊",
            font=('Arial', 20, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Input section
        input_frame = tk.Frame(main_frame, bg='#2c3e50')
        input_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            input_frame,
            text="Enter Text:",
            font=('Arial', 12, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        ).pack(anchor=tk.W)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame,
            height=4,
            font=('Courier', 11),
            bg='#34495e',
            fg='#ecf0f1',
            insertbackground='#ecf0f1'
        )
        self.input_text.pack(fill=tk.X, pady=(5, 0))
        
        # Buttons frame
        button_frame = tk.Frame(main_frame, bg='#2c3e50')
        button_frame.pack(pady=15)
        
        # Convert to Morse button
        self.convert_to_morse_btn = tk.Button(
            button_frame,
            text="Convert to Morse Code",
            command=self.convert_to_morse,
            font=('Arial', 11, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.convert_to_morse_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Convert to Text button
        self.convert_to_text_btn = tk.Button(
            button_frame,
            text="Convert to Text",
            command=self.convert_to_text,
            font=('Arial', 11, 'bold'),
            bg='#e74c3c',
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        self.convert_to_text_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        # Clear button
        clear_btn = tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_all,
            font=('Arial', 11, 'bold'),
            bg='#95a5a6',
            fg='white',
            padx=20,
            pady=8,
            cursor='hand2'
        )
        clear_btn.pack(side=tk.LEFT)
        
        # Output section
        output_frame = tk.Frame(main_frame, bg='#2c3e50')
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
        
        tk.Label(
            output_frame,
            text="Output:",
            font=('Arial', 12, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        ).pack(anchor=tk.W)
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=8,
            font=('Courier', 11),
            bg='#34495e',
            fg='#2ecc71',
            state=tk.DISABLED
        )
        self.output_text.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(
            main_frame,
            textvariable=self.status_var,
            font=('Arial', 9),
            fg='#bdc3c7',
            bg='#2c3e50',
            anchor=tk.W
        )
        status_bar.pack(fill=tk.X, pady=(10, 0))
        
        # Morse code reference
        self.create_reference_window()
        
    def create_reference_window(self):
        """Create a reference window showing the Morse code chart."""
        ref_btn = tk.Button(
            self.root,
            text="Show Morse Code Chart",
            command=self.show_reference,
            font=('Arial', 9),
            bg='#f39c12',
            fg='white',
            cursor='hand2'
        )
        ref_btn.place(relx=1.0, rely=1.0, anchor=tk.SE, x=-10, y=-10)
        
    def show_reference(self):
        """Show the Morse code reference chart."""
        ref_window = tk.Toplevel(self.root)
        ref_window.title("Morse Code Reference")
        ref_window.geometry("400x500")
        ref_window.configure(bg='#2c3e50')
        
        # Create scrollable text widget
        ref_text = scrolledtext.ScrolledText(
            ref_window,
            font=('Courier', 10),
            bg='#34495e',
            fg='#ecf0f1',
            padx=10,
            pady=10
        )
        ref_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add reference content
        ref_content = "MORSE CODE REFERENCE\n" + "="*30 + "\n\n"
        ref_content += "LETTERS:\n" + "-"*20 + "\n"
        
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if char in MORSE_CODE_DICT:
                ref_content += f"{char}: {MORSE_CODE_DICT[char]}\n"
        
        ref_content += "\nNUMBERS:\n" + "-"*20 + "\n"
        for char in "0123456789":
            if char in MORSE_CODE_DICT:
                ref_content += f"{char}: {MORSE_CODE_DICT[char]}\n"
        
        ref_content += "\nPUNCTUATION:\n" + "-"*20 + "\n"
        punctuation = ".,'!?/()&:;=+-_\"$@"
        for char in punctuation:
            if char in MORSE_CODE_DICT:
                ref_content += f"{char}: {MORSE_CODE_DICT[char]}\n"
        
        ref_text.insert(tk.END, ref_content)
        ref_text.config(state=tk.DISABLED)
        
    def convert_to_morse(self):
        """Convert input text to Morse code."""
        input_text = self.input_text.get("1.0", tk.END).strip()
        
        if not input_text:
            messagebox.showwarning("Warning", "Please enter some text to convert!")
            return
        
        self.status_var.set("Converting to Morse code...")
        self.convert_to_morse_btn.config(state=tk.DISABLED)
        
        # Use threading to prevent GUI freezing
        threading.Thread(target=self._convert_to_morse_thread, args=(input_text,)).start()
        
    def _convert_to_morse_thread(self, text):
        """Thread function for Morse code conversion."""
        try:
            morse_result = text_to_morse(text)
            
            # Update GUI in main thread
            self.root.after(0, self._update_output, morse_result, "Text converted to Morse code!")
        except Exception as e:
            self.root.after(0, self._show_error, f"Error converting to Morse: {str(e)}")
        finally:
            self.root.after(0, lambda: self.convert_to_morse_btn.config(state=tk.NORMAL))
    
    def convert_to_text(self):
        """Convert input Morse code to text."""
        input_morse = self.input_text.get("1.0", tk.END).strip()
        
        if not input_morse:
            messagebox.showwarning("Warning", "Please enter some Morse code to convert!")
            return
        
        self.status_var.set("Converting to text...")
        self.convert_to_text_btn.config(state=tk.DISABLED)
        
        # Use threading to prevent GUI freezing
        threading.Thread(target=self._convert_to_text_thread, args=(input_morse,)).start()
        
    def _convert_to_text_thread(self, morse):
        """Thread function for text conversion."""
        try:
            text_result = morse_to_text(morse)
            
            # Update GUI in main thread
            self.root.after(0, self._update_output, text_result, "Morse code converted to text!")
        except Exception as e:
            self.root.after(0, self._show_error, f"Error converting to text: {str(e)}")
        finally:
            self.root.after(0, lambda: self.convert_to_text_btn.config(state=tk.NORMAL))
    
    def _update_output(self, result, status_message):
        """Update the output text widget."""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert("1.0", result)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set(status_message)
        
    def _show_error(self, error_message):
        """Show error message."""
        messagebox.showerror("Error", error_message)
        self.status_var.set("Error occurred")
        
    def clear_all(self):
        """Clear all text fields."""
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status_var.set("Cleared all fields")


def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    app = MorseConverterGUI(root)
    
    # Center the window on screen
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (root.winfo_width() // 2)
    y = (root.winfo_screenheight() // 2) - (root.winfo_height() // 2)
    root.geometry(f"+{x}+{y}")
    
    # Start the GUI event loop
    root.mainloop()


if __name__ == "__main__":
    main()