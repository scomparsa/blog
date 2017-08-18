# -*- coding:utf-8 -*-
''' Logger Module '''

import logging
import logging.handlers

LOGGING_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOGGING_MSG_FORMAT  = '%(asctime)s %(levelname)s %(message)s'

def get_logger(name, filepath):
    ''' get logger handler '''
    logger = logging.getLogger(name)
    hdlr = logging.handlers.TimedRotatingFileHandler(filepath, when='MIDNIGHT')
    formatter = logging.Formatter(LOGGING_MSG_FORMAT)
    hdlr.setFormatter(formatter)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(hdlr)
    return logger

def close_logger(logger):
    ''' close logger handler '''
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)