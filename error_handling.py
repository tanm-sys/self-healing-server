import structlog

logger = structlog.get_logger()

def handle_error(error):
    logger.error(f"Error occurred: {error}")
