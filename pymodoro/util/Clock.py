from notify.all import *

class Clock(object):
    def __init__(self, pymodoro):
        """Create a new clock"""
        self.time = 0
        self.expire = Signal()
        self.expire.connect(pymodoro.clock_expired)
        self.pymodoro = pymodoro

    def reset(self, start_time):
        """Set the clock to start_time."""
        self.time = start_time

    def tick(self):
        """Tick the clock"""
        self.time -= 1
        if self.time == 0:
            self.expire()
