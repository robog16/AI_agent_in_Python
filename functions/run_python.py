import subprocess
import os

def run_python_file(working_directory, file_path):
    if os.path.isabs(file_path):
        abs_file_path = os.path.abspath(file_path)
    else:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    work_dir_abs_path = os.path.abspath(working_directory)

    if os.path.commonpath([abs_file_path, work_dir_abs_path]) != work_dir_abs_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    elif not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    elif not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        command = ['python3', abs_file_path]
        result = subprocess.run(
            command,
            cwd=work_dir_abs_path,
            capture_output=True,  
            text=True,       
            timeout=30,          
            check=False          
        )
                                    
        output_parts = []
        output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
        output_parts.append(f"STDERR:\n{result.stderr.strip()}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if result.stdout.strip() == '' and result.stderr.strip() == '' and result.returncode == 0:
            return 'No output produced.'
        else:
            return "\n".join(output_parts)

    except Exception as e:
        return f'Error: executing Python file: {e}'
        

    


    
