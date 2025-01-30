from .app import create_app

# text_segmentation/config.py
import os
from pathlib import Path

class Config:
    VNCORENLP_PATH = os.getenv('VNCORENLP_PATH', '/app/vncorenlp')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
