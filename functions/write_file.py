import os
from google import genai
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites the content of a specified file within the working directory. It automatically creates any missing parent directories.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'working_directory': types.Schema(
                type=types.Type.STRING,
                description="The path to the permitted root directory where the agent is allowed to write.",
            ),
            'file_path': types.Schema(
                type=types.Type.STRING,
                description="The path to the file to be written, relative to the working directory.",
            ),
            'content': types.Schema(
                type=types.Type.STRING,
                description="The string content to be written into the file. This will replace any existing content.",
            )
        },
        required = ['working_directory', 'file_path', 'content']
    )
)

def write_file(working_directory, file_path, content):
    try:
        # getting absolut path to working_directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # getting path and normalize path of file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. is file within a working_directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # 4. if directory is really a directory not a file
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Vytvoríme priečinky, ak neexistujú, Ak už existujú, exist_ok=True zabráni vyhodeniu chyby
        # Získame cestu k nadradenému priečinku
        directory = os.path.dirname(target_file)
        os.makedirs(directory, exist_ok=True)
        
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
     
    except Exception as e:
        # 7. Zachytenie chýb a ich vrátenie ako text pre LLM
        return f"Error: {str(e)}"
        