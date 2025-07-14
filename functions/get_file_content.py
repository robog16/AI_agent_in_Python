import os
from config import MAX_CHARS
from google.genai import types

def get_file_content(working_directory, file_path):
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    work_dir_abs_path = os.path.abspath(working_directory)

    if not abs_file_path.startswith(work_dir_abs_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    elif not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    else:
        try:    
            with open(abs_file_path, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                extra = f.read(1)
                if extra:
                    # znak navyše existuje, viem že bol súbor dlhší
                    file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'
            
            return file_content_string
        
        except Exception as e:
            return f'Error: {e}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f'Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.',
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            'file_path': types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory."
            )
        },
        required = ['file_path']
    )
)
                
                

                
                
                
            
        
        
        
