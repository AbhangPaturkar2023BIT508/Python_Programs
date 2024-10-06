class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        lsen1 = sentence1.split(" ")
        lsen2 = sentence2.split(" ")
        while (len(lsen1) and len(lsen2) and (lsen1[0] == lsen2[0])):
            lsen1.pop(0)
            lsen2.pop(0)

        while (len(lsen1) and len(lsen2) and (lsen1[-1] == lsen2[-1])):
            lsen1.pop()
            lsen2.pop()

        return not lsen1 or not lsen2

        
        # if len(sentence1) < len(sentence2):
        #     prevPos = 0
        #     pos = 0
        #     cnt = 0
        #     for val in lsen1:
        #         if val not in sentence2[pos:]:
        #             return False
        #         else:
        #             prevPos = pos
        #             pos = sentence2.index(val, pos)
        #             cnt+= 1 if (pos - prevPos) > 1 else 0
        #             if cnt > 1 and val != lsen2[-1]:
        #                 return False

        # else:
        #     prevPos = 0
        #     pos = 0
        #     cnt = 0
        #     for val in lsen2:
        #         if val not in sentence1[pos:]:
        #             return False
        #         else:
        #             prevPos = pos
        #             pos = sentence1.index(val, pos)
        #             cnt+= 1 if (pos - prevPos) > 1 else 0
        #             if cnt > 1 and val != lsen1[-1]:
        #                 return False

        return True
        