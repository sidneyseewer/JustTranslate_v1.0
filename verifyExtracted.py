import onnxruntime
import numpy as np

# Load the ONNX model
onnx_model = onnxruntime.InferenceSession("marianmt.onnx")

# Tokenize the input
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

# Prepare ONNX inputs
onnx_inputs = {
    "input_ids": inputs["input_ids"].cpu().numpy(),
    "attention_mask": inputs["attention_mask"].cpu().numpy(),
}

# Run the model
onnx_outputs = onnx_model.run(None, onnx_inputs)

# Get logits
logits = onnx_outputs[0]
print("ONNX Output Shape:", logits.shape)

# Decode the output (if needed)
decoded = tokenizer.decode(np.argmax(logits, axis=2).squeeze())
print("Translated Text:", decoded)
