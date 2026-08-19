import os

from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_file_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{target_file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{target_file_path}"'
        with open(target_file_path, "r") as f:
            file_content: str = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{target_file_path}" truncated at {MAX_CHARS} characters]'
        return file_content

    except Exception as e:
        return f"Error: {e}"

schema_get_file_content: dict[str, str | dict[str, str | dict[str, str | list[str] | dict[str, dict[str, str]]]]] = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns the concatenated contents of the file in the specified file path relative to the working directory, up to a maximum of 10000 characters. After 10000 characters, the content is truncated and replaced with a message stating that the rest of the content has been truncated",
        "parameters": {
            "type": "object",
            "required": ["file_path"],
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file which contents are to be concatenated, relative to the working directory"
                }
            }
        }
    }
}
