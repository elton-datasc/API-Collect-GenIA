
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

def load_llm(model_name="mistralai/Mistral-7B-Instruct-v0.1", device="cpu"):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map=device, trust_remote_code=True)
    generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
    return generator
