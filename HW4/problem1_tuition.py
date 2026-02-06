"""
Problem 1: Tuition Increase
Name: Leijie Tao
NU ID: 003181692

# I confirm that AI code completion tools were disabled while writing this program.

At one college, the tuition for a full-time student is $8,000 per semester. 
It has been announced that the tuition will increase by 3 percent each year 
for the next 5 years. Write a program with a loop that displays the projected 
semester tuition amount for the next 5 years.
"""

def calculate_tuition_for_year(current_tuition: float, increase_rate: float) -> float:
    """
    Calculate the tuition for the next year based on the increase rate.
    
    Parameters:
        current_tuition (float): The current year's tuition amount
        increase_rate (float): The annual increase rate (e.g., 0.03 for 3%)
    
    Returns:
        float: The tuition amount for the next year
    
    TODO: Implement this function
    """
    next_year_tuition = current_tuition * (1 + increase_rate) #Calculate tuition for the next year
    return next_year_tuition #Return the value


def display_tuition_projection(starting_tuition: float, increase_rate: float, num_years: int) -> float:
    """
    Display the tuition projection for the specified number of years.
    
    Parameters:
        starting_tuition (float): The initial tuition amount
        increase_rate (float): The annual increase rate (e.g., 0.03 for 3%)
        num_years (int): Number of years to project
    
    TODO: Implement this function
    Steps:
    1. Print a header for the output
    2. Use a loop to calculate and display tuition for each year
    3. Use the calculate_tuition_for_year() function inside your loop
    4. Format the output nicely (e.g., "Year 1: $8,240.00")
    """
    print("The tuition projection for the next years will be:")
    for i in range(num_years): #Calculate the tuition for next year for "num_year" times
        amount = calculate_tuition_for_year(starting_tuition, increase_rate) #Call the function to calculate
        starting_tuition = amount #Update current value of starting_tuition
        print(f"Year {i+1}: ${amount:,.2f}") #Print the tuition for each year, and use f-string to format the output.




def main():
    """
    Main function to run the tuition projection program.
    """
    # TODO: Define the constants
    
    # TODO: Call the display_tuition_projection function with the constants
    starting_tuition = 8000 #Assign a value to the variable, and pass it as an argument to the function
    increase_rate = 0.03 #Assign a value to the variable, and pass it as an argument to the function
    num_years = 5 #Assign a value to the variable, and pass it as an argument to the function
    display_tuition_projection(starting_tuition, increase_rate, num_years) #Call the function to display the result
    


# Run the program
main()
