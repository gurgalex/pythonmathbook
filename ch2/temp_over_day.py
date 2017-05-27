import matplotlib.pyplot as plt

hours_of_day = [
        "6 PM", "9 PM", "12 AM",
        "3 AM", "6AM", "9 AM", "12 PM",
        "3 PM"]

x_count = [x for x in range(len(hours_of_day))]

temperatures_of_day = [80, 71, 61, 57, 54, 64, 71, 73]

def plot_data(x, y):
    plt.plot(x, y)

def plot_xticks(x_dummy_values, xticks):
    plt.xticks(x_dummy_values, xticks)

plot_data(x_count, temperatures_of_day)
plot_xticks(x_count, hours_of_day)
plt.show()
