import os
import shutil

def list_files(directory: str) -> list[str]:
    """Return a list of file names."""
    print(f"[Agent Call] list_files(directory={directory!r})")
    try:
        return os.listdir(directory)
    except Exception as e:
        return [f"Error listing files: {e}"]

def show_file_content(filepath: str) -> str:
    """Return the full content of the specified file as a string."""
    print(f"[Agent Call] show_file_content(filepath={filepath!r})")
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


def rename_file(old_name: str, new_name: str) -> str:
    """Rename a file from old_name to new_name."""
    print(f"[Agent Call] rename_file(old_name={old_name!r}, new_name={new_name!r})")
    try:
        os.rename(old_name, new_name)
        return f"Renamed '{old_name}' to '{new_name}'"
    except Exception as e:
        return f"Error renaming file: {e}"

def delete_file(filepath: str) -> str:
    """Delete the specified file."""
    print(f"[Agent Call] delete_file(filepath={filepath!r})")
    try:
        os.remove(filepath)
        return f"Deleted file: {filepath}"
    except Exception as e:
        return f"Error deleting file: {e}"

def create_file(filepath: str, content: str = "") -> str:
    """Create a new file with optional content."""
    print(f"[Agent Call] create_file(filepath={filepath!r}, content=<length {len(content)}>)")
    try:
        with open(filepath, 'w') as f:
            f.write(content)
        return f"Created file: {filepath}"
    except Exception as e:
        return f"Error creating file: {e}"

def append_to_file(filepath: str, content: str) -> str:
    """Append content to an existing file."""
    print(f"[Agent Call] append_to_file(filepath={filepath!r}, content=<length {len(content)}>)")
    try:
        with open(filepath, 'a') as f:
            f.write(content)
        return f"Appended content to: {filepath}"
    except Exception as e:
        return f"Error appending to file: {e}"

def move_file(src: str, dst: str) -> str:
    """Move a file from src to dst."""
    print(f"[Agent Call] move_file(src={src!r}, dst={dst!r})")
    try:
        shutil.move(src, dst)
        return f"Moved file from '{src}' to '{dst}'"
    except Exception as e:
        return f"Error moving file: {e}"

def file_exists(filepath: str) -> bool:
    """Check if a file exists."""
    print(f"[Agent Call] file_exists(filepath={filepath!r})")
    return os.path.isfile(filepath)

def create_folder(folder_path: str) -> str:
    """Create a new folder (directory) at the specified path."""
    print(f"[Agent Call] create_folder(folder_path={folder_path!r})")
    try:
        os.makedirs(folder_path, exist_ok=True)
        return f"Folder created: {folder_path}"
    except Exception as e:
        return f"Error creating folder: {e}"

def copy_file(src: str, dst: str) -> str:
    """Copy a file from src to dst."""
    print(f"[Agent Call] copy_file(src={src!r}, dst={dst!r})")
    try:
        shutil.copy2(src, dst)
        return f"Copied file from '{src}' to '{dst}'"
    except Exception as e:
        return f"Error copying file: {e}"