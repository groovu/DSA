class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        horz = []
        vert = []
        dir = 0
        # let 0123 = n,e,s,w
        
        for i in instructions:
            if i == 'G':
                #increment horz or vert depending on direction
                if dir == 0:
                    vert.append(1)
                if dir == 1:
                    horz.append(1)
                if dir == 2:
                    vert.append(-1)
                if dir == 3:
                    horz.append(-1)
            if i == 'L':
                dir = (dir + 3) % 4
            if i == 'R':
                # change dir
                dir = (dir + 1) % 4
        
        posX = sum(horz)
        posY = sum(vert)
        
        return (posX == 0 and posY == 0) or dir != 0