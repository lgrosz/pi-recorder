from Recorder import record, playback
from ReadableGPIO import ReadableGPIO
from WritableGPIO import WritableGPIO
from gpiozero import GPIODevice
from json import dumps

def main():
    '''
    Example on how to record and playback inputs
    '''
    inputs = [ReadableGPIO(17, pullup=True)]
    outputs = [WritableGPIO(27)]

    events = record(inputs, outputs=outputs)
    playback(outputs, events)

if __name__ == '__main__':
    main()

