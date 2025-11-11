# My solution
# def check_parathesis(s):
#     stack = []
#     pairs = {")": "(", "]": "[", "}":"{"}
#     valid = True

#     for i in s:
#         if i == "(" or i == "[" or i == "{":
#             stack.append(i)
#         elif i == ")" or i == "]" or i == "}":
#             top = stack.pop()
#             if top != pairs[i]:
#                 valid = False

#     if valid and not stack: #len is not 0
#         return True
#     else:
#         return False

# print(check_parathesis("()"))
# print(check_parathesis("()[]{}"))
# print(check_parathesis("(]"))
# print(check_parathesis("([])"))
# print(check_parathesis("([)]"))

# AI solution:
def isValid(s: str) -> bool:
    """
    Determines if the input string s containing just the characters '(', ')', 
    '{', '}', '[' and ']' is valid.

    Args:
        s: The input string of parentheses.

    Returns:
        True if the string is valid, False otherwise.
    """
    
    # Use a list as a stack
    stack = []
    
    # Map for quick lookup of matching brackets
    # Key: closing bracket, Value: opening bracket
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        # 1. If the character is a closing bracket
        if char in mapping:
            
            # Check if the stack is not empty AND 
            # if the top element of the stack matches the required opening bracket.
            # If the stack is empty (e.g., s = "])"), we use a placeholder 
            # to prevent an error, which will fail the match check.
            top_element = stack.pop() if stack else '#'
            
            if mapping[char] != top_element:
                return False
                
        # 2. If the character is an opening bracket, push it onto the stack
        else:
            stack.append(char)
            
    # 3. After iterating through the string, the stack must be empty for the string to be valid.
    # An empty stack means every open bracket was correctly closed.
    return not stack

# --- Examples ---

print(f'Input: "()", Output: {isValid("()")}')               # Expected: True
print(f'Input: "()[]{{}}", Output: {isValid("()[]{{}}")}')   # Expected: True
print(f'Input: "(]", Output: {isValid("(]")}')               # Expected: False
print(f'Input: "([])", Output: {isValid("([])")}')           # Expected: True
print(f'Input: "([)]", Output: {isValid("([)]")}')           # Expected: False
print(f'Input: "{{[()]}}", Output: {isValid("{{[()]}}")}')   # Expected: True
print(f'Input: "[", Output: {isValid("[")}')                 # Expected: False
print(f'Input: "}}", Output: {isValid("}}")}')               # Expected: False