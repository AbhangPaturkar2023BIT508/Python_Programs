class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxReleaseTime = releaseTimes[0]
        key = keysPressed[0]

        for i in range(1, len(keysPressed)):
            currKeyRelTime = releaseTimes[i] - releaseTimes[i-1]
            if maxReleaseTime ==  currKeyRelTime:
                key += keysPressed[i]
            elif maxReleaseTime < currKeyRelTime:
                maxReleaseTime = currKeyRelTime
                key = keysPressed[i]
        
        return max(key)