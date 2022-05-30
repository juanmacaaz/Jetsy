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


    # Audio
    def get_audio_data(self):
        data = self.state_machine.global_data['audio']
        self.state_machine.global_data['audio'] = None
        return data

    def reset_audio_data(self):
        self.state_machine.global_data['audio'] = None

    # Voice

    def reproduce_msg(self, text):
        self.state_machine.global_data['voice'] = text

    def end_msg(self):
        return self.state_machine.global_data['voice'] == None

    # Sensors

    # Video

    def detecta_cara(self):
        return self.state_machine.global_data['face']