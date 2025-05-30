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