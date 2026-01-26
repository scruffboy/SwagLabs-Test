import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and return logger with name

    Logger:
    - sets the DEBUG logic level
    - outputs logs to the console
    - uses the following format: "date | logger name | level | message"

    :param name: logger name
    :return: Configured logging.Logger
    """

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
