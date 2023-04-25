"""Module providingFunction printing python version."""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['APIKEY']
URL = os.environ['URL']


authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version='2022-12-09',
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):
    """translating the english text to french"""
    translated_text = language_translator.translate(text = english_text, model_id='en-fr').get_result()
    #grabing just the translated text(string) form the object
    french_text = translated_text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """translating the frenchtext to english"""
    translated_text2 = language_translator.translate(text = french_text, model_id='fr-en').get_result()
    #grabing just the translated text(string) form the object
    english_text = translated_text2['translations'][0]['translation']
    return english_text
