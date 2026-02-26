import os
from dotenv import load_dotenv
from google import genai

# loading my .env file
load_dotenv()

# loading and defining api_key variabele for my project prompts
api_key = os.environ.get('GEMINI_API_KEY')
if api_key is None:
    raise RuntimeError('API key was not found!')

# new instance of client form genai librabry
client = genai.Client(api_key=api_key)

# first object of response from gemini LLM + my prompt
prompt = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.'
response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)

# spent tokens
prompt_tokens = response.usage_metadata.prompt_token_count
response_tokens = response.usage_metadata.candidates_token_count


def main():
    if response.usage_metadata is not None:
        print(f'User prompt: {prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
        print(f'Response:\n{response.text}')

    else:
        raise RuntimeError('We are out of tokkens!')

if __name__ == "__main__":
    main()
