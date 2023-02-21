import logging


logger = logging.getLogger(__name__)
handler = logging.FileHandler('basic_log.log', mode='w')
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.setLevel(level="INFO")
logger.addHandler(handler)
