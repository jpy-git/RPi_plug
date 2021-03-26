import RPi.GPIO as GPIO
import time

class RPi_plug:
    """Class to connect to and control Energenie Remote Control Sockets via Raspberry Pi
    """

    # Set encoder mappings for plugs 1, 2, 3, 4, & -1 (all)
    _encoder_dict = {
        -1: [False, True, True], 
        1: [True, True, True], 
        2: [True, True, False], 
        3: [True, False, True], 
        4: [True, False, False]
    }

    def __init__(self):
        """Create instance of RPi_plug
        """
        
        # Use board numbering
        GPIO.setmode(GPIO.BOARD)

        # Select GPIO pins used for D0-D3 encoder inputs
        GPIO.setup(13, GPIO.OUT) # D3
        GPIO.setup(16, GPIO.OUT) # D2
        GPIO.setup(15, GPIO.OUT) # D1
        GPIO.setup(11, GPIO.OUT) # D0
        
        # Select GPIO pin for OOK (On-Off-Keying)
        GPIO.setup(18, GPIO.OUT)

        # Set MODSEL GPIO pin low to enable OOK
        GPIO.output(18, False)

        # Select GPIO pin to enable/disable modulator
        GPIO.setup(22, GPIO.OUT)

        # Set CE GPIO pin low to disable modulator
        GPIO.output(22, False)

        # Initialise D0-D3 inputs
        GPIO.output(13, False)
        GPIO.output(16, False)
        GPIO.output(15, False)
        GPIO.output(11, False)

    def _modulator(self):
        """Send modulator signal to trigger plug
        """

        # Allow encoder to settle
        time.sleep(0.1)

        # Enable modulator
        GPIO.output(22, True)

        # Wait for signal transmission
        time.sleep(0.25)

        # Disable modulator
        GPIO.output(22, False)

    def on(self, socket_num=None):
        """Function to turn on a specified plug

        Parameters
        ----------
        socket_num : int or None, optional
            integer representing plug to turn on, by default None
        """
        
        # Validate inputs
        if socket_num:
            if not isinstance(socket_num, int):
                raise TypeError("socket_num must be an integer")
        
            if socket_num not in [1, 2, 3, 4]:
                raise ValueError("socket_num must be in range [1, 2, 3, 4]")

        # Enable selected encoder pins
        if not socket_num:
            GPIO.output(13, True)
            GPIO.output(16, self._encoder_dict[-1][0])
            GPIO.output(15, self._encoder_dict[-1][1])
            GPIO.output(11, self._encoder_dict[-1][2])
            self._modulator()
        else:
            GPIO.output(13, True)
            GPIO.output(16, self._encoder_dict[socket_num][0])
            GPIO.output(15, self._encoder_dict[socket_num][1])
            GPIO.output(11, self._encoder_dict[socket_num][2])
            self._modulator()


    def off(self, socket_num=None):
        """Function to turn off a specified plug

        Parameters
        ----------
        socket_num : int or None, optional
            integer representing plug to turn off, by default None
        """

        # Validate inputs
        if socket_num:
            if not isinstance(socket_num, int):
                raise TypeError("socket_num must be an integer")
        
            if socket_num not in [1, 2, 3, 4]:
                raise ValueError("socket_num must be in range [1, 2, 3, 4]")

        # Enable selected encoder pins
        if not socket_num:
            GPIO.output(13, False)
            GPIO.output(16, self._encoder_dict[-1][0])
            GPIO.output(15, self._encoder_dict[-1][1])
            GPIO.output(11, self._encoder_dict[-1][2])
            self._modulator()
        else:
            GPIO.output(13, False)
            GPIO.output(16, self._encoder_dict[socket_num][0])
            GPIO.output(15, self._encoder_dict[socket_num][1])
            GPIO.output(11, self._encoder_dict[socket_num][2])
            self._modulator()

    def cleanup(self):
        """Clean up GPIO pins
        """
        
        # Clean up GPIO pins
        GPIO.cleanup()


if __name__ == "__main__":
    
    plug = RPi_plug()
    plug.on()
    time.sleep(10)
    plug.off()
    plug.cleanup()