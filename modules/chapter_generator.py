# chapter_generator.py (Handles chapter-wise text generation)
import openai
from langchain import PromptTemplate

def generate_chapter(chapter_title, blocks):
    responses = []
    for block in blocks:
        prompt = generate_prompt("block_prompt", block_description=block["description"], word_count=block["word_count"])
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}]
        )
        responses.append(response["choices"][0]["message"]["content"])
    return "\n".join(responses)