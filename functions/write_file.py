import os
from google import genai
from google.genai import types

# Definícia nástroja pre model: umožní mu prepísať obsah súboru v povolenom adresári.
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

# Implementácia zápisu do súboru: vytvorí chýbajúce priečinky a zapíše obsah do cieľového súboru.
def write_file(working_directory, file_path, content):
    try:
        # Prevedie pracovný adresár na absolútnu cestu pre zápisom.
        working_dir_abs = os.path.abspath(working_directory)
        
        # Vytvorí cieľovú cestu k súboru a normalizuje ju.
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Zabráni zápisu mimo povoleného priestoru.
        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # Zamedzí zápis do adresára, keď sa očakáva súbor.
        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Vytvorí chýbajúce priečinky, ak cieľový súbor ešte neexistuje.
        directory = os.path.dirname(target_file)
        os.makedirs(directory, exist_ok=True)
        
        # Zapíše nový obsah do súboru a vrátí informáciu o úspechu.
        with open(target_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
     
    except Exception as e:
        # 7. Zachytenie chýb a ich vrátenie ako text pre LLM
        return f"Error: {str(e)}"
        