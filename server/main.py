import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, File, HTTPException, Depends, Body, UploadFile
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.staticfiles import StaticFiles
from services.file import get_document_from_file
from services.translate import get_translate_results
from services.split_text import text_splitter
from models.models import (
  Document
)

from models.api import (
  TranslateResponse
    # QueryRequest,
    # QueryResponse,
)
load_dotenv()


# 
bearer_scheme = HTTPBearer()
BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
assert BEARER_TOKEN is not None


app = FastAPI()
# app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return credentials


@app.post(
    "/translate-file_zh",
    response_model=TranslateResponse,
)
async def translate_file_zh(
    file: UploadFile = File(...),
    token: HTTPAuthorizationCredentials = Depends(validate_token),
):
    #
    EN_ZH = os.environ.get("EN_ZH")
    document = await get_document_from_file(file)
    text = document.text
    splitter = text_splitter()
    chunks = splitter.split_text(text)
    documents = [Document(text=chunk) for chunk in chunks]
    try:
        results = get_translate_results(documents, EN_ZH)
        return TranslateResponse(results=results)
    
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail=f"str({e})")

# @app.on_event("startup")
# async def startup():
#     # global datastore
#     # datastore = await get_datastore()
#     pass


def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
