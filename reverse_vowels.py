class Solution(object):
    # Description:
    # In a given string, reverse the order of vowels, whilist keeping anything else where it is and return the string
    # Example: IceCream => AceCreim
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a', 'e', 'i', 'o', 'u']
        # First extract all the vowels in reverse order
        filtered_vowels = []
        for i in range(len(s) - 1, -1, -1):
            if s[i].lower() in vowels:
                filtered_vowels.append(s[i])
        
        # Create a new string and a counter which will track the vowels found
        new_s = ""
        counter = 0
        # Loop through s and find vowels. Instead of appending vowels of s, append vowels of the filtered reversed list of vowels and increment counter
        # If its NOT a vowel, append it normally
        for j in range(len(s)):
            if s[j].lower() in vowels:
                new_s += filtered_vowels[counter]
                counter += 1
            elif s[j].lower() not in vowels:
                new_s += s[j]
        return new_s

    # Leetcode best
    def reverseVowels(self, s):
        # Convert the input string to a character array.
        word = list(s)
        start = 0
        end = len(s) - 1
        vowels = "aeiouAEIOU"
        
        # Loop until the start pointer is no longer less than the end pointer.
        while start < end:
            # Move the start pointer towards the end until it points to a vowel.
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Move the end pointer towards the start until it points to a vowel.
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Swap the vowels found at the start and end positions.
            word[start], word[end] = word[end], word[start]
            
            # Move the pointers towards each other for the next iteration.
            start += 1
            end -= 1
        
        # Convert the character array back to a string and return the result.
        return "".join(word)
        

sol = Solution()
print(sol.reverseVowels("IceCreAm"))
# Output must be: "AceCreIm"