import tone
import pyaudio
import sounddevice as sd
import time 
from sys import platform

class AudioController:
    '''
    use this controller to play and control sounds.
    you can only use one AudioController object at a time.
    when playing a sound you must call stop_sound before
    playing another. 
    '''

    sound_is_playing = False
    sound_object = None
    stream = None

    def __init__(self, **kwargs):
        self.p = pyaudio.PyAudio()
        pass

    def play_sound(self=None, instance=None, frequencies=[(400,.2), (400,.2)], duration=-1):
        '''
        generate a tone for each frequency passed in a list called frequencies
        each tone is played on a single channel
        '''

        assert not AudioController.sound_is_playing
        AudioController.sound_is_playing = True
        sounds = tone.Tones(frequencies, duration)
        if platform == "linux" or platform == "linux2":
            with sd.OutputStream(
                samplerate = tone.RATE,
                blocksize  = tone.BUFSIZE,
                channels   = sounds.num_channels,
                dtype      = 'int16',
                device     = 4,
                callback   = sounds.callback) as stream:
                while(stream.active):
                    time.sleep(.1)
        else:
            AudioController.stream = self.p.open(
                format=pyaudio.get_format_from_width(2),
                channels=sounds.num_channels,
                rate=tone.RATE,
                frames_per_buffer=tone.BUFSIZE,
                output=True,
                stream_callback=sounds.callback)

        #AudioController.stream.start_stream()
        AudioController.sound_object = sounds

    def stop_sound(self, instance=None):
        '''
        stop currently playing sound and close the stream
        this should be called before starting a new sound
        '''
        assert AudioController.sound_is_playing == True
        AudioController.sound_object.stop_sound()
        AudioController.sound_is_playing = False 

    def update_tones(self, slider=None, value=None, frequencies=None):
        assert AudioController.sound_is_playing == True
        current_freqs = self.sound_object.frequencies
        if slider:
            AudioController.sound_object.change_freqs_to([(int(value), current_freqs[0][1])] + current_freqs[1:])
        else:
            AudioController.sound_object.change_freqs_to(frequencies)
