# What this is
This project is a flexible interface to record and playback events. It contains
a simple example utilizing Raspberry Pi GPIOs, but it should work for pretty
much anything which can read and write state.

# Run on Raspberry Pi

Unix Shell via Python 3.8+ on Raspberry Pi
```
python3 main.py
```

Unix Shell via Python 3.8+ on network connected host
```
PIGPIO_ADDR=<ipv4-address-of-rpio> python3 main.py
```

