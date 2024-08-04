import os

def check_file_permissions(file_path):
    """Checks if a file has read and write permissions.

    Args:
        file_path: The path to the file.

    Returns:
        A tuple of booleans (read_access, write_access).
    """

    read_access = os.access(file_path, os.R_OK)
    write_access = os.access(file_path, os.W_OK)

    return read_access, write_access

# Example usage
file_path = "example.txt"
read, write = check_file_permissions(file_path)

print(f"File: {file_path}")
print(f"Read access: {read}")
print(f"Write access: {write}")