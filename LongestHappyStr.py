class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        n = a+b+c
        curr_a_cnt = 0
        curr_b_cnt = 0
        curr_c_cnt = 0
        s = ''
        
        for i in range(n):
            if (a >= b and a >= c and curr_a_cnt != 2) or (a>0 and(curr_c_cnt == 2 or curr_b_cnt == 2)):
                s+='a'
                a-=1
                curr_a_cnt += 1
                curr_b_cnt = 0
                curr_c_cnt = 0

            elif (b >= a and b >= c and curr_b_cnt != 2) or (b>0 and (curr_a_cnt == 2 or curr_c_cnt == 2)):
                s+='b'
                b-=1
                curr_b_cnt += 1
                curr_a_cnt = 0
                curr_c_cnt = 0

            elif (c >= a and c >= b and curr_c_cnt != 2) or (c>0 and (curr_a_cnt == 2 or curr_b_cnt == 2)):
                s+='c'
                c-=1
                curr_c_cnt += 1
                curr_a_cnt = 0
                curr_b_cnt = 0
        return s
            
