class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #cases
        # first plot: plant if no plan to right.ArithmeticError
        # last plot: plant if no plant to left
        # midd: plant if no plant to left or right.
        # idea:
        # iterate through each index, look at left and right,
        # plant or no plant.
        # continue until you've planted n plants.
        # if you get to the end of the array and haven't planted n plants, gg cannot plant.
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            else:
                return False
        planted = 0        
        for i in range(len(flowerbed)):

            if i == 0: # first plot
                left = None
                right = flowerbed[1]
                if right == 0 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    planted += 1
            elif i == len(flowerbed) - 1:
                left = flowerbed[len(flowerbed) - 2]
                right = None
                if left == 0 and flowerbed[len(flowerbed) - 1] != 1:
                    flowerbed[i] = 1
                    planted += 1
            else:
                left = flowerbed[i-1]
                right = flowerbed[i+1]
                if left == 0 and right == 0 and flowerbed[i] != 1:
                    flowerbed[i] = 1
                    planted += 1
            
        if planted >= n:
            return True
        else:
            return False