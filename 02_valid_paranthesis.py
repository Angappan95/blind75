'''
Given a string containing only (), {}, and [], determine whether the brackets are valid.

A valid string must satisfy:

Every opening bracket has a matching closing bracket.
Brackets close in the correct order.
s = "{[()]}"

# Output: True
'''

def is_valid_paranthesis_brute_force(string):
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '')
        string = string.replace('[]', '')
        string = string.replace('{}', '')
    return string == ''

def is_valid_paranthesis_stack_check(string):
    stack = []

    for ch in string:
        if ch in '({[':
            stack.append(ch)
    
        elif ch  == ')':
            if not stack or stack.pop() != '(':
                return False
        elif ch == ']':
            if not stack or stack.pop() != '[':
                return False
        elif ch == '}':
            if not stack or stack.pop() != '{':
                return False
    return len(stack) == 0

def is_valid_paranethesis_stack_optimised(string):
    mappings = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for ch in string:
        if ch in mappings:
            if not stack or stack.pop() != mappings[ch]:
                return False
        else:
            stack.append(ch)
    
    return len(stack) == 0

print(is_valid_paranethesis_stack_optimised('{[()]}'))
print(is_valid_paranethesis_stack_optimised('{[()}]}'))