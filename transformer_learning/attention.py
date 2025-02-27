import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
import torch

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# Determine if MPS is available
if torch.backends.mps.is_available():
    device = "mps"
    print("Using MPS device")
else:
    device = "cpu"
    print("MPS not available, using CPU")

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map=device,  # Use the determined device
    torch_dtype="auto",
    trust_remote_code=True,
    # attn_implementation='eager' # Remove this line to allow MPS to use optimized attention
)

# Create a pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=50,
    do_sample=False,
    device=device # Pass the device to the pipeline
)

prompt = "Write an enmail apologizing to Sarah for the tragic gardening mishap.Explain how it happened."
output = generator(prompt)
print(output[0]['generated_text'])