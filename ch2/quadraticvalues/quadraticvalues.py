"""Quadratic equation graph plotter"""
from matplotlib import pyplot as plt


def calc(x_list):
    """Returns a list of values given a quadratic formula and a x-value list"""

    y_list = [x**2 + 2*x + 1 for x in x_list]

    return y_list


def parse_input(userstring):
    """Takes supplied string and converts to a list of values"""
    xsplit = userstring.split()
    stringtovalues = [float(x) for x in xsplit]

    return stringtovalues


if __name__ == "__main__":
    # get x values
    x_input = input("Space separated x values: ")

    # parse x values
    x_values = parse_input(x_input)
    y_values = calc(x_values)

    # plot graph
    plt.plot(x_values, y_values)
    plt.show()
