from sched import scheduler
from sys import stderr
from time import monotonic, sleep
from json import dumps

# TODO: Increase reliability of playing back a set of events. This can be done
# by removing redundant events in the event list.
# Possible implementation? if iter.state is iter.next().state, remove iter.next()

def record(inputs, outputs=[], delay=0):
    '''
    Reads the array of inputs until a kill signal is received.

    args:
      inputs: A list of inputs, each should implement a 'read' method.

    kwargs:
      outputs: if specified, each given output will be sourced by its
               associated input. In other words,
               `outputs[i].write(inputs[i].read())`

      delay: the amount of time in seconds between reads of the inputs.

    Returns an array of recordable events.

    Sometimes there are issues playing back events too quickly. This can happen
    when controlling GPIO over a network. One way to avoid this is to increase
    the delay between the event reads.
    '''
    myScheduler = scheduler()
    events = []
    startTime = monotonic()

    def recordAndReschedule():
        '''
        Inner function of record which records the events of all inputs then
        schedules itself
        '''
        inputStates = []
        time = monotonic() - startTime

        for idx, xinput in enumerate(inputs):
            try:
                xinputState = xinput.read()
                inputStates.append(xinputState)
                if (outputs):
                    outputs[idx].write(xinputState)
            except AttributeError:
                stderr.write(f'input at index {idx} does not have method `read`\n')

        events.append({
            "time": time,
            "states": inputStates
        })
        myScheduler.enter(delay, None, recordAndReschedule)

    myScheduler.enter(0, None, recordAndReschedule)

    try:
        stderr.write('Recording...\n')
        myScheduler.run()
    except KeyboardInterrupt:
        list(map(myScheduler.cancel, myScheduler.queue))
        stderr.write('Finished\n')

    return events

def playback(outputs, events):
    '''
    Plays back a set of events

    args:
      outputs: A set of outputs which to play the events back on. The array
      position is important and should correspond to the array position of
      inputs in the events.

      events: A set of events (from `record()`) to play back. It should have
              the following structure:

              ```
              [
                  {
                      time: <time-of-event-in-seconds>,
                      states: [
                          <state-of-output0>,
                          <state-of-output1>,
                          ...
                      ]
                  },
                  ...
              ]
              ```
    '''
    myScheduler = scheduler()

    def playbackEvent(states):
        '''
        An inner function of `playback` which plays back a set of events onto
        `outputs`.
        '''
        for idx, state in enumerate(states):
            outputs[idx].write(True if state else False)

    stderr.write('Preparing playback...\n')
    for event in events:
        myScheduler.enter(event['time'], None, playbackEvent, (event['states'],))

    stderr.write('Playing back events...\n')
    myScheduler.run()
    stderr.write('Finished\n')

