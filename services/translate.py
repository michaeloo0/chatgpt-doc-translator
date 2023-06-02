import os 
from typing import List
from dotenv import load_dotenv, find_dotenv
from models.models import Document, TranslateResult, ApiType, TranslateType
from services.utils.interact_llm import call_openai

_ = load_dotenv(find_dotenv()) # read local .env file


async def get_translate_results(texts: List[Document], translate_type:str, api_type: str) -> List[TranslateResult]:
    
    results = []
    sys_prompt = os.environ[translate_type.upper()]
    for text in texts:
        response = await call_openai(sys_prompt=sys_prompt, user_prompt=text.text, api_type=api_type)
        if response:
            choices = response["choices"] 
            completion = choices[0].message.content.strip()
            result = TranslateResult(original_content=text.text, translated_content=completion)
            results.append(result)
      
    return results