from gpiozero import DigitalOutputDevice

class WritableGPIO:
    def __init__(self, pin):
        '''
        Creates a writable gpio at `pin`
        '''
        self.device = DigitalOutputDevice(pin)

    def write(self, state):
        '''
        Writes the state to the gpio pin
        '''
        if (state):
            self.device.on()
        else:
            self.device.off()

