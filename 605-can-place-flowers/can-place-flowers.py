class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerBedSize = len(flowerbed)
        count = 0
        for i in range(flowerBedSize):
            if flowerbed[i] == 0:
                free_left = (i == 0) or (flowerbed[i - 1] == 0)
                free_right = (i == flowerBedSize - 1) or (flowerbed[i + 1] == 0)
                if free_left and free_right:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
