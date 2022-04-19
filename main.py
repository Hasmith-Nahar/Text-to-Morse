morse_code = {

    ' ': '_',

   "'": '.----.',

   '(': '-.--.-',

   ')': '-.--.-',

   ',': '--..--',

   '-': '-....-',

   '.': '.-.-.-',

   '/': '-..-.',

   '0': '-----',

   '1': '.----',

   '2': '..---',

   '3': '...--',

   '4': '....-',

   '5': '.....',

   '6': '-....',

   '7': '--...',

   '8': '---..',

   '9': '----.',

   ':': '---...',

   ';': '-.-.-.',

   '?': '..--..',

   'A': '.-',

   'B': '-...',

   'C': '-.-.',

   'D': '-..',

   'E': '.',

   'F': '..-.',

   'G': '--.',

   'H': '....',

   'I': '..',

   'J': '.---',

   'K': '-.-',

   'L': '.-..',

   'M': '--',

   'N': '-.',

   'O': '---',

   'P': '.--.',

   'Q': '--.-',

   'R': '.-.',

   'S': '...',

   'T': '-',

   'U': '..-',

   'V': '...-',

   'W': '.--',

   'X': '-..-',

   'Y': '-.--',

   'Z': '--..',

   '_': '..--.-'



}



def text_to_morse():

    sentence = input("What is your message? ").upper()

    for i in sentence:

        print(morse_code[i])



text_to_morse()
