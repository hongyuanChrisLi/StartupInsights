import os
import logging
import sys
import __init__ as init


def get_env_variable(var_name):
    """
    Get environment variable or return exception
    """
    logging.config.fileConfig('logging.ini')

    # logging.basicConfig(
    #     filename='log.txt',
    #     format='%(levelname)s: %(message)s',
    #     level=logging.INFO
    # )

    logger = logging.getLogger(__name__)
    # logger.addHandler(logging.FileHandler())

    try:
        return os.environ[var_name]
    except KeyError as e:
        logger.error("Environment Variable Not Found: " + var_name, e)
        sys.exit(init.ENV_VAR_NOT_FOUND)
