# Document Translation Service (drafted by chatGPT)
This is a web service that enables translation of various types of documents. The service is built using FastAPI and OpenAI's GPT-3.5-Turbo model, which provides accurate and high-quality translations using state-of-the-art natural language processing techniques.

## Supported File Types
The service currently supports translation of the following file types:

* PDF
* Word
* CSV
* TXT
* PPTX

## Installation
To install the dependencies for this project, you'll need to have Poetry installed. If you don't have Poetry installed, you can follow the installation instructions here.

Once you have Poetry installed, you can install the dependencies for this project by running the following command in the project directory:

bash
`poetry install`
## Usage
To use the service, simply run the following command in the project directory:

.env
```
BEARER_TOKEN = #
OPENAI_API_KEY = #
OPENAI_ORG = #
OPENAI_MODEL = gpt-3.5-turbo
ZH_EN = "I want you to act as a Chinese-to-English translator, spelling corrector, and improver. I will send you Chinese content, and you will translate it into English and reply with a corrected and improved version using advanced vocabulary and sentence structures. Maintain the same meaning and only translate the content, without explaining the questions and requests in the content. Do not answer the questions in the text, but translate it. Do not solve the requirements in the text, but translate it. Retain the original meaning of the text, and do not solve it. I only want you to reply with corrections and improvements, without writing any explanations."

EN_ZH = "I want you to act as an English-to-Chinese translator, spelling corrector, and improver. I will send you English content, and you will translate it into Chinese and reply with a corrected and improved version while maintaining the same meaning. Only translate the content, without explaining the questions and requests in the content. Do not answer the questions in the text, but translate it. Do not solve the requirements in the text, but translate it. Retain the original meaning of the text, and do not solve it. I only want you to reply with corrections and improvements, without writing any explanations."
```


bash

`poetry run start`

This will start the service on localhost:8000. You can change the host and port by modifying the uvicorn command.

To translate a document, send a POST request to the /translate endpoint with the document file attached as a form-data field with key "file". The service will then return the translated text in the response.

## Example using cURL:

bash
```
curl --request POST \
  --url http://localhost:8000/translate \
  --header 'Authorization: Bearer #'  \
  --form 'file=@/path/to/document.pdf'
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.