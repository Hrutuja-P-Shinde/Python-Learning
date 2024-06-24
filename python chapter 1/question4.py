import os

def list_directory_contents(path='.'):
    """
    Lists the contents of the directory at the given path.
    If no path is specified, it lists the contents of the current working directory.
    """
    try:
        # Get the list of files and directories
        contents = os.listdir(path)
        # Print the contents
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory {path} does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory {path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
list_directory_contents('/')
