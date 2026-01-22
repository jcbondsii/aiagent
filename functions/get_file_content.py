import os
from config import *

def get_file_content(working_directory, file_path):
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs:
        valid_target_file = target_file.startswith(working_dir_abs) 
    else: 
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory.'
    if not valid_target_file or not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}".'
        
    with open(target_file, 'r') as file:
        content = file.read(MAX_CHARS) #read up to the max characters
        if file.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'#check if there's more content
    
    return content