"""
Translator module
"""
import os
# import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ["apikey"]
url = os.environ["url"]

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator
)

language_translator.set_service_url(url)


def english_to_french(english_text):
    """
    English to French translator
    """
    if len(english_text) < 1:
        return ""
    french_trans = language_translator.translate(
        text=english_text, model_id="en-fr"
    ).get_result()
    french_text = french_trans["translations"][0]["translation"]
    return french_text


# print(english_to_french("i love you"))


def french_to_english(french_text):
    """
    French to English translator
    """
    if len(french_text) < 1:
        return ""
    english_translation = language_translator.translate(
        text=french_text, model_id="fr-en"
    ).get_result()
    english_text = english_translation["translations"][0]["translation"]
    return english_text


# print(french_to_english("Je t'aime"))

#  f2e_translator_function = ss
