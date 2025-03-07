class Solution(object):
    # Description
    # Find whether a string s is a subsequence of t. Return True/False
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(s) == len(t) and s == t:
            return True
        elif len(s) == len(t) and s != t:
            return False

        p = 0
        for i in range(len(t)):
            if p == len(s) - 1 and s[p] == t[i]:
                return True
            if t[i] == s[p]:
                p += 1
        
        # Leetcode Best
        def isSubsequence(self, s: str, t: str) -> bool:
            if len(s) > len(t):return False
            if len(s) == 0:return True
            subsequence=0
            for i in range(0,len(t)):
                if subsequence <= len(s) -1:
                    print(s[subsequence])
                    if s[subsequence]==t[i]:

                        subsequence+=1
            return  subsequence == len(s) 
        
        return False

        

sol = Solution()
print(sol.isSubsequence("axc", "ahbgdc"))


    