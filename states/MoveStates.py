from collections import defaultdict

from numpy import append
from VoiceModule.VoiceModule import voice_module
from states.State import State

from Drivers import motion
import random

"""
    RESET STATE
"""

class Reset(State):
    def run(self, kwargs):
        self.state_machine.global_data['audio'] = 0
        self.state_machine.global_data['video'] = 0
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
        3: 'InitRepite',
        4: 'InitJoke',
        5: 'InitWhereAmI'
    }

    def run(self, kwargs):
        #self.state_machine.global_data['audio'] = None
        audio_state = self.state_machine.global_data['audio']
        kwargs = {}
        self.go_to(self.next_states[audio_state], kwargs)

"""
    Detector object sequence
"""

class InitObject(State):
    def run(self, kwargs):
        kwargs = {}
        kwargs['objects_detection'] = []
        print(f"Inicializando sequencia detector de objectos")
        kwargs['next_state'] = 'DetectionObject'
        kwargs['voice'] = 'Initializing object detector sequence'
        self.go_to("DecirFrase", kwargs)
        

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
        kwargs['next_state'] = 'Reset'
        kwargs['voice'] = 'The detected object is: ' + str(kwargs['object'])
        self.go_to("DecirFrase", kwargs)

'''
    Detector emotion sequence
'''
class InitEmotion(State):
    def run(self, kwargs):
        kwargs = {}
        print(f"Inicializando sequencia detectora de emociones")
        kwargs['next_state'] = 'DetectionEmotion'
        kwargs['voice'] = 'Initializing emotion detector sequence'
        self.go_to("DecirFrase", kwargs)
    
class DetectionEmotion(State):
    def run(self, kwargs):
        print(f"Detectando emociones")
        kwargs['emotion_detection'] = self.state_machine.global_data['emotion']
        self.go_to("DetectionEmotion", kwargs)
        if kwargs['emotion_detection'] != None:
            self.go_to("FinalDetectionEmotion", kwargs)
class FinalDetectionEmotion(State):
    def run(self, kwargs):
        print(f"Finalizando sequencia detectora de emociones")
        print('El objecto detectado es: ', kwargs['emotion_detection'])
        kwargs['next_state'] = 'Reset'
        kwargs['voice'] = 'The detected emotion is: ' + str(kwargs['emotion_detection'])
        self.go_to("DecirFrase", kwargs)
'''
    Dance sequence
'''

class InitDance(State):
    def run(self, kwargs):
        kwargs = {}
        kwargs['i'] = 0
        print(f"Inicializando sequencia detector de objectos")
        self.go_to("DetectionObject", kwargs)

class LevantaBrazoDerecho(State):
    def run(self, kwargs):
        motion.moverBrazo(True, False, 180)
        kwargs['i'] += 1
        if kwargs['i'] == 30:
            kwargs['i'] == 0
            self.go_to("DetectionObject", kwargs)
        self.go_to("LevantaBrazoDerecho", kwargs)

class LevantaBrazoIzquierdo(State):
    def run(self, kwargs):
        motion.moverBrazo(True, False, 180)
        kwargs['i'] += 1
        if kwargs['i'] == 30:
            kwargs['i'] == 0
            self.go_to("DetectionObject", kwargs)

        self.go_to("DetectionObject", kwargs)

class LevantaBrazoDerecho(State):
    def run(self, kwargs):
        motion.moverBrazo(True, False, 180)
        kwargs['i'] += 1
        if kwargs['i'] == 30:
            kwargs['i'] == 0
            self.go_to("DetectionObject", kwargs)
        self.go_to("DetectionObject", kwargs)

'''
    Repite Conmigo Sequencia
'''

class InitRepite(State):
    def run(self, kwargs):
        kwargs['sequencia'] = []
        kwargs['map'] = {
            20: ("RepiteDerecha", 20),
            21: ("RepiteIzquierda", 20),
            22: ("RepiteAdelante", 20),
            23: ("RepiteAtras", 20),
            24: ("RepiteBrazoIzquierdoArriba", 20),
            25: ("RepiteBrazoDerechoArriba", 20),
            26: ("RepiteBrazoIzquierdoAbajo", 20),
            27: ("RepiteBrazoDerechoAbajo", 20)
        }
        kwargs['next_state'] = 'EntradaVoz'
        kwargs['voice'] = 'No me puedo creer que no se separasen después de esa mierda, hhhh mis dos nalgas'
        self.go_to("DecirFrase", kwargs)

