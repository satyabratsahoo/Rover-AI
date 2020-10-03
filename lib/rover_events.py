from lib.common import AppConfig
import sys
from lib.common import log
# from lib.voice import VoiceService
from lib.rover_navigation import Navigation


def process_event(arg_key):
    event_cfg = AppConfig().config['key_events']
    if arg_key != -1:
        char_value = chr(arg_key).upper() if arg_key != 32 else 'SPACE'
        if char_value in event_cfg:
            log.debug(f'Event Received: {event_cfg[char_value]}')
            if event_cfg[char_value] == 'exit':
                sys.exit(0)
            navigation = Navigation()
            function = getattr(navigation, event_cfg[char_value])
            function()
