import os
import openai
from fastapi import HTTPException
from dotenv import load_dotenv, find_dotenv
from models.models import ApiType

_ = load_dotenv(find_dotenv()) # read local .env file

async def call_openai(sys_prompt: str, user_prompt: str, api_type: str):
    
    messages = [
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt}
    ]
    
    
    if api_type not in ApiType.__members__:
        raise HTTPException(status_code=500, detail=f"Only support Azure and OpenAI")
        
        
    if api_type == ApiType.azure.value:
        engine=os.environ['AZURE_DEPLOYMENT_NAME']
        openai.api_type = api_type
        openai.api_key = os.environ['AZURE_API_KEY']
        openai.api_base = os.environ['AZURE_API_BASE']
        openai.api_version = os.environ['AZURE_API_VERSION']
        response = openai.ChatCompletion.create(
            engine=engine,
            messages=messages,
            temperature=float(os.environ['TEMPERATURE'])
        )
        return response
    
    
    elif api_type == ApiType.open_ai.value:
        openai.api_key = os.environ['OPENAI_API_KEY']
        openai.organization = os.environ["OPENAI_ORG"] 
        response = openai.ChatCompletion.create(
            model=os.environ["OPENAI_MODEL"],
            messages=messages,
            temperature=float(os.environ['TEMPERATURE'])
        )
        return response
