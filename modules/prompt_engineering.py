# prompt_engineering.py (Constructs structured prompts)
def generate_prompt(prompt_type, **kwargs):
    prompts = load_prompts()
    return prompts[prompt_type].format(**kwargs)