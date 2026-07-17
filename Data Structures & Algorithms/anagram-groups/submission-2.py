class Solution:
    def sortWord(self, word):
        characters = list(word)
        for i in range(1, len(characters)):
            current = characters[i]
            j = i - 1
            while j >= 0 and characters[j] > current:
                characters[j + 1] = characters[j]
                j -= 1
            characters[j + 1] = current
        sorted_word = ""
        for char in characters:
            sorted_word += char
        return sorted_word

    def groupAnagrams(self, strs):
        anagrams = {}
        for word in strs:
            sorted_word = self.sortWord(word)
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        result = []
        for key in anagrams:
            result.append(anagrams[key])
        return result
        