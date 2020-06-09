import logging
import sys

from logging.handlers import *


class CustomLogger:

    def __init__(self):
        self.logger = logging.getLogger("apexLogger")
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            '[ %(asctime)s ] '
            '[ %(levelname)s ] - '
            '[ %(filename)s line %(lineno)s ] - '
            '%(message)s',
            datefmt='%m-%d-%Y %I:%M:%S %p'
        )

        # In the off chance that our CustomLogger object is instantiated in
        # multiple places and not placed via dependency injection, then the
        # following will ensure that we don't have >1 logger instances
        # logging to our multi-point handlers.
        if not self.logger.handlers:
            # Add our Stream handler for system output.
            handlerToGoToSysOutput = logging.StreamHandler(sys.stdout)
            handlerToGoToSysOutput.setFormatter(formatter)

            # TODO: Re-add the file handler below once a resource is allocated.

            # Add our File handler for file output.
            # handlerToGoToFileLog = RotatingFileHandler(
            #     'data/logs/logging.log',
            #     backupCount=5,
            #     maxBytes=1024000
            # )
            # handlerToGoToFileLog.setFormatter(formatter)

            # Add our handlers.
            self.logger.addHandler(handlerToGoToSysOutput)
            # self.logger.addHandler(handlerToGoToFileLog)
