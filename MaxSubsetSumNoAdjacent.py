# def maxSubsetSumnoAdjacent(array):
#     if not len(array):
#         return 0
#     elif len(array) == 1:
#         return array[0]
#     maxSums = array[:]
#     print(array)
#     maxSums[1] = max(array[0], array[1])
#     print(maxSums)
#     for i in range(2, len(array)):
#         maxSums[i] = max(maxSums[i- 1], maxSums[i - 2] + array[i])
#         print("ITERATION:", i - 1, maxSums[i- 1], i - 2, maxSums[i - 2], i, array[i])
#     print(maxSums[-1])
test1 = [75, 105, 120, 75, 90, 135]
test = [30, 45, 50, 55, 100, 120]


def maxSubsetSumNoAdjacent(array):
    print(array)
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    first = max(array[0], array[1])
    second = array[0]
    print("FIRST:", first)
    print("SECOND:", second)
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        print("ARRAY:", array[i], i)
        print("CURRENT:", current, i)
        second = first
        print("SECOND:", second, i)
        first = current
        print("FIRST:", first, i)
    print(first)

print(maxSubsetSumNoAdjacent(test))