from gpiozero import DigitalOutputDevice

class WritableGPIO:
    def __init__(self, pin, active_high=True):
        '''
        Creates a writable gpio at `pin`
        '''
        self.device = DigitalOutputDevice(pin, active_high=active_high)

    def write(self, state):
        '''
        Writes the state to the gpio pin
        '''
        if (state):
            self.device.on()
        else:
            self.device.off()

