test = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]
test1 = [
    [3, 3, 4],
    [2, 1, 2],
    [3, 2, 3],
    [2, 2, 8],
    [2, 3, 4],
    [5, 5, 6],
    [1, 2, 1],
    [4, 4, 5],
    [1, 1, 4],
    [2, 2, 3]
  ]
def stackDisks(array):
    print("NOT SORTED:",array)
    array.sort(key=lambda disk: disk[2])
    print("SORTED WITH KEY=LAMBDA X: X[2]",array)
    heights = [disk[2] for disk in array]
    print("HEIGHTS:",heights)
    sequences = [None for idx in array]
    print("SEQUENCES:",sequences)
    maxHeightIdx = 0
    for i in range(1, len(array)):
        currentDisk = array[i]
        print("CURRENT:",currentDisk)
        for j in range(0, i):
            otherDisk = array[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] < heights[j] + currentDisk[2]:
                    heights[i] = currentDisk[2] + heights[j]
                    print("HEIGHTS UPDATED:", heights)
                    sequences[i] = j
                if heights[i] >= heights[maxHeightIdx]:
                    maxHeightIdx = i
    print(buildSequence(array, sequences, maxHeightIdx))


def buildSequence(array, sequences, cIdx):
    sequence = []
    while cIdx is not None:
        sequence.append(array[cIdx])
        cIdx = sequences[cIdx]
    return list(reversed(sequence))

def areValidDimensions(o, c):
    return o[0] < c[0] and o[1] < c[1] and o[2] < c[2]

stackDisks(test1)

