"""
Problem 2: Sleep Debt
Name: Leijie Tao
NU ID: 003181692

# I confirm that AI code completion tools were disabled while writing this program.

A "sleep debt" represents the difference between a person's desirable and 
actual amount of sleep. Write a program that prompts the user to enter how 
many hours he or she slept each day over a period of 7 days. Using 8 hours 
per day as the desirable amount of sleep, determine his or her sleep debt by 
calculating the total hours of sleep they got over the seven-day period and 
subtracting that from the total hours of sleep he or she should have got. 
If the user does not have a sleep debt, display a message expressing your jealousy.
"""

def get_sleep_hours(num_days: int) -> float:
    """
    Prompt the user to enter hours slept for each day.
    
    Parameters:
        num_days (int): Number of days to track sleep
    
    Returns:
        float: Total hours of sleep over all days
    
    TODO: Implement this function
    Steps:
    1. Initialize a variable to store total sleep hours
    2. Use a loop to prompt for sleep hours for each day
    3. Add each day's hours to the total
    4. Return the total
    """
    total_sleep_hours = 0 #Create a variable to record total sleeping hours
    for i in range(1, num_days + 1): #Iterate from 1 to 7 to get the sleeping hours of each day
        sleep_hour_each_day = float(input(f"How many hours do you have for No.{i} day of this week?")) #Use input to get the sleeping hours of a specific day
        while sleep_hour_each_day < 0: #If users input negative hours, give the message and have another input until we get a nonnegative number
            print("Enter nonnegative number of hours")
            sleep_hour_each_day = float(input(f"How many hours do you have for No.{i} day of this week?"))
        total_sleep_hours += sleep_hour_each_day #Add the hours to the total
    return total_sleep_hours #Return the total



# TODO: Create a function to calculate sleep debt
# Think about what parameters it needs and what it should return
# Hint: You'll need actual sleep hours and desirable sleep hours

def calculate_sleep_debt(desirable_hour_per_day: float, total_sleep_hours: float) -> float:
    """
    TODO: Write the docstring
    - What does this function do?
    - What parameters does it need?
    - What does it return?
    """
    sleep_hour_needed = desirable_hour_per_day * 7 #Calculate total desiable sleeping hours over a period of 7 days
    sleep_debt = sleep_hour_needed - total_sleep_hours #Calculate the debt
    return sleep_debt # Return the debt


def display_sleep_debt_results(sleep_debt: float) -> float:
    """
    Display the sleep debt results with appropriate message.
    
    Parameters:
        sleep_debt (float): The calculated sleep debt (can be positive, negative, or zero)
    
    TODO: Implement this function
    Steps:
    1. If sleep_debt > 0: Display how many hours of sleep debt they have
    2. If sleep_debt <= 0: Express jealousy that they got enough/extra sleep
    """
    if sleep_debt > 0: #If the debt is positive, display the hours
        print(f"Your sleep debt are {sleep_debt} hours. ")
    else: #If the debt is negative or 0, express jealousy
        print(f"How can you sleep for such a long time!")


def main():
    """
    Main function to run the sleep debt calculator.
    """
    # Constants
    DESIRABLE_HOURS_PER_DAY = 8
    NUM_DAYS = 7
    
    # TODO: Get total actual sleep hours from user
    
    # TODO: Calculate total desirable sleep hours
    
    # TODO: Calculate sleep debt using your calculate_sleep_debt function
    
    # TODO: Display results using display_sleep_debt_results function
    
    try: 
        total_sleep_hours = get_sleep_hours(NUM_DAYS) #Call the function, and pass the argument to the function
        sleep_debt = calculate_sleep_debt(DESIRABLE_HOURS_PER_DAY, total_sleep_hours)#Call the function, and pass the argument to the function
        display_sleep_debt_results(sleep_debt) #Call the function, and pass the argument to the function
    except: #If users input invalid values, give the error message
        print("Error: please enter valid numbers.")

# Run the program
main()
