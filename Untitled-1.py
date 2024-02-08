class Solution:
    def reverseVowels(self, s: str) -> str:
        # Convert the string to a list for easier manipulation
        s_list = list(s)
        
        # Define vowels including both lowercase and uppercase
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        # Initialize pointers
        left, right = 0, len(s) - 1

        while left <= right:
            # Convert characters to lowercase for comparison
            char_left = s_list[left].lower()
            char_right = s_list[right].lower()

            if char_left in vowels and char_right in vowels:
                # Swap vowels
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif char_left in vowels:
                # Move right pointer if right character is not a vowel
                right -= 1
            else:
                # Move left pointer if left character is not a vowel
                left += 1

        # Convert the list back to string
        return ''.join(s_list)

# Example usage:
sol = Solution()
result = sol.reverseVowels("eccbA")
print(result)  # Output: "AccbA"








