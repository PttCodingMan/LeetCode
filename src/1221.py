class Solution:
    def balancedStringSplit(self, s: str) -> int:

        R, L, result = 0, 0, 0
        for x in s:
            if x == 'L':
                L += 1
            else:
                R += 1
            if R == L:
                result += 1
                R, L = 0, 0

        return result


s = Solution()
result = s.balancedStringSplit("RLRRLLRLRL")
print(result)
