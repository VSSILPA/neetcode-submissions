class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_freq = [0] * 26
        for char in s1:
            s1_freq[ord('a') - ord(char)] += 1

        s2_freq = [0] * 26
        for char in s2[0:len(s1)]:
            s2_freq[ord('a') - ord(char)] += 1

        if s1_freq==s2_freq:
            return True

        L=0
        for R in range(len(s1), len(s2)):
            print(R)
            if R-L+1 > len(s1):
                s2_freq[ord('a') - ord(s2[L])] -= 1
                L+=1 

            s2_freq[ord('a') - ord(s2[R])] += 1
          
            if s1_freq == s2_freq:
                return True

        return False






