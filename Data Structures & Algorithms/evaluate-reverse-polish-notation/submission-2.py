class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Initialized structures
        stack_nums = []
        operators = set(['*','-','/','+'])

        # Iterate through tokens 

        for token in tokens:
            # if operators, then do math
            if token in operators:
                # Pop two elements 
                element_2 = stack_nums.pop()
                element_1 = stack_nums.pop()

                # Do math
                match token:
                    case '*':
                        stack_nums.append(int(element_1*element_2))
                    case '/':
                        stack_nums.append(int(element_1/element_2))
                    case '-':
                        stack_nums.append(int(element_1-element_2))
                    case '+':
                        stack_nums.append(int(element_1+element_2))
            # Case of just number, then append
            else:
                stack_nums.append(int(token))
        return int(stack_nums.pop())