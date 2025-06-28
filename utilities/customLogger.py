# utils/logger.py

import logging
import os

class LogGen:
    @staticmethod
    def loggen(logfile_name: str):
        logger = logging.getLogger(logfile_name)
        if not logger.handlers:
            log_path = os.path.join("Logs", logfile_name + ".log")
            os.makedirs(os.path.dirname(log_path), exist_ok=True)
            fhandler = logging.FileHandler(filename=log_path, mode='w')
            formatter = logging.Formatter(fmt='%(asctime)s: %(name)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            fhandler.setFormatter(formatter)
            logger.addHandler(fhandler)
            logger.setLevel(logging.INFO)
        return logger
