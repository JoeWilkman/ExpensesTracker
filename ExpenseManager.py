#Start by asking the user for some of the require expense information
import tkinter as tk

#create the main window for the program
root = tk.Tk()
root.title("Expense Tracker")

#Create the expense entry form
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP)

label1 = tk.Label(frame1, text="Date:")
label1.pack(side=tk.LEFT)

entry1 = tk.Entry(frame1)
entry1.pack(side=tk.LEFT)

label2 = tk.Label(frame1, text="Category:")
label2.pack(side=tk.LEFT)

entry2 = tk.Entry(frame1)
entry2.pack(side=tk.LEFT)

label3 = tk.Label(frame1, text="Description:")
label3.pack(side=tk.LEFT)

entry3 = tk.Entry(frame1)
entry3.pack(side=tk.LEFT)

label4 = tk.Label(frame1, text="Amount:")
label4.pack(side=tk.LEFT)

entry4 = tk.Entry(frame1)
entry4.pack(side=tk.LEFT)

def add_expense():
    # Add the expense to the file
    with open("expenses.txt", "a") as f:
        f.write(f"{entry1.get()},{entry2.get()},{entry3.get()},{entry4.get()}\n")

    # Clear the entry fields
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

# Create the add expense button
frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP)

button1 = tk.Button(frame2, text="Add Expense", command=add_expense)
button1.pack(side=tk.LEFT)

# Create the expense display area
frame3 = tk.Frame(root)
frame3.pack(side=tk.TOP)

scrollbar = tk.Scrollbar(frame3)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(frame3, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

#Populate the listbox with expenses from the file
with open("expenses.txt", "r") as f:
    expenses = [line.strip().split(",") for line in f]

for expense in expenses:
    listbox.insert(tk.END, f"{expense[0]} - {expense[1]} - {expense[2]} - ${expense[3]}")

scrollbar.config(command=listbox.yview)

root.mainloop()

month = int(input("Please enter the month for the expense being added: "))
while month not in range(1, 13):
    print("I'm sorry but the value entered is invalid. Please try again.")
    month = int(input("Please enter the month for the expebse being added (1-12): "))

day = int(input("Please enter the day of the expense being entered: "))
while day not in range(1, 32):
    print("I'm sorry but the value entered is invalid. Please try again.")
    day = int(input("Please enter the day of the expense being added"))

year = int(input("Please enter the year of the expense being entered: "))
while year not in range(2005, 2099):
    print("I'm sorry but the value entered is invalid. Please try again.")
    year = int(input("Please enter the day of the expense being added"))

date = month + day + year

category = input.lower()("What is the category for the expense being entered?: ")
while category != ("food", "bills", "gas", "emergencies", "personal", "misc.", "school"):
    print("I'm sorry but the value entered is invalid. Please try again.")
    category = input.lower()("What is the category for the expense being entered?: ")

description = input("Please enter a desciption for the expense being entered: ")

amount = input("What is the amount for the expense being entered?: ")
while amount not in range(0.01, 500,000):
    print("I'm sorry but the value entered in invalid. Please try again.")
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
