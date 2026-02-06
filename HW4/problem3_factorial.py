"""
Problem 3: Calculating the Factorial of a Number
Name: Leijie Tao
NU ID: 003181692

# I confirm that AI code completion tools were disabled while writing this program.

In mathematics, the notation n! represents the factorial of the nonnegative 
integer n. The factorial of n is the product of all the nonnegative integers 
from 1 to n. For example:
    7! = 1 x 2 x 3 x 4 x 5 x 6 x 7 = 5,040
    4! = 1 x 2 x 3 x 4 = 24

Write a program that lets the user enter a nonnegative integer then uses a 
loop to calculate the factorial of that number. Display the factorial.
"""

def get_nonnegative_integer() -> int:
    """
    Prompt the user to enter a nonnegative integer.
    
    Returns:
        int: A nonnegative integer entered by the user
    
    TODO: Implement this function
    Hint: Use input() to get user input and convert it to an integer
    """
    n = int(input("Enter a nonnegative integer you want to calculate the factorial:"))#Use input function to get a number, and convert it to an integer
    while n < 0:#If users input negative hours, give the message and have another input until we get a nonnegative number
        print("Please enter a nonnegative integer.")
        n = int(input("Enter a nonnegative integer you want to calculate the factorial:"))
    return n #Return the value



def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a nonnegative integer using a loop.
    
    Parameters:
        n (int): A nonnegative integer
    
    Returns:
        int: The factorial of n
    
    TODO: Implement this function
    Steps:
    1. Initialize result to 1 (remember: 0! = 1)
    2. Use a loop to multiply result by each number from 1 to n
    3. Return the result
    
    Important: Remember that 0! = 1 by definition
    """
    result = 1 #Initialize result to 1
    for i in range(n): #Iterate n times
        result *= (i + 1) #Use i+1 to multiply result by each number from 1 to n
    return result #Return the result


# TODO: Create a function to display the result
# Think about:
# - What parameters does it need?
# - What should it print?
# - How should it format the output?
def display_result(n:int, result:int) -> int: #Take 'n' and 'result' as parameters, which will be used to display the result
    print(f"The result of {n}! is {result:,}") #Use f-string to format the output

def main():
    """
    Main function to run the factorial calculator.
    """
    # TODO: Get a nonnegative integer from the user
    
    # TODO: Calculate the factorial
    
    # TODO: Display the result
    
    try:
        n = get_nonnegative_integer() #Call the function to get an integer
        res = calculate_factorial(n) #Call the function to calculate the factorial
        display_result(n, res) #Pass the argumrnt to the display_result function
    except:#If users input invalid values, give the error message
        print("Error: Please enter a valid number.")



# Run the program
main()
