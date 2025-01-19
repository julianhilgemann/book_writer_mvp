import openai

# Replace this with your OpenAI API key
OPENAI_API_KEY = "your-openai-api-key"

# Set up the OpenAI client
openai.api_key = OPENAI_API_KEY

# Define a simple prompt
prompt = "Tell me a short fun fact about space."

# Call OpenAI's ChatCompletion API
response = openai.ChatCompletion.create(
    model="gpt-4",  # Or "gpt-3.5-turbo"
    messages=[{"role": "user", "content": prompt}]
)

# Extract and print the generated text
generated_text = response["choices"][0]["message"]["content"]
print("\nGenerated Text:\n", generated_text)
