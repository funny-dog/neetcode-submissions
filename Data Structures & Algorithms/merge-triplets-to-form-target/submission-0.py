class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        curr = [0, 0, 0]
        for a, b, c in triplets:
            if a<=target[0] and b<=target[1] and c <= target[2]:
                curr = [max(curr[0], a), max(curr[1], b), max(curr[2], c)]
        return curr == target