import os
import sys
from google import genai
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    arguments = sys.argv[1:]
    user_prompts = ' '.join(arguments)

    if not arguments:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=user_prompts)

    print(f'Prompt tokens: {response.usage_metadata.prompt_token_count}')
    print(f'Response tokens: {response.usage_metadata.candidates_token_count}')
    print('Response:')
    print(response.text) 

if __name__ == '__main__':
    main()