from gpiozero import InputDevice

class ReadableGPIO:
    def __init__(self, pin, pullup=False):
        '''
        Creates a recordable gpio at `pin`
        '''
        self.device = InputDevice(pin, pull_up=pullup)

    def read(self):
        '''
        Reads the and returns the state of the device as string
        '''
        return self.device.value

