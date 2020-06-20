string1 = "abc"
string2 = "yabdax"
# def leveDistance(str1, str2):
#     minNumOfEdits = [[x for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     print(minNumOfEdits )
#     for i in range(1, len(str2) + 1):
#         minNumOfEdits[i][0] = minNumOfEdits[i - 1][0] + 1
#         print(minNumOfEdits[i])
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             print(str1[j - 1], str2[i - 1])
#             if str1[j - 1] == str2[i - 1]:
#                 minNumOfEdits[i][j] = minNumOfEdits[i - 1][j - 1]
#             else:
#                 minNumOfEdits[i][j] = 1 + min(minNumOfEdits[i - 1][j], minNumOfEdits[i][j - 1], minNumOfEdits[i - 1][j - 1])    
#     for i in range(len(str2) + 1):        
#         print(minNumOfEdits[i])
#     print(minNumOfEdits[-1][-1])

def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2
    print(small)
    big = str1 if len(str1) >= len(str2) else str2
    print(big)
    evenEdits = [x for x in range(len(small) + 1)]
    print(evenEdits)
    oddEdits = [None for x in range(len(small) + 1)]
    print(oddEdits)
    for row in range(1, len(big) + 1):
        if row % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = row
        print('CURRENT EDITS:', currentEdits)
        print("PREV:", previousEdits)
        for col in range(1, len(small) + 1):
            print(big[row - 1], small[col - 1])
            if big[row - 1] == small[col - 1]:
                currentEdits[col] = previousEdits[col - 1]
            else:
                currentEdits[col] = 1 + min(currentEdits[col - 1], previousEdits[col], previousEdits[col - 1])
    print(evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1])
levenshteinDistance(string1, string2)