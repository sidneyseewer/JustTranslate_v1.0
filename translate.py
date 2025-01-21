from Translator_mock import *
#from Translator import *
from Translator2 import *
import argparse
import os
from datetime import datetime

OUTPUT_FOLDER = "./output"
INPUT_FOLDER = ""

def main():
    print(f"Starting Translation")
        # Create argument parser
    parser = argparse.ArgumentParser(description="Just Translate")

    # Add arguments
    parser.add_argument("-i", "--input", required=False,default=f"{INPUT_FOLDER}/test_EN_DE.txt", help="Path to the input file")
    parser.add_argument("-l", "--language", required=True, default="de", help="Language to translate to")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-t", "--text", required=False, default="", help="Text to translate")

    # Parse the arguments
    args = parser.parse_args()

    # Access arguments
    input_path = args.input
    output_path = OUTPUT_FOLDER
    language = args.language
    verbose = args.verbose
    text = args.text



    # Use the arguments in your program logic
    ts = str(datetime.now().strftime("%Y%m%d_%H%M%S"))  
    sub_folder = ""
    print(f"Input Path: {input_path}\nInput: {input}")
    if text == "":
        sub_folder = "list"
    else:
        sub_folder = "text"
    output_path = f"{OUTPUT_FOLDER}/{sub_folder}/{language}/{ts}.txt"
    create_text_file(output_path)
    if verbose and text == "":
        print(f"Input file: {input_path}")
    print(f"Output file: {output_path}")

    if not(text==""):
        translation = translate_text(text=text, lan=language)
        if not save_result(output_file_path=output_path,response=translation):
            print("Error saving output file")
    else:
        translate_file(input_path=input_path,language=language,output_path=output_path)

    # TODO: Save responses into specific langauge folder and clean up single translation more than 10

def translate_text(text: str, lan: str)-> str:
    print(f"Inside Translate_text function")
    translator = Translator2(language=lan)
    result = translator.translate(text=text)
    print(f"{text} in {lan} is: {result}")
    return str(result)

def translate_file(input_path: str, language: str, output_path: str):
    # Your program logic here
    print(f"Processing file {input_path}...")
    lines = separate_file(input_file_path=input_path)
    if lines == []:
#        save_result(output_file_path=output_path,response=f"Input file Empty or Nonexistant{input_path}")
        save_result(output_file_path=output_path)
    translator = Translator2(language=language)
    for i in range(len(lines)):
        print(f"{i+1}: DE: {lines[i]}")
        translation = translator.translate(lines[i])
        if not save_result(output_file_path=output_path,response=translation):
            print("Error saving output file")

    if output_path:
        print(f"Results will be saved to {output_path}")
    else:
        print("No output file specified.")

def create_text_file(file_path):
    """Create a text file with the specified content. Overwrites if it exists."""
    try:
        # Create dirs
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:  # 'w' mode creates or overwrites the file
            file.write("")
        print(f"File created: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_result(output_file_path: str, response: str) -> bool:
    if not output_file_path:
        return False
           
    try:
        with open(output_file_path, 'a') as file:  # 'a' mode opens the file for appending
            file.write(response + '\n')  # Add the line with a newline character
        print(f"Line added to {output_file_path}")
        return True
    except Exception as e:
        print(f"An error occurred when saving results: {e}")
        return False

def separate_file(input_file_path: str) -> []: 
    if not (os.path.exists(input_file_path)):
        print(f"Error with file path: {input_file_path}")
        return []
    try:
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        print(f"Lines:{lines}")
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{input_file_path}' does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred({input_file_path}): {e}")
        return []



if __name__ == "__main__":
    main()