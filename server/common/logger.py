import yaml
import logging
import logging.config
from .settings import LOGGING_CONF,PROJECT_NAME

with open(LOGGING_CONF,"r") as f:
    config = yaml.load(f,Loader=yaml.FullLoader)


logging.config.dictConfig(config)
logger = logging.getLogger(PROJECT_NAME)
