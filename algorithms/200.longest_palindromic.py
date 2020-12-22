class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""

        result = []
        for mid in range(len(s)):
            result = max(self.is_palindrome(s, mid, mid), result, key=len)
            result = max(self.is_palindrome(s, mid, mid+1), result, key=len)
        return result

    def is_palindrome(self, s, left, right):
        while 0 <= left and right < len(s) and s[left] == s[right]:

            left -= 1
            right += 1

        return s[left + 1:right]

m = Solution()
assert m.longestPalindrome('a') == 'a'
assert m.longestPalindrome("ccc") == "ccc"
assert m.longestPalindrome("abb") == "bb"