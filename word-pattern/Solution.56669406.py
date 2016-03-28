class Solution:
    
    def wordPattern(self, pattern, str):
        map_letter_to_word = dict()
        map_word_to_letter = dict()
        
        words = str.split()
        if len(words) != len(pattern):
            return False
        
        for letter, word in zip(pattern, words):
            if letter in map_letter_to_word and map_letter_to_word[letter] != word:
                return False
            if word in map_word_to_letter and map_word_to_letter[word] != letter:
                return False
            
            map_letter_to_word[letter] = word
            map_word_to_letter[word] = letter
        
        return True
