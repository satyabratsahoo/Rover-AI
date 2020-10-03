import RPi.GPIO as GPIO
from time import sleep
from lib.common import AppConfig, SingletonDecorator, log

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


@SingletonDecorator
class Navigation:
    def __init__(self):
        app_config = AppConfig().config
        motor_l = app_config['navigation_config']['motor_L']
        motor_r = app_config['navigation_config']['motor_R']
        self.motor_L = Motor(motor_l)
        self.motor_R = Motor(motor_r)
        self.d_sleep = 0.4
        log.info('Navigation System Initialized')

    def move_forward(self):
        self.motor_L.forward()
        self.motor_R.forward()
        log.info('[ROVER] Moving forward')
        sleep(self.d_sleep)
        self.stop()

    def move_backward(self):
        self.motor_L.backward()
        self.motor_R.backward()
        log.info('[ROVER] Moving Backward')
        sleep(self.d_sleep)
        self.stop()

    def rotate_left(self):
        self.motor_L.backward()
        self.motor_R.forward()
        log.info('[ROVER] Rotating Left')
        sleep(self.d_sleep)
        self.stop()

    def rotate_right(self):
        self.motor_R.backward()
        self.motor_L.forward()
        log.info('[ROVER] Rotating Right')
        sleep(self.d_sleep)
        self.stop()

    def stop(self):
        self.motor_L.stop()
        self.motor_R.stop()

    def rotate_360(self):
        self.motor_R.backward()
        self.motor_L.forward()
        sleep(1)
        self.stop()
        log.info('[ROVER] Rotate 360')


class Motor:
    def __init__(self, arg_config):
        self.enable = arg_config['gpio_pins']['enable']
        self.in1 = arg_config['gpio_pins']['in1']
        self.in2 = arg_config['gpio_pins']['in2']
        GPIO.setup(self.enable, GPIO.OUT)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        self.pwm = GPIO.PWM(self.enable, 0)
        self.default_duty_cycle = arg_config['pwm_default']
        self.pwm.start(0)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)

    def backward(self):
        self.pwm.ChangeDutyCycle(self.default_duty_cycle)
        GPIO.output(self.in1, GPIO.HIGH)
        GPIO.output(self.in2, GPIO.LOW)

    def forward(self):
        self.pwm.ChangeDutyCycle(self.default_duty_cycle)
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.HIGH)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
