class State:
    def __init__(self, state_machine):
        self.name = self.__class__.__name__
        self.state_machine = state_machine

    def __str__(self):
        return self.name

    def go_to(self, state, kwargs):
        self.state_machine.kwargs = kwargs
        self.state_machine.state = state

    def run(self, kwargs): pass