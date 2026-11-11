class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def is_valid(char):
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z' or '0' <= char <= '9':
                return True
            else:
                return False

        while (i < j):
            if not is_valid(s[i]):
                i+=1; continue
            if not is_valid(s[j]):
                j-=1; continue
            if s[i].lower() != s[j].lower():
                # print(s[i], s[j])
                return False
            else:
                i+=1
                j-=1
        return True

            