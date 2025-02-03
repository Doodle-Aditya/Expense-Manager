import json
import time
def new_category(category):
    categories = category_loader()
    if category in categories:
        return "Category Already Exist"
    categories[category] = []

    with open('categories.txt','w') as file:
        json.dump(categories,file)


def category_loader():
    with open('categories.txt','r') as file:
        categories = json.load(file)
        return categories
    
def list_all_categories():
    categories = category_loader()
    for i in categories:
        print(i)

def dumper(var):
    with open('categories.txt','w') as file:
        json.dump(var,file)

def add_expense(cat,amount,description):
    categories = category_loader()
    data = categories[cat]
    temp = {description:amount}
    data.append(temp)
    dumper(categories)
    print('Added Succesfully')
    
def total_expense():
    temp = category_loader()
    total = 0
    for expenses in temp.values():
        for expense in expenses:
            total = total + sum(expense.values())
    return total

def category_expense():
    categories = category_loader()
    
    for category, expense_list in categories.items():
        total = sum(list(expense.values())[0] for expense in expense_list)
        print('*'*70)
        print(f"Total expenses in {category}: {total}")
        print('*'*70)


def main():
    print('''Hello! Welcome to expense manager app 
          \n How would you like to proceed''')
    user_input = int(input('''1.Add a New Category
                           \n 2.Add expense to existing category
                           \n3.Check total expenses
                           \n4.Check expenses in each category
                           \n'''))
    if user_input == 1:
        category = input('Enter New Category')
        new_category(category)
    elif user_input == 2:
        list_all_categories()
        cat = input("Enter in which category you want to add expense: ")
        amt = int(input('Enter the amount you spent: '))
        description = input('Enter the description of the amount spent: ')
        add_expense(cat,amt,description)
    elif user_input == 3:
        value = total_expense()
        print(f"Your Total expense is {value}")
    elif user_input == 4:
        category_expense()
    else:
        print('Thankyou for using')

if __name__ == '__main__':
    while True:
        time.sleep(3)
        main()
