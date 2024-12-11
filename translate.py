from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from googletrans import Translator

# Create the FastAPI app
app = FastAPI()

# Initialize the Google Translator
translator = Translator()

# Define a request model
class TranslateRequest(BaseModel):
    text: str

# Define a response model
class TranslateResponse(BaseModel):
    translated_text: str

@app.post("/translate/hindi", response_model=TranslateResponse)
async def translate_to_hindi(request: TranslateRequest):
    """
    Translate text to Hindi.
    Args:
        request (TranslateRequest): JSON body with the text to translate.
    Returns:
        TranslateResponse: Translated text in Hindi.
    """
    try:
        translated = translator.translate(request.text, dest="hi")  # 'hi' is the language code for Hindi
        return TranslateResponse(translated_text=translated.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")

@app.post("/translate/tamil", response_model=TranslateResponse)
async def translate_to_tamil(request: TranslateRequest):
    """
    Translate text to Tamil.
    Args:
        request (TranslateRequest): JSON body with the text to translate.
    Returns:
        TranslateResponse: Translated text in Tamil.
    """
    try:
        translated = translator.translate(request.text, dest="ta")  # 'ta' is the language code for Tamil
        return TranslateResponse(translated_text=translated.text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation error: {str(e)}")