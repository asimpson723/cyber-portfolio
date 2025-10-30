#Alex Simpson
#October 2, 2025
#Assignment 6
#Budget Analysis


#Input/Process
#Ask the user to enter their budget for the month
budget = int(input("What is your monthly budget?: "))

#If the input is zero or less than zero ask for the input again
if budget <= 0:
    print("Invalid number entered, please try again.")
    budget = int(input("What is your monthly budget?: "))

#Initialize variables
expenses = 1
total_expenses = 0
keep_going = "Y"

#Ask the user to enter the amout of an expense
while keep_going == "Y":
    expenses = int(input("Enter your expense: "))
    keep_going = input("Do you have another expense? (Enter Y for yes and N for no)")
    #Calculate expenses and remaining budget 
    total_expenses = expenses + total_expenses
    remaining_budget = budget - total_expenses

#Output
if keep_going == "N":
    print()
    #Display the total amount of the user's budget
    print(f"Your total monthly budget is ${budget:,.2f}")
    #Display the total amount of expenses
    print(f"Your total monthly expenses are: ${total_expenses:,.2f}")
    #Display remaining balance of budget after expenses have been paid
    print(f"Your remaining budget is: ${remaining_budget:,.2f}") 
if total_expenses > budget:
    print("You are over budget!")
else:
    print("You are under budget,Great Job!")
