
import os

from llama_index.llms.gemini import Gemini

GOOGLE_API_KEY = "AIzaSyAk7npVIB2Eq2VjFcWj7LiHAqHVudksCQI"  # add your GOOGLE API key here
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

llm = Gemini(
    model="models/gemini-1.5-flash",
)
resp = llm.complete("Write a poem about the secret book")
print(resp)
