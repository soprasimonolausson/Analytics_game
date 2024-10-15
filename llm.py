import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_API_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
