import os

import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize model (using Gemini Pro)
model = genai.GenerativeModel("gemini-pro")

# Generate content
response = model.generate_content("Write a hello world program in Python")

# Print response
print(response.text)

# Chat example
chat = model.start_chat()
response = chat.send_message("What is artificial intelligence?")
print(response.text)
