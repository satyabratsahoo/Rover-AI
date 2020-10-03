import cv2
from lib.common import AppConfig, log
from lib.rover_events import process_event
from lib.qr_reader import QrReader
from pyzbar.pyzbar import decode
from lib.rover_navigation import Navigation
# from lib.voice import VoiceService
import asyncio
if __name__ == '__main__':

    log.info('Rover Initialization Started ....')
    app_config = AppConfig().config
    log.info('Rover Initialization Completed ....')
    navigation = Navigation()
    log.info('Voice Service Initialization Started ....')
    # voice = VoiceService()
    # asyncio.run(voice.say('Rover-AI voice service is activated'))
    log.info('Voice Service Initialization Completed ....')

    log.info('Started Rover Camera ....')
    vs = cv2.VideoCapture(app_config['rover_cam']['device_id'])
    log.info('Rover Camera started successfully')
    qr_reader = QrReader()
    while True:
        ret, frame = vs.read()
        frame = cv2.resize(frame, (400, 400))
        img_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        value = decode(img_grey)
        if not value:
            pass
        else:
            qr_reader.process(value[0][0].decode('ascii'))
            cv2.rectangle(frame, (value[0][3][0]), (value[0][3][2]), (255, 0, 0), thickness=2)
        # Show the video frame :
        cv2.imshow("Rover-AI Camera View", frame)

        key = cv2.waitKey(1)
        process_event(key)
