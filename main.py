from Recorder import record, playback, compress
from ReadableGPIO import ReadableGPIO
from WritableGPIO import WritableGPIO

def main():
    '''
    Example on how to record and playback inputs
    '''
    inputs = [ReadableGPIO(17, pull_up=True)]
    outputs = [WritableGPIO(27, active_high=False)]

    events = record(inputs, outputs=outputs)
    events = compress(events)
    playback(outputs, events)

if __name__ == '__main__':
    main()

