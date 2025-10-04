"""Dylan Potton
Topic Challenge 6B
October 3rd, 2025"""


import csv

def csv_reader(filename):
    """
    Reads a CSV file, multiplies each number by 2, and returns a list of dictionaries.
    
    Args:
        filename (str): Path to the CSV file to read
    
    Returns:
        list: List of dictionaries with modified values
    """
    modified_data = []
    
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            modified_row = {}
            for key, value in row.items():
                # Convert to float, multiply by 2, and convert back to string
                try:
                    modified_value = float(value) * 2
                    modified_row[key] = modified_value
                except ValueError:
                    # If it's not a number, keep the original value
                    modified_row[key] = value
            
            modified_data.append(modified_row)
    
    return modified_data

def csv_writer(data, filename, fieldnames=None):
    """
    Writes a list of dictionaries to a CSV file.
    
    Args:
        data (list): List of dictionaries to write
        filename (str): Path to the output CSV file
        fieldnames (list, optional): List of field names for the CSV header
    """
    if fieldnames is None and data:
        fieldnames = data[0].keys()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    """
    Main function to demonstrate the CSV processing.
    """
    # Read and modify the CSV data
    input_filename = 'data.csv'
    output_filename = 'modified_data.csv'
    
    try:
        # Read the CSV file and multiply all numbers by 2
        modified_data = csv_reader(input_filename)
        
        print("Original data from CSV:")
        with open(input_filename, 'r') as f:
            print(f.read())
        
        print("\nModified data (after multiplying by 2):")
        for row in modified_data:
            print(row)
        
        # Write the modified data to a new CSV file
        csv_writer(modified_data, output_filename)
        
        print(f"\nModified data has been written to '{output_filename}'")
        
        # Display the contents of the new file
        print(f"\nContents of '{output_filename}':")
        with open(output_filename, 'r') as f:
            print(f.read())
            
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found. Please make sure it exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()