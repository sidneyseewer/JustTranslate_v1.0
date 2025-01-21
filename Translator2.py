from transformers import MarianMTModel, MarianTokenizer
import os
import re

class Translator2():
    def __init__(self, language: str):
        self.language = language
        self.tokenizer, self.model = self.setup_tranlator2(language)

    # Send Text with auto listen bool
    def translate(self, text):
        # Tokenize the input text
        inputs = self.tokenizer.encode(text, return_tensors="pt")
        
        # Perform translation
        outputs = self.model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
        translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return translated_text
    
    # Speak Text
    def speak(self, text):
        pass
        # speak_text(text=text, lan=self.language)


    # Setup language
    def setup_tranlator2(self,target_language):
        model_name = f'en-{target_language}'
    #    model_dirs = re.compile(f"models/{model_name}/snapshots/")
        #model_dir = model_dirs[0]
        model_dir = f"./models/{model_name}/"
        
    #    snapshot_dir = os.listdir(model_dir)[0]
    #    model_dir = f"{model_dir}/{snapshot_dir}"
        if not os.path.exists(model_dir):
            print(f"Path does not exist, exiting: {model_dir}")
            exit()
        # Load the tokenizer and model from the local directory

    #    model_folders = re.compile(f"{model_dir}/*/snapshots/")
        snapshot_name = str(model_dir) + "snapshots/"
        next_dir = os.listdir(snapshot_name)[0]
        print(f"Model Name: {model_name}")
        model_dir = os.path.join(snapshot_name,next_dir)
#        model_dir = re.compile(f'{model_name}')
        print(f"Model Dir (re): {model_dir}")
        model_name = model_dir[0]
        print(f"Model Name: {model_name}")
        print(f"Model Dir (re): {model_dir}")
        tokenizer = MarianTokenizer.from_pretrained(model_dir)
        model = MarianMTModel.from_pretrained(model_dir)

        return tokenizer, model

#tokenizer_de, model_de = setup_tranlator("de")
#tokenizer_fr, model_fr = setup_tranlator("fr")
#tokenizer_es, model_es = setup_tranlator("es")
#tokenizer_ru, model_ru = setup_tranlator("ru")