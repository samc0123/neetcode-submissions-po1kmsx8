class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try: 
                number = int(token)
                stack.append(number)
                continue
            except ValueError:
                val_2 = stack.pop()
                val_1 = stack.pop()
                match token:
                    case "*":
                        stack.append(val_1 * val_2)
                    case "-":
                        stack.append(val_1 - val_2)
                    case "/":
                        stack.append(int(val_1 / val_2))
                    case "+":
                        stack.append(val_1 + val_2)
                print(stack)
        return stack.pop()
                        
