import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # This is optional; by default, it reads from env

# Generate a chat completion
chat_completion = OpenAI().chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "generate one word",
        }
    ],
)

# Print the AI's response
print(chat_completion.choices[0].message.content)
