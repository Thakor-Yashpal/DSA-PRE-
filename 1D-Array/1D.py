class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i, j = 0, 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result.append(word1[i])
                i += 1
            if j < len(word2):
                result.append(word2[j])
                j += 1
        return ''.join(result)

sol = Solution()
print(sol.mergeAlternately("abc", "pqr")) 



# redoing the code

class another_soluction(object):
    def one_more (slef,word01,word02):
        result = []
        i,j = 0,0
        
        for i in range((len(word01) + len(word02))):
            if i <len(word01):
                result.append(word01[i])
            if j < len(word02):
                result.append(word02[j])
                j += 1
        return ''.join(result)

sol = another_soluction()
print(sol.one_more("abc", "pqr"))