class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here

        if not target:
            return 0

        if target not in source:
            return -1

        target_length = len(target)
        for i in range(len(source)):
            if source[i:i + target_length] == target:
                return i

        return -1

answer = Solution()
assert answer.strStr("source", "target") == -1
assert answer.strStr("abcdabcdefg", "bcd") == 1
assert answer.strStr("abcdabcdefg", "") == 0
assert answer.strStr("", "") == 0