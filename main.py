import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = genai.Client(api_key = api_key)

model = "gemini-2.5-flash"
contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

def main():
    print(client.models.generate_content(model=model, contents=contents).text)


if __name__ == "__main__":
    main()
