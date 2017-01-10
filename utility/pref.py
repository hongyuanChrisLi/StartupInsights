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
        logger.exception("Environment Variable Not Found: " + str(var_name))
        sys.exit(init.ENV_VAR_NOT_FOUND)
