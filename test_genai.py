import os
import toml
from google import genai
from google.genai import types

secrets = toml.load(".streamlit/secrets.toml")
client = genai.Client(api_key=secrets["GEMINI_API_KEY"])

config = types.GenerateContentConfig(
    system_instruction="You are an elite poet.",
    max_output_tokens=600,
    temperature=0.7,
    thinking_config=types.ThinkingConfig(include_thoughts=True)
)

try:
    print("Testing gemini-2.5-flash with thinking_config...")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Initialize the engine. Provide the first prompt and constraint using the required format.",
        config=config
    )
    print("Success!")
    print("Response text:", response.text)
except Exception as e:
    print(f"Error with 2.5: {e}")

try:
    print("Testing gemini-3.0-flash with thinking_config...")
    response = client.models.generate_content(
        model="gemini-3.0-flash",
        contents="Hello",
        config=config
    )
    print("Success!")
except Exception as e:
    print(f"Error with 3.0: {e}")
