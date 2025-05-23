import logging
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)


class CustomFormatter(logging.Formatter):
    yellow = "\033[33m"
    bright_yellow = "\033[93m"
    red = "\033[31m"
    bright_red = "\033[91m"
    green = "\33[32m"
    violet = "\33[35m"

    bold = "\033[1m"
    reset = "\033[0m"

    date = "%(asctime)s.%(msecs)03d"
    level = " | %(levelname)s"
    message = " %(message)s"

    FORMATS = {
        logging.DEBUG: bold + date + bright_yellow + level + 4 * ' ' + '|' + message + reset,
        logging.INFO: bold + date + green + " | " + "INFO" + 2 * ' ' + '|' + message + reset,
        logging.WARNING: bold + date + yellow + " | " + "WARNING" + 2 * ' ' + '|' + message + reset,
        logging.ERROR: bold + date + red + level + 4 * ' ' + '|' + message + reset,
        logging.CRITICAL: bold + date + bright_red + level + ' ' + '|' + message + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%H:%M:%S')
        return formatter.format(record)


logging.Formatter(datefmt='%H:%M:%S')
handler = logging.StreamHandler()
handler.setFormatter(CustomFormatter())

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)