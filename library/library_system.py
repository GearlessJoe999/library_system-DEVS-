from pypdevs.DEVS import *
from library import Library
from user import User


class LibrarySystem(CoupledDEVS):
    def __init__(self):
        CoupledDEVS.__init__(self, "LibrarySystem")
        self.library = self.addSubModel(Library())
        self.user = self.addSubModel(User())
        self.connectPorts(self.user.out, self.library.interrupt)


### simulation

from pypdevs.simulator import Simulator

sim = Simulator(LibrarySystem())
sim.setVerbose()
sim.setTerminationTime(300)
sim.setClassicDEVS()
sim.simulate()