class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ttlReqEne = 0
        ttlReqExe = 0
        # // 5 - 4 
        # // [1,4,3,2]
        for i in range(len(energy)):
            if initialEnergy <= energy[i]:
                reqEne = ((energy[i]+1) - initialEnergy)
                initialEnergy += reqEne
                ttlReqEne += reqEne

            if initialExperience <= experience[i]:
                reqExe = ((experience[i]+1) - initialExperience)
                initialExperience += reqExe
                ttlReqExe += reqExe
            
            initialEnergy -= energy[i]

            initialExperience += experience[i]
        
        return ttlReqEne+ttlReqExe