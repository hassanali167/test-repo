"""
Topic: Logging in Python

Explanation:
The `logging` module is used for tracking events during execution.
"""

import logging

# Configuring logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Logging messages
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

"""
Code Explanation:
- `logging.basicConfig()` configures logging settings.
- Different levels: DEBUG, INFO, WARNING, ERROR, CRITICAL.
- Each message logs with a timestamp and severity level.
"""
