from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info, get_files_info
from functions.get_file_content import schema_get_file_content, get_file_content
from functions.write_file import schema_write_file, write_file
from functions.run_python_file import schema_run_python_file, run_python_file


# Definícia nástrojov, ktoré môže model volať pri riešení úloh.
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
)

# Mapovanie názvov funkcií na ich implementácie v Pythone.
function_map = {
    "get_files_info": get_files_info,
    'get_file_content': get_file_content,
    'write_file': write_file,
    'run_python_file': run_python_file
    }

# Táto funkcia zabalí volanie nástroja do formátu, ktorý rozumie Gemini API.
def call_function(function_call, verbose=False):
    
    # V prípade detailného režimu sa vypíše, ktorý nástroj sa volá.
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    else:
        print(f" - Calling function: {function_call.name}")

    # Bezpečne získame názov funkcie z volania modelu.
    function_name = function_call.name or ""

    # Check if the name exists in the map
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    
    # Argumenty z modelu sa prevedú do slovníka a doplní sa povolený pracovný adresár.
    args = dict(function_call.args) if function_call.args else {}

    args['working_directory'] = './calculator'

    function_result = function_map[function_name](**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )



    