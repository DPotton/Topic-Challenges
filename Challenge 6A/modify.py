"""Dylan Potton
Topic Challenge 6A
October 3rd, 2025"""

def modify_aqua_line():
    """Reads the file and replaces the line containing 'Aqua' with 'Azure #007fff'"""
    try:
        with open("6A.txt", "r") as file:
            lines = file.readlines()
        
        # Replace the line containing Aqua
        modified_lines = []
        for line in lines:
            if "Aqua" in line:
                modified_lines.append("Azure #007fff\n")
            else:
                modified_lines.append(line)
        
        return "".join(modified_lines)
        
    except FileNotFoundError:
        print("File '6A.txt' not found!")
        return None

def overwrite_file(modified_content):
    """Overwrites the original file with the modified content"""
    if modified_content is not None:
        with open("6A.txt", "w") as file:
            file.write(modified_content)
        print("File successfully updated!")

# Usage
modified_text = modify_aqua_line()
overwrite_file(modified_text)