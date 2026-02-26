import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# loading my .env file
load_dotenv()

# loading and defining api_key variabele for my project prompts
api_key = os.environ.get('GEMINI_API_KEY')
if api_key is None:
    raise RuntimeError('API key was not found!')

# new instance of client form genai librabry
client = genai.Client(api_key=api_key)

# create a parser object, define the arguments we want to accept, and then parse whatever arguments the user actually provided when they ran the script.
# Now we can access `args.user_prompt`
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

# creating a list of messages, which is the format that the genai library expects for conversations. 
# Each message has a role (in this case, "user") and parts (which is a list of parts, where each part has text). 
# In this case, we only have one part, which is the user's prompt.
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# first object of response from gemini LLM + my prompt
# prompt = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.' /not necesarry right now
response = client.models.generate_content(model='gemini-2.5-flash', contents=messages)

# spent tokens
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count


def main():
    if response.usage_metadata is not None:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
        print(f'Response:\n{response.text}')

    else:
        raise RuntimeError('We are out of tokkens!')

if __name__ == "__main__":
    main()
