class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        str = re.sub('[^a-zA-Z0-9]', '', s)
        return str[:len(str)/2].lower() == str[-1:(len(str) - 1)/2:-1].lower()
