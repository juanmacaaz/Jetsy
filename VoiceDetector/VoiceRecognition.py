import pyaudio

import torch
from glob import glob

from VoiceDetector.auxiliar import *

def process_audio(last_output):
    CHUNK_SIZE = 1024
    CHUNK_SIZE_PLAY = 1024
    FORMAT = pyaudio.paInt16
    RATE = 44100
    MAXIMUM = 16384
    THRESHOLD = 1800
    LANGUAGE = 'es'

    device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU
    model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                        model='silero_stt',
                                        language=LANGUAGE, # also available 'de', 'es'
                                        device=device)
    (read_batch, split_into_batches,
    read_audio, prepare_model_input) = utils

    while True:
        print("Háblale al micrófono")
        record_to_file('tmp.wav')
        print("Grabado! Escrcito a tmp.wav")
        test_files = glob('tmp.wav')
        batches = split_into_batches(test_files, batch_size=10)
        input = prepare_model_input(read_batch(batches[0]),
                                    device=device)
        output = model(input)
        
        last_output[0] = decoder(output[0].cpu())