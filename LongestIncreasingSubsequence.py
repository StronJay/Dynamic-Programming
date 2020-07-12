class Solution(object):
    #O(n^2) T | O(n) S
    def longestIncreasingSubsequence(self, array):
        longestSoFar = [1 for x in array]
        idxs = [None for i in array]
        max_idx = 0
        for i in range(1, len(array)):
            for j in range(0, i):
                if array[j] < array[i] and longestSoFar[i] < longestSoFar[j] + 1:
                    longestSoFar[i] = longestSoFar[j] + 1
                    idxs[i] = j
            if longestSoFar[i] >= longestSoFar[max_idx]:
                max_idx = i
        return self.buildSequence(array, idxs, max_idx)

    def buildSequence(self, array, idxs, current_idx):
        sequence = []
        while current_idx is not None:
            sequence.append(array[current_idx])
            current_idx = idxs[current_idx]
        return list(reversed(sequence))
    # O(nlogn) T | O(n) S
    def longest_increasing_subsequence(self, array):
        max_length = 0
        sequences = [None for _ in array]
        idxs = [None for i in range(len(array)+1)]
        for i, num in enumerate(array):
            new_length = self.binary_search(1, max_length, array, idxs, num)
            sequences[i] = idxs[new_length-1]
            idxs[new_length] = i
            max_length = max(max_length, new_length)

        return self.build_sequence(array, sequences, idxs[max_length])

    def binary_search(self, start_idx, end_idx, array, idxs, num):
        if start_idx > end_idx: return start_idx

        mid_idx = (start_idx + end_idx) // 2
        if   array[idxs[mid_idx]] < num: start_idx = mid_idx + 1
        elif array[idxs[mid_idx]] > num: end_idx = mid_idx - 1

        return self.binary_search(start_idx, end_idx, array, idxs, num)

    def build_sequence(self, array, sequences, current_idx):
        sequence = []
        while current_idx is not None:
            sequence.append(array[current_idx])
            current_idx = sequences[current_idx]

        return list(reversed(sequence))

test = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(Solution().longest_increasing_subsequence(test))