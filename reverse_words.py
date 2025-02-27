class Solution(object):
    # Description:
    # Reverse words in a given string
    # Return reversed string
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        new_s = ""
        for i in range(len(words)):
            if i == len(words) - 1:
                new_s += words[i]
            else:
                new_s += words[i]
                new_s += " "


        return new_s
    
    # Leetcode best
    def reverseWordsLeet(self, s):
        """
        :type s: str
        :rtype: str
        """
        New = s.split()
        Val= New[::-1]
        return ' '.join(Val)
    

sol = Solution()
print(sol.reverseWords("  hello world  "))