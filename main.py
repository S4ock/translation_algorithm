from googletrans import Translator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import pyttsx3
# Language codes and names
LANGUAGES = {
    'en': 'English',
    'fr': 'French',
    'ro': 'Romanian',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'nl': 'Dutch',
    'ru': 'Russian',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'ar': 'Arabic',
    'tr': 'Turkish',
    'sv': 'Swedish',
    'da': 'Danish',
    'fi': 'Finnish',
    'no': 'Norwegian',
    'pl': 'Polish',
    'el': 'Greek'
}

def text_to_speech(text, lang='en'):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def display_language_list():
    print("Available languages:")
    for code, name in LANGUAGES.items():
        print(f"{code}: {name}")

def main():
    # Display available languages
    display_language_list()

    # Create a Translator instance
    translator = Translator()

    # Input text and target language
    texts = input("Write what you want to translate: ").strip()
    if not texts:
        print("No text provided for translation.")
        return

    langs = input("Write what language you want to translate to (e.g., 'fr' for French): ").strip()
    if not langs:
        print("No target language provided.")
        return

    if langs not in LANGUAGES:
        print("Invalid language code provided. Please use a valid language code.")
        return

    # Detect the language of the input text
    try:
        detected_lang = detect(texts)
        detected_lang_name = LANGUAGES.get(detected_lang, "Unknown")
    except LangDetectException:
        print("Could not detect the language. Please ensure your text is valid.")
        return

    # Translate the entire text
    try:
        translation = translator.translate(texts, src=detected_lang, dest=langs).text
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return

    # Print the original text, detected language, and translated text
    print(f"\nOriginal Text: {texts}")
    print(f"Original Text Language: {detected_lang_name} ({detected_lang})")
    print(f"Translated Text: {translation}")

    # Convert translated text to speech
    if input("\nWould you like to hear the translated text? (yes/no): ").strip().lower() == 'yes':
        text_to_speech(translation, langs)

if __name__ == "__main__":
    main()
