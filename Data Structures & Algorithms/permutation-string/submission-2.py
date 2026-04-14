class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        # print(k)

        if k > len(s2):
            return False

        sorted_string = ''.join(sorted(s1))

        for i in range(len(s2) - k + 1):
            substring = s2[i:i+k]
            sorted_substring = ''.join(sorted(substring))

            print(sorted_substring)
            print(sorted_string)
            if (sorted_substring == sorted_string):
                return True

        return False
    