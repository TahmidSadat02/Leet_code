from collections import Counter
class Solution:
    def checkInclusion(self, s1,s2):
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        window1 = Counter(s1)
        window2 = Counter(s2[:n]) # for window

        if window1 == window2:
            return True

        for i in range(n, m):
            window2[s2[i]] += 1 # add another window/char ahead
            window2[s2[i-n]] -= 1 # remove previous 1st window/char
            
            if window2[s2[i-n]] == 0:
                del window2[s2[i-n]]

            if window1 == window2: # checked again the s2 window is == window1 or not
                return True

        return False