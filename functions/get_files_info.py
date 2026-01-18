import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    if os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs:
        valid_target_dir = target_dir.startswith(working_dir_abs) 
    else: 
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory.'
    if not valid_target_dir:
        return f'Error: "{directory}" is not a directory.'
    
    files_info = ""
    for entry in os.listdir(target_dir):
        entry_path = os.path.join(target_dir, entry)
        if os.path.isfile(entry_path):
            file_info = "- "+ entry + ": file_size=" + str(os.path.getsize(entry_path)) + " bytes, is_dir=False"
        elif os.path.isdir(entry_path):
            file_info = "- "+ entry + ": file_size=" + str(os.path.getsize(entry_path)) + " bytes, is_dir=True"
            
            #file_info = {
             #   "name": entry,
              #  "size": os.path.getsize(entry_path),
               # "is_dir": os.path.isdir(entry_path)
            #}
        files_info += file_info + "\n"
    return files_info