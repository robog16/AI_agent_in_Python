import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        # getting absolut path to working_directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # getting path and normalize path of file
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. is file within a working_directory
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 4. if file is really a file not a directory or if even exists
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        # if file ends with .py
        if not target_file.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        # using a subprocess to run the file
        command = ["python", target_file]
        if args:
            command.extend(args)

        process = subprocess.run(command, capture_output=True, text=True, cwd=working_dir_abs, timeout=30)

        output_string = ''
        if process.returncode != 0:
            output_string += f"Process exited with code {process.returncode}\n"
        if not process.stdout and not process.stderr:
            output_string += "No output produced\n"
        else:
            if process.stdout:
                output_string += f'STDOUT:\n{process.stdout}\n'
            if process.stderr:
                output_string += f'STDERR:\n{process.stderr}'
        
        return output_string
    
    except Exception as e:
        # 7. Zachytenie chýb a ich vrátenie ako text pre LLM
        return f"Error: executing Python file: {e}"