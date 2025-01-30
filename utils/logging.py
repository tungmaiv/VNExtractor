import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def log_info(endpoint: str, status_code: int, message: str):
    logging.info(f"{endpoint} - {status_code} - {message}")

def log_error(endpoint: str, status_code: int, message: str):
    logging.error(f"{endpoint} - {status_code} - {message}")

def log_warning(endpoint: str, status_code: int, message: str):
    logging.warning(f"{endpoint} - {status_code} - {message}")
