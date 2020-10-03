import json
from lib.common import log
from lib.rover_navigation import Navigation


class QrReader:
    def __init__(self):
        pass

    def process(self, arg_data):
        try:
            data_in = json.loads(arg_data)
            log.info(data_in)
            qr_command = data_in['action']
            navigation = Navigation()
            function = getattr(navigation, qr_command)
            function()

        except Exception as ex:
            log.debug(f'Invalid QR Value: {data_in}')
