arr1 = [3, 10, 2, 1, 2, 3, 7, 1, 1, 1, 3, 2, 3, 2, 1, 1, 1, 1]
test1 = [2, 1, 2, 3, 1, 1, 1]
def minJumps(array):
    jumps = [float("inf") for x in array]
    jumps[0] = 0
    for i in range(1, len(array)):
        for j in range(0, i):
            print("ARRAY[j]:", array[j], "i", i, "j", j)
            if array[j] >= i - j:
                jumps[i] = min(jumps[j] + 1, jumps[i])
                print("JUMPS:", jumps[i])
    print(jumps)
    print(array)
    print(jumps[-1])

# def minJumps(array):
#     if len(array) == 1:
#         return 0
#     jumps = 0
#     maxReach = array[0]
#     steps = array[0]
#     for i in range(1, len(array) - 1):
#         print("MAX REACH:", maxReach, "INDEX", i, "ARRAY[i]:", array[i], "STEPS:", steps)
#         maxReach = max(maxReach, i + array[i])
#         steps -= 1
#         if steps == 0:
#             print(jumps)
#             jumps += 1
#             steps = maxReach - i
#     print(array)
#     print(jumps + 1)

minJumps(test1)