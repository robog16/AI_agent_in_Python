import os

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
        