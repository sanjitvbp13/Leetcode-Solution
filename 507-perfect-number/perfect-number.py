class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=1:
            return False
        
        v =1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                v += i
                if i!=num//i:
                    v+=num//i
                
        return v== num        