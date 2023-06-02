import os
import secrets
from typing import List
from dotenv import load_dotenv, find_dotenv
from models.models import TranslateResult
_ = load_dotenv(find_dotenv()) # read local .env file
file_folder = os.environ['FILE_FOLDER']
host = os.environ['HOST']

async def generate_pdf(content_list: List[TranslateResult]):

    token = secrets.token_hex(16)
    if not os.path.exists(file_folder):
        os.makedirs(file_folder)

    with open(f"{file_folder}/{token}.txt", "w+") as f:
        for i in range(len(content_list)):
            f.write(content_list[i].translated_content)

    download_link = f"{host}/download-file/{token}"
    return download_link