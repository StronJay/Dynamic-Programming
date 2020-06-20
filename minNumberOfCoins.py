n = 13
ds = [2, 4]
def minNumOfCoins(n, denoms):
    smallestWays = [float("inf") for amount in range(n + 1)]
    smallestWays[0] = 0
    print(smallestWays)
    for d in ds:
        for a in range(len(smallestWays)):
            if d <= a:
                print(d, a, [a - d])
                smallestWays[a] = min(smallestWays[a], smallestWays[a - d] + 1)
    return smallestWays[-1] if smallestWays[-1] != float("inf") else -1
print(minNumOfCoins(n, ds))