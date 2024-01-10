def isValid(s: str) -> bool:
    OPENBRACKETS_STACK = []
    for i in s:
        if i in ['(','[','{']:
            OPENBRACKETS_STACK.append(i)
        elif not OPENBRACKETS_STACK:
            return False
        elif i==')' and OPENBRACKETS_STACK[-1]=='(':
            OPENBRACKETS_STACK.pop()
        elif i==']' and OPENBRACKETS_STACK[-1]=='[':
            OPENBRACKETS_STACK.pop()
        elif i=='}' and OPENBRACKETS_STACK[-1]=='{':
            OPENBRACKETS_STACK.pop()
        else:
            return False
    return not OPENBRACKETS_STACK
