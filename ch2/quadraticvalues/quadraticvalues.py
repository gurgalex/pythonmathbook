
def calc(x_list):
    """Returns a list of values given a quadratic formula and a x-value list"""

    y_list = [x**2 + 2*x + 1 for x in x_list]

    return y_list
