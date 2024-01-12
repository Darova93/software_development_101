def isValid(s: str) -> bool:
    OPENBRACKETS_STACK = []
    for char in s:
        if char in ['(','[','{']:
            OPENBRACKETS_STACK.append(char)
        elif not OPENBRACKETS_STACK:
            return False
        elif char==')' and OPENBRACKETS_STACK[-1]=='(':
            OPENBRACKETS_STACK.pop()
        elif char==']' and OPENBRACKETS_STACK[-1]=='[':
            OPENBRACKETS_STACK.pop()
        elif char=='}' and OPENBRACKETS_STACK[-1]=='{':
            OPENBRACKETS_STACK.pop()
        else:
            return False
    return len(OPENBRACKETS_STACK)==0
