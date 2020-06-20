test1 = [[1, 2], [4, 3], [5, 6], [6, 7]]
test2 = [
    [465, 100],
    [400, 85],
    [255, 55],
    [350, 45],
    [650, 130],
    [1000, 190],
    [455, 100],
    [100, 25],
    [1200, 190],
    [320, 65],
    [750, 100],
    [50, 45],
    [550, 65],
    [100, 50],
    [600, 70],
    [240, 40]
  ]
tCapacity = 10
def napsackProblem(items, capacity):
    knapsack = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    for i in range(len(items) + 1):
        print(knapsack[i])
    print("ITEMS:", items)
    for i in range(1, len(items) + 1):
        weight = items[i - 1][1]
        value = items[i - 1][0]
        print("WEIGHT:", weight)
        print("VALUE:", value)
        for c in range(capacity + 1):
            if weight > c:
                knapsack[i][c] = knapsack[i - 1][c]
            else:
                knapsack[i][c] = max(knapsack[i - 1][c], knapsack[i - 1][c - weight] + value)
    print(knapsack)
    print(knapsack[-1][-1], buildSequence(knapsack, items))

def buildSequence(knapsack, items):
    sequence = []
    i = len(knapsack) - 1
    c = len(knapsack[0]) - 1
    while i > 0:
        if knapsack[i][c] == knapsack[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    for i in range(len(sequence) - 1, -1, -1):
        print(i)
        print("HERE I AM", list(sequence)[i])
    print(sequence, reversed(sequence), list(reversed(sequence)))
    return list(reversed(sequence))

napsackProblem(test1, tCapacity)