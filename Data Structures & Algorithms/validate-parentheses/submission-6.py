class Solution:
    def isValid(self, s: str) -> bool:
        '''
        Need to push the open parentheses on the stack 
        When a closed parentheses comes, pop from the stack and make sure 
        the last opening was the correct pair 
        '''

        paren_pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        stack_open = []

        for char in s:
            if char in paren_pairs.keys():
                # Closing parentheses 
                if not stack_open:
                    return False 
                # Pop from stack 
                char_open_pair = stack_open.pop()
                if paren_pairs[char] != char_open_pair:
                    return False
            else:
                stack_open.append(char)
        return True if len(stack_open) == 0 else False