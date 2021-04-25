from RPi_plug import RPi_plug
import time

class MorseCode:
    """Class to convert text to Morse code and display on remote lamp
    """

    # Dictionary to map text character to Morse code
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
        """function to initialise MorseCode class

        Parameters
        ----------
        text : str
            string inputted by user
        plug : object
            instance of RPi_plug class
        """

        if isinstance(text, str):
            self._text = text
        else:
            raise TypeError("text must be a string")

        self._plug = plug

    @property
    def text(self):
        """Getter for text attribute

        Returns
        -------
        str
            string inputted by user
        """

        return self._text

    @text.setter
    def text(self, new_text):
        """Setter for text attribute

        Parameters
        ----------
        new_text : str
            string inputted by user
        """

        if isinstance(new_text, str):
            self._text = new_text
        else:
            raise TypeError("new_text must be a string")

    def text_to_morse(self):
        """Covert text to Morse code string

        Returns
        -------
        str
            Morse code string consisting of dots (.), dashes (-), & spaces (_)
        """
        
        input_string_list = list(self._text.upper())
        morse_string = "_".join([self.morse_code_dict[char] for char in input_string_list if char in self.morse_code_dict])

        return morse_string

    def _dot(self):
        """Short pulse representing Morse code dot (.)
        """

        self._plug.on()
        time.sleep(0.4)
        self._plug.off()
        time.sleep(0.3)


    def _dash(self):
        """Long pulse representing Morse code dash (-)
        """

        self._plug.on()
        time.sleep(0.8)
        self._plug.off()
        time.sleep(0.3)

    def _space(self):
        """Delay for spaces in Morse code
        """

        time.sleep(1)

    def light_morse(self):
        """Convert Morse code string to light pulses on remote lamp
        """
        
        for char in self.text_to_morse():

            if char == ".":
                self._dot()
            elif char == "-":
                self._dash()
            else:
                self._space()

def main():
    """Main function for morse_code_light.py
    """

    # Create RPi_plug instance
    plug = RPi_plug()

    try:
        # Request user input text and convert to morse code
        morse = MorseCode(
            text = input("Please input text: "),
            plug = plug
        )

        # Print inputted text and translated Morse code
        print(
            f"""
            Text: {morse.text}
            Morse Code: {morse.text_to_morse()}
            """
        )

        # Display Morse code light pulses
        morse.light_morse()

    finally:
        # Clean up GPIO pins
        plug.cleanup()

if __name__ == "__main__":

    # Initiate main function
    main()


    