class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        decode = [encoded[0]]
        for i in range(0, len(encoded)):
            decode.append(decode[i]^encoded[i])
        return decode

        