Write a class named Signal with the following specification:

Attributes

(1) state: string, either "red" or "green"; represents the current state of the signal
(2) v: int, represents the vehicle density at the current instant
(3) T: int, threshold for the vehicle density

Methods

self is the first argument of all methods. We will only mention additional arguments, if any.
(1) __init__: constructor; accepts the threshold T as argument; initially the signal is red and the vehicle density is 0.
(2) sense: accept the vehicle density as argument and update the corresponding attribute; assume that this information comes from a sensor.
(3) update: update the state of the signal-attribute depending on the current values of the attributes.



class Signal:
    def __init__(self, T):
        self.state = 'red'
        self.v = 0
        self.T = T

    def sense(self, v):
        self.v = v

    def update(self):
        if self.v >= self.T:
            if self.state == 'red':
                self.state = 'green'
        else:
            if self.state == 'green':
                self.state = 'red'