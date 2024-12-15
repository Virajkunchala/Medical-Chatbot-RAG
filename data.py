
import os

from llama_index.llms.gemini import Gemini

os.environ["GOOGLE_API_KEY"] = os.environ["GOOGLE_API_KEY"]

llm = Gemini(
    model="models/gemini-1.5-flash",
)
resp = llm.complete("Write a poem about the secret book")
print(resp)
