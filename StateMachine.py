import sys
import os
import time

from multiprocessing import Process, Manager

from VoiceDetector.VoiceRecognition import process_audio 

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
        lista = manager.list()
        lista.append(None)

        p = Process(target=process_audio, args=(lista,))
        p.start()

        while 1:
            time.sleep(0.5)
            # Coger informacion de la voz
            print(lista)
            # Conger informacion de los sensores

            # Ejecutar el estado actual
            self.states[self.state].run(self.kwargs)