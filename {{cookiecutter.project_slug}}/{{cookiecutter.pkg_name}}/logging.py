import logging
import sys

def verbosity_to_log_level(verbosity, default=logging.WARN):
    # Log levels go by 10's, with DEBUG=10 and CRITICAL=50
    # See https://docs.python.org/3/howto/logging.html#logging-levels
    return max(default - (verbosity * 10), 0)

def set_root_log_level(verbosity, default=logging.WARN):
    root_logger = logging.getLogger()
    log_level = verbosity_to_log_level(verbosity)
    root_logger.setLevel(log_level)

def init_logging():
    logging.basicConfig(
        stream=sys.stderr,
        format='%(levelname)s: %(message)s',
        level=logging.DEBUG)
