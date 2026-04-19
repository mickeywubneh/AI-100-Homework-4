from google import genai
import os

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
#Input 1: Explain why Python is good for beginners.
#Input 2: Explain what an API is.
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain what an API is."
)

print(response)
