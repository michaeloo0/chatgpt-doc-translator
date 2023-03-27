import os 
import openai
from dotenv import load_dotenv
from typing import List
from models.models import Document, TranslateResult
from tenacity import retry, wait_random_exponential, stop_after_attempt
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG") 
model = os.getenv("OPENAI_MODEL") 

# @retry(wait=wait_random_exponential(min=1, max=20), stop=stop_after_attempt(3))
def get_translate_results(texts: List[Document], target: str) -> List[List[str]]:
    """
    Embed texts using OpenAI's ada model.

    Args:
        texts: The list of texts to embed.

    Returns:
        A list of embeddings, each of which is a list of floats.

    Raises:
        Exception: If the OpenAI API call fails.
    """
    # Call the OpenAI API to get the embeddings
    results = []
    
    for text in texts:
        messages = [{"role": "system", "content": target}]
        user_messaeg = {"role": "user", "content": text.text}
        messages.append(user_messaeg) 
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages
        )
        choices = response["choices"]  # type: ignore
        completion = choices[0].message.content.strip()
        result = TranslateResult(original_content=text.text, translated_content=completion)
        results.append(result)
      
    # Return the embeddings as a list of lists of floats
    return results