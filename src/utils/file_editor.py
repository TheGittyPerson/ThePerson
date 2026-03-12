import re

def update_file_content(file_path, search_pattern, replacement):
    """
    Update the content of a file by replacing occurrences of a search pattern with a replacement string.
    
    Parameters:
    file_path (str): The path to the file to be updated.
    search_pattern (str): The regular expression pattern to search for.
    replacement (str): The string to replace the search pattern with.
    
    Returns:
    bool: True if the file was updated, False otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        
        changes_made = False
        for i, line in enumerate(content):
            if re.search(search_pattern, line):
                content[i] = re.sub(search_pattern, replacement, line)
                changes_made = True
        
        if changes_made:
            with open(file_path, 'w') as file:
                file.writelines(content)
        
        return changes_made
    except Exception as e:
        print(f"An error occurred: {e}")
        return False