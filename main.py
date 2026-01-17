import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client = genai.Client(api_key = api_key)

model = "gemini-2.5-flash"
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type = str, help="User prompt")
#argument to enable verbose output
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()


#used for single prompt input
contents = args.user_prompt
#used for multiple prompt input
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

cmg_c = client.models.generate_content(model=model, contents=messages)
text = cmg_c.text
x = cmg_c.usage_metadata.prompt_token_count
y = cmg_c.usage_metadata.candidates_token_count

def main():
    if args.verbose:
        print(f"User prompt: {contents}\nPrompt tokens: {x}\nResponse tokens: {y}\nResponse: {text}")
    else:
        print(f"Response: {text}")


if __name__ == "__main__":
    main()
