import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

# loading my .env file
load_dotenv()

# loading and defining api_key variabele for my project prompts
api_key = os.environ.get('GEMINI_API_KEY')
if api_key is None:
    raise RuntimeError('API key was not found!')

# new instance of client form genai librabry
client = genai.Client(api_key=api_key)

def main():
    # create a parser object, define the arguments we want to accept, and then parse whatever arguments the user actually provided when they ran the script.
    # Now we can access `args.user_prompt`
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", help="Prompt for the model")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # creating a list of messages, which is the format that the genai library expects for conversations. 
    # Each message has a role (in this case, "user") and parts (which is a list of parts, where each part has text). 
    # In this case, we only have one part, which is the user's prompt.
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # first object of response from gemini LLM + my prompt
    # prompt = 'Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.' /not necesarry right now
    response = client.models.generate_content(model='gemini-2.5-flash', contents=messages, config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt, temperature=0,))

    if response.usage_metadata is None:
        raise RuntimeError('We are out of tokkens!')
    
    # spent tokens
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    
    if args.verbose:
        print(f'User prompt: {args.user_prompt}')
        print(f'Prompt tokens: {prompt_tokens}')
        print(f'Response tokens: {response_tokens}')
    
    # Initialize a list to store the results we get back from our functions
    function_results = []

    if response.function_calls:
        for function_call in response.function_calls:
            # 10. Use call_function instead of just printing the name
            function_call_result = call_function(function_call, verbose=args.verbose)

            # 10.1. Check that we actually got parts back
            if not function_call_result.parts:
                raise Exception("Function call result has no parts")

            # 10.2. & 10.3. Validate the response structure
            # We look at the first part returned by call_function
            part = function_call_result.parts[0]
            if part.function_response is None:
                raise Exception("Function response is missing")
            if part.function_response.response is None:
                raise Exception("Function response data is missing")

            # 10.4. Save the part so we can use it later
            function_results.append(part)

            # 10.5. If verbose, print the actual result dictionary
            if args.verbose:
                print(f"-> {part.function_response.response}")
    else:
        print(f'Response:\n{response.text}')
    
if __name__ == "__main__":
    main()