import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role":"user","content":"Why is the sky blue?"},
    ]
)
print(response["message"]["content"])

#Example 2
"""
res = ollama.generate(
    model="llama3.2",
    prompt="Why is the ocean so salty?"
)
print(ollama.show("llama3.2"))
"""