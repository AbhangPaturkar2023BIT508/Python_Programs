class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gain = [0] + gain
        high_altitude = 0
        for i in range(1, len(gain)):
            alti = gain[i-1] + gain[i]
            gain[i] = alti
            if high_altitude < alti:
                high_altitude = alti
        return high_altitude