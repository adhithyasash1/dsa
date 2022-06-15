def EvaluateExpression(s):
    string = s.split(' ')
    ans = 0
    stack = [ ]
    for i in string:
        if i.isdigit():
            stack.append(i)
        elif i in '*/+-':
            lol = ''
            B = stack.pop()
            A = stack.pop()
            lol = str(A)+i+str(B)
            ans = eval(lol)
            stack.append(ans)
        elif i == '**':
            lol = ''
            B = stack.pop()
            A = stack.pop()
            lol = str(A)+i+str(B)
            ans = eval(lol)
            stack.append(ans)
    return(ans)

''' 
def EvaluateExpression(exp):
    S = [ ]
    L = exp.split(' ')

    Operand = ['+', '-', '*', '/', '**']

    for i in L:
        if i in Operand:
            pop1 = S.pop()
            pop2 = S.pop()
            k = eval((f"{pop2}{i}{pop1}"))
            S.append((k))

        else:
            S.append(int(i))

    return (S[0])
'''

     
































