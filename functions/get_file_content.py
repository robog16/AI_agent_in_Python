import os
from config import MAX_CHARS

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
                
                

                
                
                
            
        
        
        
