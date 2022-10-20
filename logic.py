import random
import csv
import time
from numpy.random import multinomial


def randomize2(n, total):
    divide = 1 / n
    return multinomial(total, [divide] * n)


def randomize(n, total, minn, maxx):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""
    dividers = None
    if n - 1 > maxx-minn:
        dividers = sorted(random.sample(range(1, total), n - 1))
    else:
        dividers = sorted(random.sample(range(minn, maxx), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]


def generate_excel(ts, cn, max_n, min_n):
    total_sum = 0
    columns_number = 0
    if ts.isnumeric():
        total_sum = int(ts)
    if cn.isnumeric():
        columns_number = int(cn)
    max_number = total_sum
    min_number = 1
    if max_n.isnumeric():
        max_number = int(max_n)
    if min_n.isnumeric():
        min_number = int(min_n)
    results = []
    if columns_number > total_sum:
        results = randomize2(columns_number, total_sum)
    else:
        results = randomize(columns_number, total_sum, min_number, max_number)
    create_excel(results)


def create_excel(results):
    t = time.localtime()
    current_time = time.strftime("%H.%M.%S", t)
    name = 'RandomExcel' + current_time + '.csv'
    maxxx = 0
    with open(name, 'w', newline='') as file:
        writer = csv.writer(file)
        for element in results:
            if element > maxxx:
                maxxx = element
            writer.writerow([element])
    print("Finished! The file is - " + name)

