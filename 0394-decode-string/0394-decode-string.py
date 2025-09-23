class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            if char.isdigit():
                # Accumulate the number (k)
                current_num = current_num * 10 + int(char)
            elif char == "[":
                # Push current number and string to stack
                stack.append((current_num, current_str))
                # Reset for the next substring
                current_num = 0
                current_str = ""
            elif char == "]":
                # Pop the top from stack (last number and string)
                prev_num, prev_str = stack.pop()
                # Repeat the current string `prev_num` times and append it to `prev_str`
                current_str = prev_str + current_str * prev_num
            else:
                # Append the current character to the string
                current_str += char
        
        return current_str
