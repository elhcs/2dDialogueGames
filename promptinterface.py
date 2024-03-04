import openai

# Set your API key
openai.api_key = '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'

# Function to list available engines
def list_engines():
    engines = openai.Engine.list()
    #for engine in engines.data:
        #print(f"Engine: {engine['id']}")

# Function to generate text
def generate_text(prompt, max_tokens=100, temperature=0.7):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=temperature
    )
    return response['choices'][0]['message']['content'].strip()


# Example of listing engines
list_engines()

# Example prompt
prompt = "dialogue between batman and superman"

# Generate text using the selected engine
generated_text = generate_text(prompt)
generated_text = generated_text.split('\n\n')

print("Generated Text:")
print(generated_text)
