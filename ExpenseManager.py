#Start by asking the user for some of the require expense information

month = int(input("Please enter the month for the expense being added: "))
while month not in range(1, 13):
    print("I'm sorry but the value entered is invalid. Please try again.")
    month = int(input("Please enter the month for the expebse being added (1-12): "))

day = int(input("Please enter the day of the expense being entered: "))
while day not in range(1, 32):
    print("I'm sorry but the value entered is invalid. Please try again.")
    day = int(input("Please enter the day of the expense being added"))

category = input("What is the category for the expense being entered?: ")
while category != ("Food", )

description = input("Please enter a desciption for the expense being entered: ")

amount = input("What is the amount for the expense being entered?: ")

#write the expense data to a text file
with open("expenses.txt", "a") as f:
    f.write(f"{date}, {category}, {description}, {amount}\n")

#Be able to read the data in the text file
with open("expenses.txt", "r") as f:
    expenses = [line.strip().split(",") for line in f]

#Display the expenses to the user/reader
print("All Expenses: ")
for expense in expenses:
    print(f"{expense[0]} - {expense[1]} - {expense[2]} - ${expense[3]}")

#Filter the expenses by date
start_date = input("Please enter the start date for the filter (MM-DD-YYYY): ")
end_date = input("Please enter the end date for the filer (MM-DD-YYYY): ")
filtered_expenses = [expense for expense in expenses if start_date <= expense[0] <= end_date]

#Display the filterd expenses
print("Filtered Expenses: ")
for expense in filtered_expenses:
    print(f"{expense[0]} - {expense[1]} - {expense[2]} - ${expense[3]}")

#Generate a report for the filtered expenses
total_spent  = sum(float(expense[3]) for expense in filtered_expenses)
average_spent = total_spent / len(filtered_expenses)
print(f"Total spent: ${total_spent:.2f}")
print(f"Average spent per expense: ${average_spent:.2f}")