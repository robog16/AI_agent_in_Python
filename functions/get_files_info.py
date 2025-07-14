import os
from google.genai import types 

def get_files_info(working_directory, directory=None):
    abs_path_directory = os.path.abspath((os.path.join(working_directory, directory)))
    abs_path_work_directory = os.path.abspath(working_directory)

    if not abs_path_directory.startswith(abs_path_work_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    elif not os.path.isdir(abs_path_directory):
        return f'Error: "{directory}" is not a directory'

    else:
        try:
            tempor_list = []
            directory_content_list = os.listdir(abs_path_directory)
            for i in directory_content_list:
                current_file_path = os.path.join(abs_path_directory, i)
                partial_string = f'- {i}: file_size={os.path.getsize(current_file_path)} bytes, is_dir={os.path.isdir(current_file_path)}'
                tempor_list.append(partial_string)
            final_string = ('\n').join(tempor_list)
            return final_string
        
        except Exception as e:
            return f'Error {e} occured'

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)