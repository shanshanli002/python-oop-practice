"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self,start):
        """constructor method and set start variable and initial_value to what the user put in"""
        self.start = start
        self.initial_value = start

    
    def generate(self):
        """method that when called will imcrement and output start """
        print(self.start)
        self.start += 1


    def reset(self):
        """method resets self.start variable to the initial value user put in"""
        self.start = self.initial_value