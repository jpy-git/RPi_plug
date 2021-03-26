from RPi_plug import RPi_plug
import time

class MorseCode:

    morse_code_dict = { 
        'A':'.-', 
        'B':'-...',
        'C':'-.-.', 
        'D':'-..', 
        'E':'.',
        'F':'..-.', 
        'G':'--.', 
        'H':'....',
        'I':'..', 
        'J':'.---', 
        'K':'-.-',
        'L':'.-..', 
        'M':'--', 
        'N':'-.',
        'O':'---', 
        'P':'.--.', 
        'Q':'--.-',
        'R':'.-.', 
        'S':'...', 
        'T':'-',
        'U':'..-', 
        'V':'...-', 
        'W':'.--',
        'X':'-..-', 
        'Y':'-.--', 
        'Z':'--..',
        '1':'.----', 
        '2':'..---', 
        '3':'...--',
        '4':'....-', 
        '5':'.....', 
        '6':'-....',
        '7':'--...', 
        '8':'---..', 
        '9':'----.',
        '0':'-----', 
        ',':'--..--', 
        '.':'.-.-.-',
        '?':'..--..', 
        '/':'-..-.', 
        '-':'-....-',
        '(':'-.--.', 
        ')':'-.--.-',
        ' ': '_'
    }

    def __init__(self, text, plug):
        
        if isinstance(text, str):
            self._text = text
        else:
            raise TypeError("text must be a string")

        self._plug = plug

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text):

        if isinstance(new_text, str):
            self._text = new_text
        else:
            raise TypeError("new_text must be a string")

    def text_to_morse(self):
        
        input_string_list = list(self._text.upper())
        morse_string = "_".join([self.morse_code_dict[char] for char in input_string_list if char in self.morse_code_dict])

        return morse_string

    def _dot(self):
        self._plug.socket_on()
        time.sleep(0.3)
        self._plug.socket_off()
        time.sleep(0.2)


    def _dash(self):
        self._plug.socket_on()
        time.sleep(0.8)
        self._plug.socket_off()
        time.sleep(0.2)

    def _space(self):
        time.sleep(0.8)

    def light_morse(self):
        
        for char in self.text_to_morse():

            if char == ".":
                self._dot()
            elif char == "-":
                self._dash()
            else:
                self._space()

if __name__ == "__main__":

    plug = RPi_plug()

    try:
        morse = MorseCode(
            text = input("Please input text: "),
            plug = plug
        )

        print(
            f"""
            Text: {morse.text}
            Morse Code: {morse.text_to_morse()}
            """
        )

        morse.light_morse()

    
    finally:
        plug.cleanup()



