class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        for num in sorted(count.keys()):
            if count[num] > 0:
                tmp = count[num]
                for i in range(groupSize):
                    if count[num+i] < tmp:
                        return False
                    count[num+i] -= tmp
        return True