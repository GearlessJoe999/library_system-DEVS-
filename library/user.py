from pypdevs.DEVS import *


class User(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "User")
        self.out = self.addOutPort("Output")
        self.state = "not_borrowing"
        self.elapsed = 0.0

    def intTransition(self):
        if self.state == "not_borrowing":
            return "borrowing_book"
        elif self.state == "borrowing_book":
            return "not_borrowing"

    def timeAdvance(self):
        if self.state == "not_borrowing":
            return 50
        elif self.state == "borrowing_book":
            return 15

    def outputFnc(self):
        if self.state == "not_borrowing":
            return {self.out: "request"}
        elif self.state == "borrowing_book":
            return {self.out: "return"}
