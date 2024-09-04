class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0
        currPos = [0, 0]
        currDir = 0
        obstacles=set(map(tuple,obstacles))

        for command in commands:
            if command == -1:
                currDir = (currDir + 1) % 4
                continue
            if command == -2:
                currDir = (currDir + 3) % 4
                # continue

            direction = directions[currDir]
            for i in range(command):
                nextX = direction[0] + currPos[0]
                nextY = direction[1] + currPos[1]
                # if (nextX, nextY) in obstacles:
                #     break
                if obstacles.count([nextX, nextY]) > 0:
                    break
                currPos[0] = nextX
                currPos[1] = nextY
            
            res = max(res, currPos[0] * currPos[0] + currPos[1] * currPos[1])
        
        return res