def split_bill(total_amount: float, num_people: int, tip_percent: float = 18, tax_percent: float = 8.5) -> float:        
    # TODO: Write your code here
    # Step 1: Calculate tax amount and add to total_amount
    # Step 2: Calculate tip amount (on the after-tax total) and add it
    # Step 3: Divide by num_people
    # Step 4: Round to 2 decimal places
    tax_amount = total_amount * (tax_percent / 100)
    total_amount += tax_amount
    tip_amount = total_amount * (tip_percent / 100)
    total_amount += tip_amount
    per_person = round(total_amount / num_people, 2)
    return per_person
    
def get_num_people():
    restaurant_bill = []
    num_people = int(input("Enter the number of people:"))
    has_bills = True
    total_amount = 0
    while has_bills:
        bill_amount = float(input("Enter restaurant bill amount(enter 0 to stop):"))
        if bill_amount != 0:
            restaurant_bill.append(bill_amount)
            total_amount += bill_amount
            each_person_bill = split_bill(bill_amount, num_people)
            print(f"Each person pays: ${each_person_bill:.2f}")
            
        else:
            has_bills = False
    print("Restaurant Breakdown:")
    for i in range(len(restaurant_bill)):
        restaurant_each_person_bill = split_bill(restaurant_bill[i], num_people)
        print(f"Restaurant {i+1}: Bill ${restaurant_bill[i]:.2f} -> Each pays ${restaurant_each_person_bill:.2f}")
    each_person_total_bill = split_bill(total_amount, num_people)
    print(f"Total per person across all restaurants: ${each_person_total_bill:.2f}")
    return num_people

def display_receipt(num_people:int):
    for i in range(40):
        print("=", end = "")
    print()
    print("SPLIT BILL RECEIPT")
    for i in range(40):
        print("=", end = "")
    print()
    print("People sharing the bill:")
    if num_people < 4:
        print(f"😊" * num_people)
    elif num_people <= 6:
        if num_people == 4:
            print(f"😊" * 2 )
            print(f"😊" * 2 )
        else:
            print(f"😊" * 3)
            print(f"😊" * (num_people - 3))
    for i in range(40):
        print("=", end = "") 

def main():
    num_people = get_num_people()
    display_receipt(num_people)
main()