import sys
import os
import time

from multiprocessing import Process, Manager

from VoiceDetector.VoiceRecognition import process_audio 
from ObjectClassificator.VideoDetector import process_video

lista_estados_importados = []
for entry in os.scandir('states'):
        if entry.is_file():
            string = f'from states import {entry.name}'[:-3]
            lista_estados_importados.append(entry.name[:-3])
            exec (string)

def get_clases_by_module(module):
    lista_clases = []
    current_module = sys.modules[module]
    for key in dir(current_module):
        if isinstance( getattr(current_module, key), type ):
            lista_clases.append(key)
    return lista_clases

class StateMachine:
    def __init__(self, initial_state):

        """
        Estado inicial del automata
        """
        
        self.state = initial_state
        self.states = {}
        self.kwargs = None
        self.global_data = {}

        """
            Diccionario con informacion que necesitamos siempre
            para calcular el siguiente estado.
        """
        self.global_data = {}
        self.load_states()

    def load_states(self):
        for entry in lista_estados_importados:
            try:
                tmp = get_clases_by_module(f"states.{entry}")
                for state in tmp:
                    print(state)
                    st_tmp = eval(f"{entry}.{state}(self)")
                    self.add_state(st_tmp)
            except: pass

    def add_state(self, state):
        self.states[state.name] = state

    def run(self):
        
        manager = Manager()
        self.global_data = manager.dict()
        self.global_data['audio'] = 0
        self.global_data['video'] = None

        p = Process(target=process_audio, args=(self.global_data,))
        p.start()

        p = Process(target=process_video, args=(self.global_data,))
        p.start()

        while 1:
            # Coger informacion de la voz
            #print(self.global_data['video'])
            if self.global_data['audio'] == -1:
                self.state = 'Reset'
            # Coger informacion del video
            
            # Coger informacion de los sensores
            # Ejecutar el estado actual
            print(self.state)
            self.states[self.state].run(self.kwargs)
            time.sleep(0.5)