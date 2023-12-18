import os
from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = True
MODEL = os.environ.get('OPEN_AI_MODEL')
AUTH_USER_MODEL = 'accounts.User'
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY_FINETUNING')