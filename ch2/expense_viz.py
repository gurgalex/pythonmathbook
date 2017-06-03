"""Expense visualizer via bar graph"""

def get_expense_info():
    category = []
    cost = []

    get_number_of_categories = True
    while(get_number_of_categories):
        try:
            number_categories = int(input("How many categories? "))
            get_number_of_categories = False;
        except ValueError:
            print("Whoops, please enter a whole number.")

    for n in range(number_categories):
        category.append(input("Category: "))
        no_expense_entered = True
        while(no_expense_entered):
            try:
                cost.append(int(input("Expenditure: ")))
                no_expense_entered = False
            except ValueError:
                print("Enter a whole number for expenditure.")

    return (category, cost)

category, cost = get_expense_info()
