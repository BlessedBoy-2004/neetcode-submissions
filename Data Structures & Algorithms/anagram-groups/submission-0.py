class Solution:
    def groupAnagrams(self,strs):
        anagrams:dict[str,list[str]]={}
        for words in strs:
            sorted_words="".join(sorted(words))
            if sorted_words in anagrams:
                anagrams[sorted_words].append(words)
            else:
                anagrams[sorted_words]=[words]
        return list(anagrams.values())
        