sentence = input()
while sentence != '.':
    stack = []
    balanced = True
    for ch in sentence:
        if ch == '(' or ch == '[':
            stack.append(ch)
        elif ch == ')' or ch == ']':
            if len(stack) == 0:
                balanced = False
                break
            top = stack.pop()
            if top + ch != '()' and top + ch != '[]':
                balanced = False
                break
    if len(stack) != 0:
        balanced = False
    
    print('yes' if balanced else 'no')
    sentence = input()
