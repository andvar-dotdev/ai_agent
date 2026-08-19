import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_file_path]
        if args != None:
            command.extend(args)
        result = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        if not result.stderr and not result.stdout:
            return f"No output produced"
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file: dict[str, str | dict[str, str | dict[str, str | list[str] | dict[str, dict[str, str | dict[str, str]]]]]] = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs the specified python executable relative to the working directory with provided arguments (if provided). It then returns the outputs of STDOUT and STDERR. Should the result give a returncode other than zero, then the non-zero return code is also provided.",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the executable python file which is to be run, relative to the working directory"
                },
                "args": {
                    "type": "array",
                    "description": "List containing strings of the arguments to be passed to the function that is to be run. This object defaults to None if it is not provided.",
                    "items": {
                        "type": "string"
                    }
                }
            }
        }
    }
}
