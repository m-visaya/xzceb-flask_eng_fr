import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_translator_instance():
    global translator

    authenticator = IAMAuthenticator(apikey)
    translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    translator.set_service_url(url)

def english_to_french(english_text):
    if not english_text:
        return None
    res = translator.translate(text=english_text, model_id='en-fr').get_result()
    translations = res['translations']
    french_text = translations[0]['translation']
    return french_text

def french_to_english(french_text):
    if not french_text:
        return None
    res = translator.translate(text=french_text, model_id='fr-en').get_result()
    translations = res['translations']
    english_text = translations[0]['translation']
    return english_text

create_translator_instance()
