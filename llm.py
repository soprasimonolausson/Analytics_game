import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
AZURE_OPENAI_API_ENDPOINT: str = os.getenv("AZURE_ENDPOINT")
AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_API_KEY")
    
def set_up_client():
    client = AzureOpenAI(
    azure_endpoint = AZURE_OPENAI_API_ENDPOINT,
    api_key= AZURE_OPENAI_API_KEY,  
    api_version=os.getenv('version'),
    )
    return client