from pypdevs.DEVS import *
from pypdevs.infinity import INFINITY


class Library(AtomicDEVS):
    def __init__(self):
        AtomicDEVS.__init__(self, "library")
        self.state = "book_on_shelf"
        self.elapsed = 0.0
        self.observe = self.addOutPort("observer")
        self.interrupt = self.addInPort("interrupt")

    def intTransition(self):
        state = self.state
        return {"book_on_shelf": "Loaned",
                "Loaned": "due",
                "due": "Compute_fine",
                "Compute_fine": "book_on_shelf"}[state]

    def timeAdvance(self):
        state = self.state
        return {"book_on_shelf": INFINITY,
                "Loaned": 10,
                "due": INFINITY,
                "Compute_fine": 1}[state]

    def outputFnc(self):
        state = self.state
        if state == "due":
            return {self.observe: "warning"}
        elif state == "Compute_fine":
            return {self.observe: "fine"}
        elif state == "book_on_shelf":
            return {self.observe: "Loaned"}
        elif state == "Loaned":
            return {self.observe: "due"}

    def extTransition(self, inputs):
        inp = inputs[self.interrupt]
        if inp == "request":
            if self.state == "book_on_shelf":
                return "Loaned"
        elif inp == "return":
            if self.state == "Loaned":
                return "book_on_shelf"
            elif self.state == "due":
                return "Compute_fine"


### Experiment
from pypdevs.simulator import Simulator

model = Library()
sim = Simulator(model)

sim.setVerbose()
sim.setTerminationTime(1000)
sim.setClassicDEVS()
sim.simulate()
