import yaml
from lib.file import get_full_path
from lib import logger

logger.config()
log = logger.get_logger(__name__)


class SingletonDecorator:
    def __init__(self, arg_class):
        self._cls = arg_class
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self._cls(*args, **kwargs)
        return self.instance


@SingletonDecorator
class AppConfig:
    def __init__(self):
        config_path = get_full_path('configs', 'rover_configs.yml')
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        log.info('Rover Configuration loaded successfully')

