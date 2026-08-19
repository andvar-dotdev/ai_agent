import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot write to "{target_file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_file_path):
            return f'Error: Cannot write to "{target_file_path}" as it is a directory'
        os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{target_file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"

schema_write_file: dict[str, str | dict[str, str | dict[str, str | list[str] | dict[str, dict[str, str]]]]] = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Overwrites the contents of the specified file relative to the working directory with the specified contents. If the file or parts of its parent directories don't exist, it creates them. If it succesfully runs, it returns a string stating so, else it returns a string with an error.",
        "parameters": {
            "type": "object",
            "required": ["file_path", "content"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file which is to be overwritten with the provided content, relative to the working directory"
                },
                "content": {
                    "type": "string",
                    "description": "This string contains the contents with which the function will overwrite the specified file's contents."
                }
            }
        }
    }
}
