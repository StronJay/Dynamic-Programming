test =  [8, 12, 15,  7]

def mxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    print(sequences)
    sums = array[:]
    print(sums)
    maxSumIdx = 0
    for i in range(1, len(array)):
        currentNum = array[i]
        print("array[i]:", currentNum)
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum >= sums[i]:
                print("otherNum:", otherNum, "currentNum:", currentNum, "sums[j]:", sums[j], "sums[i]", sums[i])
                sums[i] = sums[j] + currentNum
                print(sums)

                sequences[i] = j
            if sums[i] > sums[maxSumIdx]:
                maxSumIdx = i
    
    print(sequences)
    print([sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)])

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

print(mxSumIncreasingSubsequence(test))