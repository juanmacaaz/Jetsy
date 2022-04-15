import pyaudio
import os

import torch
from glob import glob
from array import array
from shutil import move
from struct import pack
from sys import byteorder
import wave

class VoiceRecognition:
    CHUNK_SIZE = 1024
    CHUNK_SIZE_PLAY = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    MAXIMUM = 16384
    THRESHOLD = 1800
    LANGUAGE = 'es'

    def __init__(self):
        self.device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU
        self.model, self.decoder, self.utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                            model='silero_stt',
                                            language=self.LANGUAGE, # also available 'de', 'es'
                                            device=self.device)
        (self.read_batch, self.split_into_batches,
        self.read_audio, self.prepare_model_input) = self.utils

    