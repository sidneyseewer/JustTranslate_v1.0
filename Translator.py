
from transformers import MarianMTModel, MarianTokenizer
import os

class Translator():
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
def setup_tranlator(target_language):
    # model_name = f'opus-mt-en-{target_language}'
    model_dir = f"models/opus-mt-en-{target_language}/snapshots"
    snapshot_dir = os.listdir(model_dir)[0]
    model_dir = f"{model_dir}/{snapshot_dir}"
    if not os.path.exists(model_dir):
        print("Path does not exist, exiting.")
        exit()
    # Load the tokenizer and model from the local directory
    tokenizer = MarianTokenizer.from_pretrained(model_dir)
    model = MarianMTModel.from_pretrained(model_dir)
    return tokenizer, model

