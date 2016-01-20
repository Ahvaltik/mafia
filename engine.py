class Engine:
    def __init__(self, system):
        self.system = system

    def start(self):
        while not self.system.finished():
            self.system.step()

    def result(self):
        print str(len(self.system.gangsters)) + "/" + str(len(self.system.agents))
        if len(self.system.gangsters) > 0:
            print "Gang wins"
        else:
            print "Town wins"
