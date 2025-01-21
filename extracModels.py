from transformers import MarianMTModel, MarianTokenizer
import torch
from pathlib import Path
import os

# Load the model and tokenizer
model_name = "./models/en-de"  # Replace with your desired MarianMT model
snapshot_name = str(model_name) + "/snapshots/"
next_dir = os.listdir(snapshot_name)[0]
new_dir = os.path.join(snapshot_name,next_dir)
print(f"Model Name: {new_dir}")
model = MarianMTModel.from_pretrained(new_dir)
tokenizer = MarianTokenizer.from_pretrained(new_dir)
print(f"Loaded model and tokenizer")
# Example input text
text = "Hello, how are you?"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Define dynamic axes for ONNX (allow variable input and output sizes)
dynamic_axes = {
    "input_ids": {0: "batch_size", 1: "sequence_length"},
    "attention_mask": {0: "batch_size", 1: "sequence_length"},
    "logits": {0: "batch_size", 1: "sequence_length"},
}

# Export the model to ONNX
print(f"Exporting now")
onnx_path = "marianmt.onnx"
onnx_path = ".output/models/"+str(onnx_path)
torch.onnx.export(
    model, 
    (inputs["input_ids"], inputs["attention_mask"]),  # Model inputs
    onnx_path, 
    input_names=["input_ids", "attention_mask"], 
    output_names=["logits"],  # Model output
    dynamic_axes=dynamic_axes, 
    opset_version=12  # ONNX opset version
)

print(f"Model successfully exported to {onnx_path}")
