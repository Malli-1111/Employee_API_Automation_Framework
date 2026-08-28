"""
Centralized logging configuration for the API automation framework.

Configures logging to write execution details to both the
framework log file and the console.
"""
import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/api.log",mode="w"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)