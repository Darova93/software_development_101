def isValid(s: str) -> bool:
    bracketDict = {'(':')', '[':']', '{':'}'}
    openBracketsStack = []
    for char in s:
        if char in bracketDict:
            openBracketsStack.append(char)
        elif len(openBracketsStack)==0:
            return False
        elif char == bracketDict[openBracketsStack[-1]]:
            openBracketsStack.pop() 
        else:
            return False                   
    return len(openBracketsStack)==0
