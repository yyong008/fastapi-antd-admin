import os
from dotenv import load_dotenv


load_dotenv()

SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")
DATABASE_URL = os.getenv("DATABASE_URL")
PRESENTATION_MODE = os.getenv("PRESENTATION_MODE")
DEBUG = os.getenv("DEBUG")
