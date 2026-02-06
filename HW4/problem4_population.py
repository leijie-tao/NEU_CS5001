"""
Problem 4: Population
Name: Leijie Tao
NU ID: 003181692

# I confirm that AI code completion tools were disabled while writing this program.

Write a program that predicts the approximate size of a population of organisms. 
The application should prompt the user to enter the starting number of organisms, 
the average daily population increase (as a percentage), and the number of days 
the organisms will be left to multiply.

Example:
    Starting number of organisms: 2 
    Average daily increase: 30% 
    Number of days to multiply: 10

The program should display a table showing the population for each day.
"""

def get_population_inputs():
    """
    Prompt user for initial population parameters.
    
    Returns:
        (starting_population, daily_increase_rate, num_days)
        daily_increase_rate should be as a decimal (e.g., 0.30 for 30%)
    
    TODO: Implement this function
    Steps:
    1. Prompt for starting number of organisms
    2. Prompt for daily increase percentage
    3. Prompt for number of days
    4. Convert percentage to decimal (divide by 100)
    5. Return all three values
    """
    starting_population = float(input("Enter the starting number of organisms:"))#Use input function to get the starting number, and convert it to float
    daily_increase_rate = float(input("Enter the average daily population increase((e.g., 30 for 30%)):"))/100 #Use input function to get the population increase rate, and convert it to float
    num_days = int(input("Enter the number of days the organisms will be left to multiply:"))#Use input function to get the number of days, and convert it to integer
    return starting_population, daily_increase_rate, num_days #Return the arguments

def calculate_next_day_population(current_population: float, daily_increase_rate: float) -> float:
    """
    Calculate population for the next day.
    
    Parameters:
        current_population (float): Current day's population
        daily_increase_rate (float): Daily increase rate as decimal (e.g., 0.30 for 30%)
    
    Returns:
        float: Population for the next day
    
    TODO: Implement this function
    Hint: Next population = current population * (1 + daily_increase_rate)
    """
    next_population = current_population * (1 + daily_increase_rate) #Calculate next-day population and return
    return next_population #return the argument

# TODO: Create a function to display the population table
# This function should:
# - Take starting_population, daily_increase_rate, and num_days as parameters
# - Print a header for the table
# - Use a loop to calculate and display population for each day
# - Use the calculate_next_day_population() function in your loop
# - Format output nicely (e.g., "Day 1: 2.00 organisms")
def display_population_table(starting_population:float , daily_increase_rate: float, num_days: int) -> float:
    print(f"The population table of the next {num_days} days:") #Print a header for the table
    for i in range(num_days): #Iterate 'num_days' times
        next_population = calculate_next_day_population(starting_population, daily_increase_rate) #For each iteration, call the function to calculate next-day population
        print(f"Day {i+1}: {next_population:,.2f} organisms") #Print the result with required format
        starting_population = next_population #Update the starting population


def main():
    """
    Main function to run the population growth predictor.
    """
    # TODO: Get inputs from user using get_population_inputs()
    
    # TODO: Display the population table using your display function
    
    starting_population, daily_increase_rate, num_days = get_population_inputs() #Call the function to get 3 inputs
    display_population_table(starting_population, daily_increase_rate, num_days) #Pass the arguments to the display function

# Run the program
main()
