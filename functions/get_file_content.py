import os
from config import MAX_CHARS
from google import genai
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory. The content is returned as a string.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            )
        },
        required = ['file_path']
    )
)

def get_file_content(working_directory, file_path):
    try:
        # getting absolut path to working_directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # getting path and normalize path of file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. is file within a working_directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # 4. if directory is really a directory not a file
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # final string
        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        # returning one final multiline string
        return file_content_string
        
    except Exception as e:
        # 7. Zachytenie chýb a ich vrátenie ako text pre LLM
        return f"Error: {str(e)}"
