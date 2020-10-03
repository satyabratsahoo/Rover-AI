import pyttsx
from lib.common import SingletonDecorator


@SingletonDecorator
class VoiceService:
    def __init__(self):
        self.engine = pyttsx.init()
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('volume', 1.0)
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    def say(self, arg_in_text):
        self.engine.say(arg_in_text)
        self.engine.runAndWait()
