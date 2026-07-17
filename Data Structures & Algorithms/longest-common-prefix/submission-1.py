class Solution:
    def longestCommonPrefix(self,strs):
        if not strs:
            return ""
        first_word=strs[0]
        for i in range(len(first_word)):
            char_to_match=first_word[i]
            for j in range(1,len(strs)):
                current_word=strs[j]
                if i>=len(current_word) or char_to_match!=current_word[i]:
                    return first_word[:i]
        return first_word






        