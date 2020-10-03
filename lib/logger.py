import logging.config
import logging.handlers
import logging
import yaml
from lib.file import get_full_path


def config():
    log_cfg = get_full_path('configs', 'logger.yml')
    with open(log_cfg, 'r') as file:
        cfg = yaml.safe_load(file.read())
        logging.config.dictConfig(cfg)


def get_logger(arg_name):
    return logging.getLogger(arg_name)

