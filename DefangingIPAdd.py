class Solution(object):
    def defangIPaddr(self, address):
        str = ""
        for ch in address:
            if ch == '.':
                str += '[.]'
            else:
                str += ch
        
        return str
        """
        :type address: str
        :rtype: str
        """
        