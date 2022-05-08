from states.State import State

class S1(State):
    def run(self, kwargs):
        kwargs = {}
        kwargs['it'] = 0
        print(f"S1")
        self.go_to("S2", kwargs)


class S2(State):
    def run(self, kwargs):
        kwargs['it'] += 1
        self.go_to("S3", kwargs)


class S3(State):
    def run(self, kwargs):
        if kwargs['it'] < 90000:
            self.go_to("S2", kwargs)
        else:
            self.go_to("S4", kwargs)


class S4(State):
    def run(self, kwargs):
        print("S4")
        self.go_to("S1", kwargs)