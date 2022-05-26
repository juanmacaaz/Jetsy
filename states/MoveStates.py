from collections import defaultdict

from states.State import State

"""
    RESET STATE
"""

class Reset(State):
    def run(self, kwargs):
        self.state_machine.global_data['audio'] = 0
        self.state_machine.global_data['video'] = 0
        kwargs = {}
        self.go_to('Default', kwargs)

"""
    DEFAULT STATE
"""
class Default(State):
    next_states = {
        -1: 'Default',
        0: 'Default',
        1: 'InitObject',
        2: 'InitEmotion',
        3: 'InitLeft',
        4: 'InitRight',
        5: 'InitTime',
        6: 'InitHappy',
        7: 'InitSad',
        8: 'InitAngry',
        9: 'InitSurprise',
        10: 'InitWhere',
        11: 'InitRotate',
        12: 'InitTellJoke',
        13: 'InitGo',
        14: 'InitStop',
    }

    def run(self, kwargs):
        #self.state_machine.global_data['audio'] = None
        audio_state = self.state_machine.global_data['audio']
        self.go_to(self.next_states[audio_state], kwargs)

"""
    Detector object sequence
"""

class InitObject(State):
    def run(self, kwargs):
        kwargs = {}
        kwargs['objects_detection'] = []
        print(f"Inicializando sequencia detector de objectos")
        self.go_to("DetectionObject", kwargs)

class DetectionObject(State):
    def run(self, kwargs):
        print(f"Detectando objectos")
        kwargs['objects_detection'].append(self.state_machine.global_data['video'])
        self.go_to("DetectionObject", kwargs)
        if len(kwargs['objects_detection']) > 10:
            self.go_to("FinalDetectionObject", kwargs)

class FinalDetectionObject(State):
    def run(self, kwargs):
        print(f"Finalizando sequencia detector de objectos")
        # Coge el objecto con el sumatorio mas alto
        default_dict = defaultdict(float)
        for obj, conf in kwargs['objects_detection']:
            default_dict[obj] += conf
        kwargs['object'] = max(default_dict, key=default_dict.get)
        print('El objecto detectado es: ', kwargs['object'])
        self.go_to("Reset", kwargs)

'''
    Detector emotion sequence
'''

'''
    Happy sequence
'''

class InitHappy(State):
    def run(self, kwargs):
        print('Estoy feliz')
        self.go_to("S2", kwargs)
        

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