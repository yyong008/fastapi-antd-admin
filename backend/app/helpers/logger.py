import logging
import logging.config
from pathlib import Path

# Define log file path
log_file_path = Path("logs/app.log")
log_file_path.parent.mkdir(
    parents=True, exist_ok=True
)  # Ensure the logs directory exists

# Define logging configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
        "detailed": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s - [in %(pathname)s:%(lineno)d]"
        },
        "json": {
            "format": '{"timestamp": "%(asctime)s", "logger": "%(name)s", "level": "%(levelname)s", "message": "%(message)s"}'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": log_file_path,
            "formatter": "detailed",
            "encoding": "utf8",
        },
        "json_file": {
            "class": "logging.FileHandler",
            "filename": "logs/app.json.log",
            "formatter": "json",
            "encoding": "utf8",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console", "file", "json_file"],
            "propagate": False,
        },
    },
}

# Apply logging configuration
logging.config.dictConfig(LOGGING_CONFIG)

# Create logger instance for the application
logger = logging.getLogger("app")

# Example usage in other modules
# from app.core.logger import logger
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
