class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instr = instructions * 4
        x = y = 0
        direction = 0
        
        for i in instr:
            if i == "G":
                if direction == 0:
                    y += 1
                if direction == 1:
                    x += 1
                if direction == 2:
                    y -= 1
                if direction == 3:
                    x -= 1
            if i == "L":
                direction = (direction - 1) % 4
            if i == "R":
                direction = (direction + 1) % 4
        
        if (x == 0 and y == 0):
            return True
        return False