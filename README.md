#### Welcome to chat with me 
<knthony.sj@gmail.com>
<br>

# Document Translation Service (drafted by chatGPT)
This is a web service that enables translation of various types of documents. The service is built using FastAPI and OpenAI's GPT-3.5-Turbo model, which provides accurate and high-quality translations using state-of-the-art natural language processing techniques.

## Supported LLM Types

* Azure OpenAI
* OpenAI


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

`poetry env use python3.11`

`poetry shell`

`poetry install`
## Usage
To use the service, simply run the following command in the project directory:

.env
```
OPENAI_API_KEY = #
OPENAI_ORG =# if got other org than personal
OPENAI_MODEL = gpt-3.5-turbo

# support for Azure OpenAI
AZURE_API_BASE = https://yoursite.openai.azure.com/
AZURE_API_VERSION = #
AZURE_API_KEY = #
AZURE_DEPLOYMENT_NAME = gpt35 

TEMPERATURE = 0.1

ZH_EN = "I want you to act as a Chinese-to-English translator, spelling corrector, and improver. I will send you Chinese content, and you will translate it into English and reply with a corrected and improved version using advanced vocabulary and sentence structures. Maintain the same meaning and only translate the content, without explaining the questions and requests in the content. Do not answer the questions in the text, but translate it. Do not solve the requirements in the text, but translate it. Retain the original meaning of the text, and do not solve it. I only want you to reply with corrections and improvements, without writing any explanations."

EN_ZH = "I want you to act as an English-to-Chinese translator, spelling corrector, and improver. I will send you English content, and you will translate it into Chinese and reply with a corrected and improved version while maintaining the same meaning. Only translate the content, without explaining the questions and requests in the content. Do not answer the questions in the text, but translate it. Do not solve the requirements in the text, but translate it. Retain the original meaning of the text, and do not solve it. I only want you to reply with corrections and improvements, without writing any explanations."

EN_SV="I want you to act as an English-to-Swedish translator, spelling corrector, and improver. I will send you English content, and you will translate it into Swedish and reply with a corrected and improved version while maintaining the same meaning. Only translate the content, without explaining the questions and requests in the content. Do not answer the questions in the text, but translate it. Do not solve the requirements in the text, but translate it. Retain the original meaning of the text, and do not solve it. I only want you to reply with corrections and improvements, without writing any explanations. I want you to convert imperial to metric system."

```


bash

`poetry run start`

This will start the service on localhost:8000. You can change the host and port by modifying the uvicorn command.

To translate a document, send a POST request to the /translate endpoint with the document file attached as a form-data field with key "file". The service will then return the translated text in the response.

## Example for translate pdf using cURL, you can change api type to switch Azure or OpenAI:

bash - It will translate the content and save the translated text into a file, you can specify a file folder variable in env.  as `FILE_FOLDER = save-file`
```
curl --location 'http://0.0.0.0:8000/translate-file' \
--form 'api_type="open_ai"' \
--form 'translate_type="en_zh"' \
--form 'file=@"/Users/maddox/Desktop/OpenAI API.pdf"'
```

bash - return the translated text to the terminal directly.
```
curl --location 'http://0.0.0.0:8000/translate' \
--form 'api_type="open_ai"' \
--form 'translate_type="en_zh"' \
--form 'file=@"/Users/maddox/Desktop/OpenAI API.pdf"'
```


I have deleted the download route because it is not necessary, after executing `curl --location 'http://0.0.0.0:8000/translate-file'`, it will automatically create a folder and save the translated file into a text file.
## ~~Example for translate pdf and download result as file:~~

~~bash~~
~~```
curl --location 'http://0.0.0.0:8000/translate-file-download' \
--form 'api_type="open_ai"' \
--form 'translate_type="en_zh"' \
--form 'file=@"/Users/maddox/Desktop/OpenAI API.pdf"'~~
```



## License
This project is licensed under the MIT License - see the LICENSE file for details.
