class Solution:
    
    def is_vowel(self, c):
        vowels = {"a", "e", "i", "o", "u"}
        return c.lower() in vowels

    def reverseVowels(self, s):
        left = 0
        right = len(s) - 1
        s = list(s)
        
        while left < right:
            while left < right and not self.is_vowel(s[left]):
                left += 1
            while left < right and not self.is_vowel(s[right]):
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)
