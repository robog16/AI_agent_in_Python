import os

def write_file(working_directory, file_path, content):  
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    work_dir_abs_path = os.path.abspath(working_directory)

    if os.path.commonpath([abs_file_path, work_dir_abs_path]) != work_dir_abs_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
    try:
        os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: {e}'