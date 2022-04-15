import pyaudio
import os

import torch
from glob import glob
from array import array
from shutil import move
from struct import pack
from sys import byteorder
import wave

CHUNK_SIZE = 1024
CHUNK_SIZE_PLAY = 1024
FORMAT = pyaudio.paInt16
RATE = 44100
MAXIMUM = 16384
THRESHOLD = 1800

def is_silent(snd_data):
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    """Normaliza el volumen de una pista de audio"""
    times = float(MAXIMUM) / max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i * times))
    return r


def trim(snd_data):
    """Corta los silencios al principio y al final"""

    def _trim(sound_data):
        snd_started = False
        r = array('h')

        for i in sound_data:
            if not snd_started and i > THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    snd_data = _trim(snd_data)
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data


def add_silence(snd_data, seconds):
    r = array('h', [0 for i in range(int(seconds * RATE))])
    r.extend(snd_data)
    r.extend([0 for i in range(int(seconds * RATE))])
    return r


def record():
    """ Graba el audio usando el micrófono """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
                    input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if not silent:
            num_silent = 0

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 90:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    r = normalize(r)
    r = trim(r)
    r = add_silence(r, 0.5)
    return sample_width, r


def record_to_file(path):
    """ Usando la función record, crea un fichero wav en el directorio del programa """
    sample_width, data = record()
    data = pack('<' + ('h' * len(data)), *data)

    if os.path.exists(path):
        os.remove(path)
    
    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

def reproduce_audio_file(dir_audio):
    """ Reproduce el audio del fichero wav """
    p = pyaudio.PyAudio()
    wf = wave.open(dir_audio, 'rb')

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK_SIZE_PLAY)

    while data != b'':
        stream.write(data)
        data = wf.readframes(CHUNK_SIZE_PLAY)

    stream.stop_stream()
    stream.close()

    p.terminate()


device = torch.device('cpu')  # gpu also works, but our models are fast enough for CPU
model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                       model='silero_stt',
                                       language='es', # also available 'de', 'es'
                                       device=device)
(read_batch, split_into_batches,
 read_audio, prepare_model_input) = utils  # see function signature for details

while True:
    print("Háblale al micrófono")
    record_to_file('demo.wav')
    print("Grabado! Escrcito a demo.wav")
    test_files = glob('demo.wav')
    batches = split_into_batches(test_files, batch_size=10)
    input = prepare_model_input(read_batch(batches[0]),
                                device=device)
    output = model(input)
    
    for example in output:
        print(decoder(example.cpu()))