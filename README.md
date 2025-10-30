# Py-Day82 Project: Text to Morse Code Converter (GUI)

A modern GUI-based Python program that converts strings into Morse code and vice versa using tkinter.

## Features

- **Modern GUI Interface** - Clean, dark-themed user interface
- **Bidirectional Conversion** - Convert text to Morse code and vice versa
- **Real-time Processing** - Instant conversion with threading support
- **Morse Code Reference** - Built-in reference chart window
- **Full Character Support** - Letters (A-Z), numbers (0-9), and common punctuation
- **Error Handling** - User-friendly error messages and validation
- **Copy-Paste Friendly** - Large text areas for easy input/output

## Files

- `morse_converter.py` - Main GUI application

## Usage

Run the GUI application:
```bash
python morse_converter.py
```

## GUI Features

- **Input Area** - Large text box for entering text or Morse code
- **Convert Buttons** - Separate buttons for text-to-Morse and Morse-to-text conversion
- **Output Display** - Scrollable output area with syntax highlighting
- **Clear Function** - One-click clear all fields
- **Reference Chart** - Pop-up window showing complete Morse code reference
- **Status Bar** - Real-time status updates

## Morse Code Format

- Letters and numbers are separated by spaces
- Words are separated by ` / `
- Dots (.) and dashes (-) represent the Morse code signals

## Examples

```
Text: HELLO WORLD
Morse: .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Text: SOS
Morse: ... --- ...

Text: PYTHON
Morse: .--. -.-- - .... --- -.
```

## Supported Characters

- All letters A-Z
- All digits 0-9
- Common punctuation: . , ? ' ! / ( ) & : ; = + - _ " $ @
