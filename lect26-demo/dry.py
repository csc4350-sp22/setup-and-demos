# REPETITIVE

def average_of_averages(l1, l2):
    sum1 = 0
    for number in l1:
        sum1 += number
    avg1 = sum1 / len(l1)

    sum2 = 0
    for number in l2:
        sum2 += number
    avg2 = sum2 / len(l2)

    return (avg1 + avg2) / 2


# BETTER
def average(l):
    return sum(l) / len(l)

def average_of_averages(l1, l2):
    return average([average(l1), average(l2)])
