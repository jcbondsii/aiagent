import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        # Resolve absolute paths
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        # Security check to ensure the file is within the working directory
        if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: File "{file_path}" does not exist or is not a regular file'
        if file_path.endswith('.py') is False:
            return f'Error: File "{file_path}" is not a Python file'
        
        # Execute the Python file        
        command = ["python", abs_file_path]

        if args:
            command.extend(args)
        completed = subprocess.run(command, capture_output=True, text=True, cwd=abs_working_dir, timeout=30)

        if completed.returncode != 0:
            return f'Error: Execution of file "{file_path}" failed with return code {completed.returncode}'
        elif completed.stdout  == None and completed.stderr == None:
            return f'Error: No output captured from execution of file "{file_path}"'
        else:
            return f'STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}'
    except Exception as e:
        return f'Error executing file "{file_path}": {e}'