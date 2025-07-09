import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    #toto je nastavenie suvisiace s API aktivacnym klucom
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    #toto je nastavenie suvisiace s so systemovymi argumentami ked spustam program cez konzolu
    arguments = sys.argv[1:]
    if '--verbose' in arguments:
        verbose_mode = True
        arguments.remove('--verbose')
    else:
        verbose_mode = False
        
    user_prompts = ' '.join(arguments)

    if not arguments:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompts)])]
    
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    prompts_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    print(response.text)

    if verbose_mode:
        print(f'User prompt: {user_prompts}')
        print(f'Prompt tokens: {prompts_tokens}')
        print(f'Response tokens: {response_tokens}')
    
if __name__ == '__main__':
    main()