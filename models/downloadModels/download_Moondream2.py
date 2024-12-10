from transformers import AutoModelForCausalLM, AutoTokenizer

# Set up the model and tokenizer
model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

print("\n==SUCCESS==\n")