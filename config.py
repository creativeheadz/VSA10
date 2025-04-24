import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

ENDPOINT = os.getenv("ENDPOINT")
TOKEN_ID = os.getenv("TOKEN_ID")
TOKEN_SECRET = os.getenv("TOKEN_SECRET")