import tkinter as tk
window = tk.Tk()
window.title("NATO Phonetic Translator")
def convert_nato_to_english(nato_input):
    d = {
        'Alpha': 'A', 'Bravo': 'B', 'Charlie': 'C',
        'Delta': 'D', 'Echo': 'E', 'Foxtrot': 'F',
        'Golf': 'G', 'Hotel': 'H', 'India': 'I',
        'Juliett': 'J', 'Kilo': 'K', 'Lima': 'L',
        'Mike': 'M', 'November': 'N', 'Oscar': 'O',
        'Papa': 'P', 'Quebec': 'Q', 'Romeo': 'R',
        'Sierra': 'S', 'Tango': 'T', 'Uniform': 'U',
        'Victor': 'V', 'Whiskey': 'W', 'X-ray': 'X',
        'Yankee': 'Y', 'Zulu': 'Z', ' ': ' ',
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
        'zero': '0', '+': '+', 'minus': '-', 'equals': '=',
        '#': '#', '.': '.', ',': ',', '@': '@',
        'speech-bubble': '"', 'open-square-bracket': '[', 'closed-square-bracket': ']',
        'open-bracket': '(', 'closed-bracket': ')', 'exclamation-point': '!',
        'pound-sign': '£', 'dollar-sign': '$', 'percent-sign': '%',
        'caret': '^', 'and-symbol': '&', 'asterisk': '*', 'underscore': '_',
        'open-curly-square-bracket': '{', 'closed-curly-square-bracket': '}',
        'tilde': '~', 'colon': ':', 'semi-colon': ';', 'straight-line': '|',
        'less-than-sign': '<', 'greater-than-sign': '>', 'forward-slash': '/',
        'question-mark': '?', 'backtick': '`', 'not-sign': '¬', 'apostrophe': "'", 'backslash': '\\',
        'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie',
        'd': 'Delta', 'e': 'Echo', 'f': 'Foxtrot',
        'g': 'Golf', 'h': 'Hotel', 'i': 'India',
        'j': 'Juliett', 'k': 'Kilo', 'l': 'Lima',
        'm': 'Mike', 'n': 'November', 'o': 'Oscar',
        'p': 'Papa', 'q': 'Quebec', 'r': 'Romeo',
        's': 'Sierra', 't': 'Tango', 'u': 'Uniform',
        'v': 'Victor', 'w': 'Whiskey', 'x': 'X-ray',
        'y': 'Yankee', 'z': 'Zulu',
    }

    nato_words = nato_input.split()
    english_output = ' '.join([d.get(word, word) for word in nato_words])
    return english_output

def convert_english_to_nato(english_input):
    d = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie',
        'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
        'G': 'Golf', 'H': 'Hotel', 'I': 'India',
        'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
        'Y': 'Yankee', 'Z': 'Zulu', ' ': ' ',
        '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine',
        '0': 'zero', '+': '+', 'minus': '-', 'equals': '=',
        '#': '#', '.': '.', ',': ',', '@': '@',
        'speech-bubble': '"', 'open-square-bracket': '[', 'closed-square-bracket': ']',
        'open-bracket': '(', 'closed-bracket': ')', 'exclamation-point': '!',
        'pound-sign': '£', 'dollar-sign': '$', 'percent-sign': '%',
        'caret': '^', 'and-symbol': '&', 'asterisk': '*', 'underscore': '_',
        'open-curly-square-bracket': '{', 'closed-curly-square-bracket': '}',
        'tilde': '~', 'colon': ':', 'semi-colon': ';', 'straight-line': '|',
        'less-than-sign': '<', 'greater-than-sign': '>', 'forward-slash': '/',
        'question-mark': '?', 'backtick': '`', 'not-sign': '¬', 'apostrophe': "'", 'backslash': '\\',
    }

    english_input = english_input.upper()
    nato_output = ' '.join([d.get(char, char) for char in english_input])
    return nato_output

def on_translate_click():
    input_text = input_entry.get()
    option = option_var.get()
    if option == "NATO to English":
        result = convert_nato_to_english(input_text)
    else:
        result = convert_english_to_nato(input_text)
    result_label.config(text="Translation: " + result)

def toggle_fullscreen():
    if window.attributes('-fullscreen'):
        window.attributes('-fullscreen', False)
        result_label.config(font=("Arial", 12))
        fullscreen_button.config(text="Full Screen")
    else:
        window.attributes('-fullscreen', True)
        result_label.config(font=("Arial", 24))
        fullscreen_button.config(text="Exit Full Screen")

def exit_app():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("NATO Phonetic Translator")

# Create and configure the GUI elements
input_label = tk.Label(window, text="Enter text:")
input_label.pack()

input_entry = tk.Entry(window)
input_entry.pack()

option_var = tk.StringVar()
option_var.set("English to NATO")

option_menu = tk.OptionMenu(window, option_var, "English to NATO", "NATO to English")
option_menu.pack()

translate_button = tk.Button(window, text="Translate", command=on_translate_click)
translate_button.pack()

result_label = tk.Label(window, text="Translation: ", font=("Arial", 12))
result_label.pack()

fullscreen_button = tk.Button(window, text="Full Screen", command=toggle_fullscreen)
fullscreen_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_app)
exit_button.pack()

# Start the GUI event loop
window.mainloop()