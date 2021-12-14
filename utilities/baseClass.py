import inspect
import logging

import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    # this method provides logging to the test
    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('../reports/logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
