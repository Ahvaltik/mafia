from system import *

class Engine:
    def __init__(self):
        self.gang_wins = 0

    def start(self):
        for i in range(100):
            system = System()
            while not system.finished():
                system.step()
            if system.gang_exists():
                self.gang_wins += 1

    def result(self):
        print "Gang wins " + str(self.gang_wins) + " times"
        print "Town wins " + str(100 - self.gang_wins) + " times"
