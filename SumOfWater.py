test = [0, 100, 0, 0, 10, 1, 1, 10, 1, 0, 1, 1, 0, 100]
def sumOfWater(array):
    maxes = [0 for x in array]
    leftMax = 0
    for i in range(len(array)):
        maxes[i] = leftMax
        leftMax = max(leftMax, array[i])
        print(i, leftMax)
    print("LEFT MAXES:", maxes)
    rightMax = 0
    for i in reversed(range(len(array))):
        
        minHeight = min(rightMax, maxes[i])
        if array[i] < minHeight:
            maxes[i] = minHeight - array[i]
            print("Min Height:", maxes, "i", i)
        else:
            maxes[i] = 0
            print("Min Height: --", maxes, "i", i)
        rightMax = max(rightMax, array[i])
    print(array)
    print(sum(maxes))

#sumOfWater(test)

fuku = [3, 5, -4, 8, 11, 1, -1, 6]

def workBitch(array, tS):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            currentSum = array[i] + array[j]
            if currentSum == tS:
                print(i, j, currentSum)

workBitch(fuku, 10)

