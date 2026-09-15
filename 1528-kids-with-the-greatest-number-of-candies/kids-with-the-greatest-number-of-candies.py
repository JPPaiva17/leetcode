class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        booleanArray = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                booleanArray.append(True)
            else:
                booleanArray.append(False)
        return booleanArray

            