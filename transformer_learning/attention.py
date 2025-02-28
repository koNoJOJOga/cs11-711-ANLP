import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer, pipeline, AutoModelForCausalLM
import torch

# load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# Force CPU usage
device = "cpu"
print("Using CPU device")

model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map=device,
    torch_dtype="auto",
    trust_remote_code=True
)

# Create a pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=50,
    do_sample=False
)

prompt = "Write an enmail apologizing to Sarah for the tragic gardening mishap.Explain how it happened."
output = generator(prompt)
print(output[0]['generated_text'])