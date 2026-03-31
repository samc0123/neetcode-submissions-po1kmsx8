class Solution:
    def isValid(self, s: str) -> bool:
        # Fundamentals of a stack 
        # Push -> add to the end 
        # Pop -> pull from the end
        # Peek -> take a look at the last element (stack[-1])

        # Initial operation, convert string to stack 
        stack_s = []
        for char in s:
            stack_s.append(char)

        # Setup stack for tracking close chars since operating from back 
        stack_close = []

        # Setup hashmap for mapping open to close chars
        open_to_close_chars = {
            '(':')',
            '[':']',
            '{':'}'
        }

        # Special case <2 elements 
        if len(stack_s) < 2:
            return False

        # Iterate through `stack_s`:
        while stack_s:
            c = stack_s.pop()
            # If closing character, add to `stack_close`
            if c in open_to_close_chars.values():
                stack_close.append(c)
            # If opening character, pop from stack and compare 
            elif c in open_to_close_chars.keys() and len(stack_close)>0:
                last_close_char = stack_close.pop()
                # If not a match, fail 
                if open_to_close_chars[c] != last_close_char:
                    return False
            elif c in open_to_close_chars.keys() and len(stack_close) == 0:
                return False # no matching closing character for opening character
        if len(stack_s) == 0 and len(stack_close) == 0:
            return True
        else:
            return False
                


        

