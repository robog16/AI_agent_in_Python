def get_files_info(working_directory, directory=None):
    abs_path_directory = os.path.abspath((os.path.join(working_directory, directory)))
    abs_path_work_directory = os.path.abspath(working_directory)

    if not abs_path_directory.startswith(abs_path_work_directory):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

    if not os.path.isdir(abs_path_directory):
        print(f'Error: "{directory}" is not a directory')

    else:
        directory_content = os.listdir(directory)
        final_string = f'- README.md: file_size=1032 bytes, is_dir=False\n- src: file_size=128 bytes, is_dir=True\n- package.json: file_size=1234 bytes, is_dir=False'
