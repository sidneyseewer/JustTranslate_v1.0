


languages = ["de", "fr", "es", "ru", "en"]

def translate(text: str, lan: str):
    if not text:
        return "Error: Text is None"
    if not lan:
        return "Error: Lan and Text is None"
    if lan in languages:
        return f"Guten Tag! ({lan})"
    return "Error Traslate Fuction"

def test_translate():
    lan = "de"
    text = "Good Morning"
    print(f"Sending: {lan}, {text}")
    t_text = translate(text=text, lan=lan)
    print(f"Translation: {t_text}")
    
    
    
def main():
    print("Translator mock starting.")
    test_translate()
    
if __name__ == "__main__":
    main()