class DecirFrase(State):
    def run(self, kwargs):
        self.reproduce_msg(kwargs['voice'])
        self.go_to('EsperarFrase', kwargs)

class EsperarFrase(State):
    def run(self, kwargs):
        print(kwargs['voice'])
        if self.end_msg():
            del kwargs['voice']
            self.go_to(kwargs['next_state'], kwargs)
            del kwargs['next_state']
        else:
            self.go_to('EsperarFrase', kwargs)


class EntradaVoz(State):
    def run(self, kwargs):
        audio_code = self.get_audio_data()
        if audio_code == None: return
        if audio_code >= 20 and audio_code <= 27:
            kwargs['sequencia'].append(audio_code)
        self.go_to("EntradaVoz", kwargs)
        if audio_code == -4:
            self.go_to("RepiteEjecutaInstruccion", kwargs)
        print(kwargs['sequencia'])


class RepiteEjecutaInstruccion(State):
    def run(self, kwargs):
        print(f'Ejecutando la sequencia {kwargs}')
        if len(kwargs["sequencia"]) != 0:
            kwargs["it"] = kwargs['map'][kwargs['sequencia'][-1]][1]
            self.go_to(kwargs['map'][kwargs['sequencia'][-1]][0], kwargs)
            kwargs["sequencia"].pop()
        else:
            self.go_to("Reset", kwargs)
            
        
class RepiteDerecha(State):
    def run(self,kwargs):
        print("girando derecha")
        if kwargs["it"] != 0:
            self.go_to("RepiteDerecha", kwargs)
            kwargs["it"] -= 1
        else:
            self.go_to("RepiteEjecutaInstruccion", kwargs)

        
class RepiteIzquierda(State):
    def run(self,kwargs):
        print("girando izquierda")
        if kwargs["it"] != 0:
            self.go_to("RepiteIzquierda", kwargs)
            kwargs["it"] -= 1
        else:
            self.go_to("RepiteEjecutaInstruccion", kwargs)

        
class RepiteAdelante(State):
    def run(self,kwargs):
        print("Yendo Recto")
        if kwargs["it"] != 0:
            self.go_to("RepiteAdelante", kwargs)
            kwargs["it"] -= 1
        else:
            self.go_to("RepiteEjecutaInstruccion", kwargs)

        
class RepiteAtras(State):
    def run(self,kwargs):
        print("tirando hacia atras")
        if kwargs["it"] != 0:
            self.go_to("RepiteAtras", kwargs)
            kwargs["it"] -= 1
        else:
            self.go_to("RepiteEjecutaInstruccion", kwargs)

    
'''
    Tel me a joke
'''

class InitJoke(State):
    jokes = [
        "Miguel gay",
        "Miguel's mom",
        "The fuking Miguel",
        '''
    What did one traffic light say to the other? Stop looking at me, I'm changing! 
        '''
        ,
        '''
        What do you call bears with no ears? B.
        ''',
        '''
        Why do French people eat snails? They don't like fast food!
        '''
        ,
        '''
        What is sticky and brown? A stick!
        '''
        ,
        '''
        Want to hear a construction joke? Oh never mind, I'm still working on that one.
        '''
        ,
        '''
        I hate Russian dolls… they're so full of themselves!
        '''
    ]
    def run(self, kwargs):
        kwargs['next_state'] = 'Reset'
        id_joke = random.randint(0, len(self.jokes)-1)
        kwargs['voice'] = self.jokes[id_joke]
        self.go_to("DecirFrase", kwargs)

'''
    Donde estoy
'''

class InitWhereAmI(State):
    def run(self, kwargs):
        kwargs['next_state'] = 'SearchFace'
        kwargs['voice'] = 'Where are you?'
        self.go_to("DecirFrase", kwargs)

class SearchFace(State):
    def run(self, kwargs):
        print('Moviendose hacia la derecha')
        if self.detecta_cara():
            kwargs['next_state'] = 'Reset'
            kwargs['voice'] = 'Here you are!!'
            self.go_to("DecirFrase", kwargs)
        else:
            self.go_to("SearchFace", kwargs)