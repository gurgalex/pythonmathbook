"""Expense visualizer via bar graph"""
from matplotlib import pyplot as plt

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

def plot_expenses(categories, costs):
    """Plot expenses by category onto a horizontal bar chart
    :param categories: Sequence of categories used for labels on graph
    :param costs: Expenditure amount for each category
    """
    ## Equal spaced bars
    positions = [x for x in range(1, len(categories) + 1)]
    plt.barh(positions, costs)
    plt.yticks(positions, categories)
    plt.xlabel("Expenditure")
    plt.ylabel("Category")
    plt.title("Expense visualizer")
    plt.grid()
    plt.show()


categories, cost = get_expense_info()
plot_expenses(categories, cost)
