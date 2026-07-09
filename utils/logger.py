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