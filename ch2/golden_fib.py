"""Compares the fibonacci sequence to the golden ratio using a graph"""
from matplotlib import pyplot as plt


def fiblist(n):
    """Returns a list of n fibonacci numbers"""
    sequence = [i for i in fibseq(n)]
    return sequence


def fibseq(n):
    """Yields the next fibonacci number"""
    # Set values for fib 1 and 2
    first, second = 1, 1

    # compute the next value of the fib sequence
    for x in range(n):  # Only generate a certain amount of values
        yield first  # avoid recursion depth limit
        first, second = second, first + second


n = 100
fibs = fiblist(n)

golden = []
for i, fib in enumerate(fibs):
    if (i == 0):
        continue

    else:
        ratio = fibs[i] / fibs[i-1]
        golden.append(ratio)

x_axis = [x for x in range(1, 100)]  # only 99 ratio values
plt.title("Ratio between consecutive Fibonacci numbers")
plt.xlabel("Seq num")
plt.ylabel("Ratio")
plt.plot(x_axis, golden)
plt.show()
