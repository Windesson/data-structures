class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""
        for i in range(32):
            if n % 2:
                binary += "1"
            else:
                binary += "0"
            n = n >> 1
        
        res = 0
        step = 1
        for i in range(31, -1, -1):
            if binary[i] == "1":
                res += step
            if step == 1:
                step = 2
            else: 
                step = step * 2

        return res



        