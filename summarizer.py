from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Use the version fine-tuned for summarization
model_name = "Salesforce/codet5-base-multi-sum"
# model_name = "Salesforce/codet5-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def summarize_code(code_snippet):
    """Generate a natural language summary for the given code snippet."""
    input_text = f"summarize: {code_snippet.strip()}"
    inputs = tokenizer(
        input_text,
        return_tensors="pt",
        max_length=512,
        padding="max_length",
        truncation=True
    )
    outputs = model.generate(
        inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=64,
        num_beams=5,
        length_penalty=2.0,
        early_stopping=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# def summarize_code(code_snippet):
#     """Generate a more detailed natural language summary."""
#     input_text = f"Explain in detail what the following code does:\n{code_snippet.strip()}"
#     inputs = tokenizer(
#         input_text,
#         return_tensors="pt",
#         max_length=512,
#         padding="max_length",
#         truncation=True
#     )
#     outputs = model.generate(
#         inputs["input_ids"],
#         attention_mask=inputs["attention_mask"],
#         max_length=128,
#         num_beams=5,
#         length_penalty=1.5,
#         early_stopping=True
#     )
#     return tokenizer.decode(outputs[0], skip_special_tokens=True)
