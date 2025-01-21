
from transformers import MarianMTModel, MarianTokenizer
import os
import re
from Translator2 import Translator2

MODEL_DIR = "./models"

class Translator2():
    def __init__(self, language: str):
        self.language = language
        self.tokenizer, self.model = setup_tranlator(language)

    # Send Text with auto listen bool
    def translate(self, text):
        # Tokenize the input text
        inputs = self.tokenizer.encode(text, return_tensors="pt")
        
        # Perform translation
        outputs = self.model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text

# Setup all languages
def setup_tranlator(target_language: str):
    # model_name = f'opus-mt-en-{target_language}'
#    if target_language.startsWith(""):
#        pass
    model_name = f"en-{target_language}/"
 #   snapshot_dir = os.listdir(model_dir)[0]
 #   model_dir = f"{model_dir}/{snapshot_dir}"
    #model_regex = re.compile(f"{model_name}/*/snapshots/")
    model_path = f"{MODEL_DIR}/{model_name}"
    print(f"Model Paht: {model_path}")
    if not os.path.exists(model_path):
        print("Path does not exist, exiting.")
        exit()
    # Load the tokenizer and model from the local directory
    model_folders = re.compile(f"{model_path}/*/snapshots/")
    tokenizer = MarianTokenizer.from_pretrained(model_folders)
    model = MarianMTModel.from_pretrained(model_folders)
    return tokenizer, model

