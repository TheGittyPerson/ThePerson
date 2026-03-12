# src/person.py

def fix_documentation_typos(file_path):
    import re
    from textblob import TextBlob

    # Read the file content
    with open(file_path, 'r') as file:
        content = file.read()

    # Use TextBlob to correct typos
    blob = TextBlob(content)
    corrected_content = blob.correct().string

    # Write the corrected content back to the file
    with open(file_path, 'w') as file:
        file.write(corrected_content)

# Example usage
if __name__ == "__main__":
    fix_documentation_typos('CONTRIBUTING.md')