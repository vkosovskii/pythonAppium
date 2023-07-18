import logging


def gen_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.propagate = 0
        console = logging.StreamHandler()
        logger.addHandler(console)
        formatter = logging.Formatter(
            "\x1b[33;20m" + "%(asctime)s %(name)s:  %(message)s"
        )
        console.setFormatter(formatter)
    return logger
