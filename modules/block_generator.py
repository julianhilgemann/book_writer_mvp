# block_generator.py (Generates specific blocks within chapters)
def generate_block(block_description, word_count):
    prompt = generate_prompt("block_prompt", block_description=block_description, word_count=word_count)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]