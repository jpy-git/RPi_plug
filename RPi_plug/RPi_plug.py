import RPi.GPIO as GPIO
import time

class RPi_plug:

    def __init__(self):
        
        # Use board numbering
        GPIO.setmode(GPIO.BOARD)

        # Select the GPIO pins used for the encoder K0-K3 data inputs
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(11, GPIO.OUT)
        
        # Select the signal to select ASK/FSK
        GPIO.setup(18, GPIO.OUT)

        # Select the signal used to enable/disable the modulator
        GPIO.setup(22, GPIO.OUT)

        # Disable the modulator by setting CE pin low
        GPIO.output(22, False)

        # Set the modulator to ASK for On Off Keying 
        # by setting MODSEL pin low
        GPIO.output(18, False)

        # Initialise K0-K3 inputs of the encoder to 0000
        GPIO.output(13, False)
        GPIO.output(16, False)
        GPIO.output(15, False)
        GPIO.output(11, False)

    def _modulator(self):

        # Let encoder settle
        time.sleep(0.1)
        # Enable modulator
        GPIO.output(22, True)
        # Wait
        time.sleep(0.25)
        # Disable modulator
        GPIO.output(22, False)

    def socket_on(self, socket_num=None):
        
        # Validate inputs
        if socket_num:
            if not isinstance(socket_num, int):
                raise TypeError("socket_num must be an integer")
        
            if socket_num not in [1, 2, 3, 4]:
                raise ValueError("socket_num must be in range [1, 2, 3, 4]")

        # If socket_num == None then turn on all plugs (1011)
        if not socket_num:
            GPIO.output(13, True)
            GPIO.output(16, False)
            GPIO.output(15, True)
            GPIO.output(11, True)
            self._modulator()

    def socket_off(self, socket_num=None):
        
        # Validate inputs
        if socket_num:
            if not isinstance(socket_num, int):
                raise TypeError("socket_num must be an integer")
        
            if socket_num not in [1, 2, 3, 4]:
                raise ValueError("socket_num must be in range [1, 2, 3, 4]")

        # If socket_num == None then turn off all plugs (0011)
        if not socket_num:
            GPIO.output(13, False)
            GPIO.output(16, False)
            GPIO.output(15, True)
            GPIO.output(11, True)
            self._modulator()

    def cleanup(self):
        GPIO.cleanup()


if __name__ == "__main__":
    plug = RPi_plug()
    plug.socket_on()
    time.sleep(10)
    plug.socket_off()
    plug.cleanup()


