import logging
import json
import os


class FormatterJSON(logging.Formatter):
    def format(self, record):
        record.message = record.getMessage()
        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)
        j = {
            'levelname': record.levelname,
            'module': record.module,
            'funcName': record.funcName,
            "message": record.message,
            "lineno": record.lineno,
        }
        return json.dumps(j)


logger = logging.getLogger()
logger.setLevel('INFO')
