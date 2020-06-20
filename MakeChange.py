def makeChange(n, denoms):
    ways = [0 for j in range(n + 1)]
    ways[0] = 1
    print(ways)
    for i in denoms:
        for j in range(1, n + 1):
            print("DENOM:", i, "AMOUNT:", j)
            if i <= j:
                ways[j] += ways[j - i]
                print(ways, ways[j- i])
    print(ways)

denoms = [1, 2, 3, 4, 7]
n = 7
print(makeChange(n, denoms))