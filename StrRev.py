#User function Template for python3

class Solution:
    def reverseString(self, s):
        # code here
        rev = ''
        for ch in s[::-1]:
            if ch not in rev and ch != ' ':
                rev += ch
        
        return rev



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        
        ob = Solution()
        ans = ob.reverseString(s)
        print(ans)
# } Driver Code Ends