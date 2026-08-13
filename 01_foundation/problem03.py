import os
# select a directory to list its contents
def print_directory_contents(path='.'):
    """
    Prints the files and directories inside the given path.
    Defaults to the current working directory ('.').
    """
    try:
        # Fetch the list of all files and directories
        contents = os.listdir(path)
        
        print(f"Contents of directory '{path}':")
        print("-" * 30)
        
        # Iterate through the list and print each item
        for item in contents:
            print(item)
            
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Print contents of the current directory
print_directory_contents()

# To print contents of a specific directory, pass the path as a string:
# print_directory_contents('/path/to/your/directory')


# Another Alternative
import os

# write all the contents of a directory in a detailed manner
# example: [File] filename.txt, [Directory] foldername
def print_detailed_contents(path='.'):
    try:
        # scandir returns an iterator of DirEntry objects
        with os.scandir(path) as entries:
            print(f"Detailed contents of '{path}':")
            print("-" * 30)
            for entry in entries:
                # You can easily check if it's a file or a directory
                item_type = "File" if entry.is_file() else "Directory"
                print(f"[{item_type}] {entry.name}")
                
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")