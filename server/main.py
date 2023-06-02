import os
import uvicorn

from fastapi import FastAPI, File, HTTPException, Depends, Body, UploadFile,Response, status
from services.utils.process_file import get_document_from_file
from services.utils.generate_pdf import generate_pdf
from services.translate import get_translate_results
from services.utils.split_text import text_splitter

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
file_folder = os.environ['FILE_FOLDER']

from models.models import (
  Document
)
from models.api import (
  TranslateResponse,
  TranslatedFileResponse
)


app = FastAPI()

@app.post(
    "/translate-file",
    response_model=TranslateResponse,
)
async def translate_file(
    file: UploadFile = File(...),
    api_type: str = Body(...),
    translate_type: str = Body(...)
):
    try:
        document = await get_document_from_file(file)
    except Exception:
        raise e
   
    splitter = text_splitter()
    chunks = splitter.split_text(document.text)
    documents = [Document(text=chunk) for chunk in chunks]
    
    try:
        results = await get_translate_results(documents, translate_type=translate_type, api_type=api_type)
        return TranslateResponse(results=results)
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"str({e})")

@app.post(
    "/translate-file-download",
    response_model=TranslatedFileResponse,
)
async def translate_file(
    file: UploadFile = File(...),
    api_type: str = Body(...),
    translate_type: str = Body(...)
):
    try:
        document = await get_document_from_file(file)
    except Exception:
        raise e
   
    splitter = text_splitter()
    chunks = splitter.split_text(document.text)
    documents = [Document(text=chunk) for chunk in chunks]
    
    try:
        results = await get_translate_results(documents, translate_type=translate_type, api_type=api_type)
        download_link = await generate_pdf(results)
        return TranslatedFileResponse(result=download_link)
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"str({e})")

@app.get("/download-file/{token}")
async def serve_text_file(token: str):
    # Check if the file exists
    if os.path.exists(f"{file_folder}/{token}.txt"):
        # Set the response headers
        headers = {
            "Content-Type": "text/plain",
            "Content-Disposition": f"attachment; filename={token}.txt",
        }

        # Return the file contents as a response with the headers set
        with open(f"{file_folder}/{token}.txt", "rb") as f:
            contents = f.read()
            return Response(content=contents, status_code=status.HTTP_200_OK, headers=headers)
    else:
        # Return a 404 error if the file does not exist
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
def start():
    uvicorn.run("server.main:app", host="0.0.0.0", port=8000, reload=True)
