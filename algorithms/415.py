class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here

        if not s:
            return True

        string = "".join([letter.lower() for letter in s if letter.isalnum()])


        mid = len(string) // 2
        if string[:mid] == string[mid+1:][::-1]:
            return True

        if string[:mid] == string[mid:][::-1]:
            return True

        return  False

answer = Solution()
assert answer.isPalindrome('A man, a plan, a canal: Panama') == True
assert answer.isPalindrome('aa') == True
assert answer.isPalindrome("race a car") == False


