class Solution:
    def isAnagram(self,s,t):
        count={}
        if (len(s)!=len(t)):
            return False
        for i in range(len(s)):
            current=s[i]
            if current in count:
                count[current]+=1
            else:
                count[current]=1
        for i in range(len(t)):
            current=t[i]
            if current not in count:
                return False
            if count[current]==0:
                return False
            else:
                count[current]-=1
        return True
        
        