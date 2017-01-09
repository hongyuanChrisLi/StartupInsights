import os
import logging
import sys
import __init__ as init


def get_env_variable(var_name):
    """
    Get environment variable or return exception
    """
    logging.config.fileConfig('logging.ini')
    logger = logging.getLogger(__name__)

    try:
        return os.environ[var_name]
    except KeyError as e:
        logger.error("Environment Variable Not Found: " + var_name, e)
        sys.exit(init.ENV_VAR_NOT_FOUND)
