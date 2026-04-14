class Solution:
    from collections import Counter
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Take length of s1 and s2 which are strings
        n1, n2 = len(s1), len(s2)

        # If n1 is greater than n2, return false, impossible
        if n1 > n2:
            return False

        # Make a freq map of s1 and s2 only stopping at n1's length
        s1_count = Counter(s1)
        window_count = Counter(s2[:n1])

        # If the maps match, return true
        if s1_count == window_count:
            return True

        # For each time we slide the window from the end of n1 to n2
        for i in range(n1, n2):
            # Add the next character to the window
            window_count[s2[i]] += 1
            # Remove the previous character since it's no longer in the window
            window_count[s2[i-n1]] -= 1

            # Removing the 0's completely
            if window_count[s2[i-n1]] == 0:
                del window_count[s2[i-n1]]

            # If they're true after that, edge case
            if s1_count == window_count:
                return True

        return False
        
    