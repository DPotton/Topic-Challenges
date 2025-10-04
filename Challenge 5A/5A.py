"""Dylan Potton
Topic Challenge 5A
October 2nd, 2025"""

import math


class MyMath:
    """Class to calculate average and standard deviation."""
    def __init__(self):
        self.num_list = []  # Initialize as empty list
    
    def average(self, numbers=None):
        try:
            # Use provided numbers or instance variable
            if numbers is None:
                numbers = self.num_list
            
            if len(numbers) == 0:
                return 0
            
            return sum(numbers) / len(numbers)
        
        except ZeroDivisionError:
            print("Error: Cannot calculate average of empty list")
            return 0
        except TypeError:
            print("Error: Input must contain only numbers")
            return 0
    
    def stddev(self, numbers=None):
        try:
            # Use provided numbers or instance variable
            if numbers is None:
                numbers = self.num_list
                
            if len(numbers) < 2:
                return 0
            
            mean = self.average(numbers)
            squared_differences = [(x - mean) ** 2 for x in numbers]
            sum_squared_differences = sum(squared_differences)
            
            # Sample variance (divide by n-1)
            variance = sum_squared_differences / (len(numbers) - 1)
            
            std_dev = math.sqrt(variance)
            return std_dev
        
        except ZeroDivisionError:
            print("Error: Cannot calculate standard deviation with less than 2 numbers")
            return 0
        except ValueError:
            print("Error: Invalid calculation in standard deviation")
            return 0


def main():
    """Main function to interact with user and display results."""
    my_math = MyMath()
    
    while True:
        try:
            # Prompt user for list of numbers
            print("Enter numbers separated by spaces (or 'quit' to exit):")
            user_input = input().strip()
            
            # Check if user wants to quit
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Check for empty input
            if not user_input:
                print("Error: No numbers entered. Please try again.\n")
                continue
            
            # Convert input to list of floats
            numbers = []
            has_error = False
            
            for part in user_input.split():
                try:
                    numbers.append(float(part))
                except ValueError:
                    print(f"Error: '{part}' is not a valid number. Please try again.\n")
                    has_error = True
                    break
            
            # If there was an error in conversion, try again
            if has_error:
                continue
            
            # Add numbers to the class
            my_math.num_list = numbers
            
            # Calculate and print results
            avg = my_math.average()
            std_dev = my_math.stddev()
            
            print(f"Numbers entered: {my_math.num_list}")
            print(f"Average: {avg:.2f}")
            print(f"Standard Deviation: {std_dev:.2f}")
            print()  # Empty line for readability
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.\n")

if __name__ == "__main__":
    main()