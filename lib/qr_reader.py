import json
from lib.common import log


class QrReader:
    def __init__(self):
        pass

    def process(self, arg_data):
        try:
            data_in = json.loads(arg_data)
            log.info(data_in)
        except Exception as ex:
            log.debug(f'Invalid QR Value: {data_in}')
