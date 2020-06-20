pi = "3141592653589793238462643383279"
test = ["3",
        "314",
        "49",
        "9001",
        "15926535897",
        "14",
        "93238462643383279",
        "9323",
        "8462643383279",
        "4",
        "793"]
notest = ["3141", "1512", "159", "592", "59265", "793", "12412451", "8462643383279"]

def numbersInPi(pi, numbers):
    numbersTable = {number: True for number in numbers}
    print(numbersTable)
    minSpaces = getMinSpaces(pi, numbersTable, {}, 0)
    print("Minimum Spaces:",minSpaces)
    return -1 if minSpaces == float("inf") else minSpaces
no = {18: 0, 14: 1, 3: 2, 1: 3}

def getMinSpaces(pi, numbersTable, cache, idx):
    print("idx:",idx)
    print("CREAM:",cache)
    if idx == len(pi):
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx, len(pi)):
        prefix = pi[idx : i + 1]
        print("PREFIX:",prefix, "Does this exist in numbersTable?",  "i:", i, "idx:", idx)
        if prefix in numbersTable:
            print("YES IT DOES!", prefix, "i:", i, "idx:", idx)
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i + 1)
            minSpaces = min(minSpaces, minSpacesInSuffix + 1)
    cache[idx] = minSpaces
    return cache[idx]


numbersInPi(pi, test)
