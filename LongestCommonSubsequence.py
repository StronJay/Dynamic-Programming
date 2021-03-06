str1, str2, str3, str4 = "clabcnt", "cabcne", "clement", "antoine"

# def longestCommonSubsequence(str1, str2):
#     lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     for i in range( len(str2) + 1):
#         print(lcs[i])
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 print(i, j, lcs[i - 1][j - 1], [str2[i - 1]])
#                 lcs[i][j] = lcs[i -1][j - 1] + [str2[i - 1]]
#             else:
#                 lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key=len)
#     for i in range( len(str2) + 1):
#         print(lcs[i])
#     print(lcs[-1][-1])

# def longestCommonSubsequence(str1, str2):
#     small = str1 if len(str1) < len(str2) else str2
#     big = str1 if len(str1) >= len(str2) else str2
#     print(small, big)
#     evenLcs = [[] for x in range(len(small) + 1)]
#     oddLcs = [[] for x in range(len(small) + 1)]
#     for i in range(1, len(big) + 1):
#         if i % 2 == 1:
#             currentLcs = oddLcs
#             previousLcs = evenLcs
#         else:
#             currentLcs = evenLcs
#             previousLcs = oddLcs
#         for j in range(1, len(small) + 1):
#             if big[i - 1] == small[j - 1]:
#                 currentLcs[j] = previousLcs[j - 1] + [big[i - 1]]
#             else:
#                 currentLcs[j] = max(previousLcs[j], currentLcs[j - 1], key=len)
#     print(evenLcs, "ODD:", oddLcs)
#     print(evenLcs[-1] if len(big) % 2 == 0 else oddLcs[-1])

# def longestCommonSubsequence(str1, str2):
#     lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
#     for i in range(1, len(str2) + 1):
#         for j in range(1, len(str1) + 1):
#             if str2[i - 1] == str1[j - 1]:
#                 lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
#             else:
#                 if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
#                     lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
#                 else:
#                     lcs[i][j] = [None, lcs[i][j - 1][1], i, j -1]
#     print(buildSequence(lcs, str1))

# def buildSequence(lcs, string):
#     sequence = []
#     i = len(lcs) - 1
#     j = len(lcs[0]) - 1
#     while i != 0 and j != 0:
#         currentEntry = lcs[i][j]
#         if currentEntry[0] is not None:
#             sequence.append(currentEntry[0])
#         i = currentEntry[2]
#         j = currentEntry[3]
#     return list(reversed(sequence))

def longestCommonSubsequence(str1, str2):
    lengths = [[0 for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]
    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str1[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])
    print(buildSequence(lengths, str1))

def buildSequence(lengths, string):
    sequence = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1
    while i != 0 and j != 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(string[j - 1])
            j -= 1
            i -= 1
    return list(reversed(sequence))

longestCommonSubsequence(str1, str2)