from util.Clock import *

class Pymodoro:
    def __init__(self, gui):
        """Create a new pymodoro object, initialising variables"""
        self.num_pomodoros = 0
        self.num_breaks = 0
        self.num_big_breaks = 0
        self.work_clock = Clock(self)
        self.break_clock = Clock(self)
        self.big_break_clock = Clock(self)
        self.is_working = False
        self.is_break = False
        self.is_big_break = False
        self.gui = gui
        self.current_clock = self.work_clock 

    def update_clocks(self):
        """Make the clock tick"""
        if self.is_working:
            self.work_clock.tick()
        elif self.is_break:
            self.break_clock.tick()
        elif self.is_big_break:
            self.big_break_clock.tick()

        return True

    def start_pomodoro(self, widget = None):
        """docstring for start_pomodoro"""
        self.is_working = True
        self.work_clock.reset(20)
        self.current_clock = self.work_clock

    def start_break(self):
        """docstring for start_break"""
        self.is_break = True
        self.break_clock.reset(10)
        self.current_clock = self.break_clock

    def start_extended_break(self):
        """docstring for start_extended_break"""
        self.is_big_break = True
        self.big_break_clock.reset(30)
        self.current_clock = self.big_break_clock

    def clock_expired(self):
        """docstring for clock_expired"""
        if self.is_working:
            self.is_working = False
            self.gui.notify_expiry("Pomodoro complete", "Time for a break!")
            self.num_pomodoros += 1
            print self.num_pomodoros
            if (self.num_pomodoros % 4) != 0:
                self.start_break()
            else:
                self.start_extended_break()
        elif self.is_break:
            self.is_break = False
            self.gui.notify_expiry("Break over", "Time to get back to work!")
            self.start_pomodoro()
        elif self.is_big_break:
            self.is_big_break = False
            self.gui.notify_expiry("Extended break over", "Time to get back to work!")
            self.start_pomodoro()
        return True 
