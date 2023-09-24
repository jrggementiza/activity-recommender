import os

from dotenv import load_dotenv

# TODO: Load lazily instead
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
