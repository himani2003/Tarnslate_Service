# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from googletrans import Translator

# # Create the FastAPI app
# app = FastAPI()

# # Initialize the Google Translator
# translator = Translator()

# # Define a request model
# class TranslateRequest(BaseModel):
#     text: str

# # Define a response model
# class TranslateResponse(BaseModel):
#     translated_text: str

# @app.post("/translate/hindi", response_model=TranslateResponse)
# async def translate_to_hindi(request: TranslateRequest):
#     """
#     Translate text to Hindi.
#     Args:
#         request (TranslateRequest): JSON body with the text to translate.
#     Returns:
#         TranslateResponse: Translated text in Hindi.
#     """
#     try:
#         translated = translator.translate(request.text, dest="hi")  # 'hi' is the language code for Hindi
#         return TranslateResponse(translated_text=translated.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

# @app.post("/translate/tamil", response_model=TranslateResponse)
# async def translate_to_tamil(request: TranslateRequest):
#     """
#     Translate text to Tamil.
#     Args:
#         request (TranslateRequest): JSON body with the text to translate.
#     Returns:
#         TranslateResponse: Translated text in Tamil.
#     """
#     try:
#         translated = translator.translate(request.text, dest="ta")  # 'ta' is the language code for Tamil
#         return TranslateResponse(translated_text=translated.text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from googletrans import Translator

# # Create the FastAPI app
# app = FastAPI()

# # Initialize the Google Translator
# translator = Translator()

# # Define a request model
# class TranslateRequest(BaseModel):
#     text: str

# # Define a response model
# class TranslateResponse(BaseModel):
#     translated_text: str

# @app.post("/translate/hindi", response_model=TranslateResponse)
# async def translate_to_hindi(request: TranslateRequest):
#     """
#     Translate text to Hindi.
#     Args:
#         request (TranslateRequest): JSON body with the text to translate.
#     Returns:
#         TranslateResponse: Translated text in Hindi.
#     """
#     try:
#         # Split the input text into lines
#         lines = request.text.split("\n")
        
#         # Translate each line individually and collect the results
#         translated_lines = [translator.translate(line, dest="hi").text for line in lines]
        
#         # Join the translated lines back together with new line characters
#         translated_text = "\n".join(translated_lines)
        
#         return TranslateResponse(translated_text=translated_text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

# @app.post("/translate/tamil", response_model=TranslateResponse)
# async def translate_to_tamil(request: TranslateRequest):
#     """
#     Translate text to Tamil.
#     Args:
#         request (TranslateRequest): JSON body with the text to translate.
#     Returns:
#         TranslateResponse: Translated text in Tamil.
#     """
#     try:
#         # Split the input text into lines
#         lines = request.text.split("\n")
        
#         # Translate each line individually and collect the results
#         translated_lines = [translator.translate(line, dest="ta").text for line in lines]
        
#         # Join the translated lines back together with new line characters
#         translated_text = "\n".join(translated_lines)
        
#         return TranslateResponse(translated_text=translated_text)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")
    
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googletrans import Translator
from fastapi.responses import PlainTextResponse

# Create the FastAPI app
app = FastAPI()

# Initialize the Google Translator
translator = Translator()

# Define a request model
class TranslateRequest(BaseModel):
    insert: str

# Helper function to split text into chunks of <= 5000 characters
def split_text_into_chunks(insert: str, max_chunk_size: int = 4000):
    lines = insert.split("\n")  # Split text by lines
    chunks = []
    current_chunk = []
    current_length = 0

    for line in lines:
        line_length = len(line) + 1  # Add 1 for the newline character
        if current_length + line_length > max_chunk_size:
            chunks.append("\n".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(line)
        current_length += line_length

    if current_chunk:
        chunks.append("\n".join(current_chunk))

    return chunks

@app.post("/translate/hindi", response_class=PlainTextResponse)
async def translate_to_hindi(request: TranslateRequest):
    """
    Translate text to Hindi.
    Args:
        request (TranslateRequest): JSON body with the text to translate.
    Returns:
        PlainTextResponse: Translated text in Hindi as plain text.
    """
    try:
        print(request)
        print(request.insert)
        # Split the input text into manageable chunks
        chunks = split_text_into_chunks(request.insert)

        # Translate each chunk and collect the results
        translated_chunks = [translator.translate(chunk, dest="hi").text for chunk in chunks]

        # Combine all translated chunks into one string
        translated_text = "\n".join(translated_chunks)

        # Return the translated text as plain text
        return PlainTextResponse(content=translated_text, media_type="text/plain")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.post("/translate/tamil", response_class=PlainTextResponse)
async def translate_to_tamil(request: TranslateRequest):
    """
    Translate text to Tamil.
    Args:
        request (TranslateRequest): JSON body with the text to translate.
    Returns:
        PlainTextResponse: Translated text in Tamil as plain text.
    """
    try:
        # Split the input text into manageable chunks
        chunks = split_text_into_chunks(request.insert)

        # Translate each chunk and collect the results
        translated_chunks = [translator.translate(chunk, dest="ta").text for chunk in chunks]

        # Combine all translated chunks into one string
        translated_text = "\n".join(translated_chunks)

        # Return the translated text as plain text
        return PlainTextResponse(content=translated_text, media_type="text/plain")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")
