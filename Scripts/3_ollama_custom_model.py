import ollama

modelfile = """
FROM llama3.2
SYSTEM You are a very smart assistant who knows everything about oceans
PARAMETER temperature 0.1
"""

ollama.create(model="ocean",system="You are a very smart assistant who knows everything about oceans",from_="llama3.2")

res = ollama.generate(model="ocean", prompt="Why is the ocean so salty?")
print(res["response"])

#To delete the model
ollama.delete("ocean")