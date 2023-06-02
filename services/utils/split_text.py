import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter


tokenizer = tiktoken.get_encoding('cl100k_base')

# create the length function
def tiktoken_len(text):
    tokens = tokenizer.encode(
        text,
        disallowed_special=()
    )
    return len(tokens)
  
def text_splitter(chunk_size=2048):
  text_splitter = RecursiveCharacterTextSplitter(
      # Set a really small chunk size, just to show.
      chunk_size = chunk_size,
      chunk_overlap  = 5,
      length_function = tiktoken_len,
  )
  return text_splitter