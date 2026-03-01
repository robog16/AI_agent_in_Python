import os

def get_files_info(working_directory, directory="."):
    try:
        # getting absolut path to working_directory
        working_dir_abs = os.path.abspath(working_directory)
        
        # getting path and normalize path of target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        # 3. is directory within a working_directory
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # 4. if directory is really a directory not a file
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        # final string
        items = os.listdir(target_dir)
        lines = []
        for item in items:
            # need to connect path to get metadata of files in target directory
            item_path = os.path.join(target_dir, item)
            size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            lines.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")

        # returning one final multiline string
        return "\n".join(lines)

    except Exception as e:
        # 7. Zachytenie chýb a ich vrátenie ako text pre LLM
        return f"Error: {str(e)}"