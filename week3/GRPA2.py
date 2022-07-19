'''
An arithmetic expression can be written in postfix form where each operator appears after the
operands.

For example:

A + B is written as A B +
(A + B) * (C - D) is written as A B + CD - *.
The expressions written in the given form are easier to evaluate compared to normal expressions,
as parenthesis are not required.
A postfix expression can be evaluated with a stack using the following algorithm :

. Create a stack to store operands (or numbers).
Scan each element in the given expression left to right.
. If the element is a number (operand), push it into the stack.
. If the element is an operator, pop two operands (Assume that the first popped element
is B and the second popped element is A ) for the operator op from the stack.
Evaluate the operation ( A op B ) and push the result back to the stack.

When the expression is ends, the number in the stack is the final answer.

Write a function EvaluateExpression(exp), that accepts an
expression exp in string format,
where each items are separated by the space. The function returns the evaluated value.

Note: Assume that the expression has only + , - , * , / and ** operators.
'''

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

# Solution 2

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

# Solution 3

class create_stack:
  def __init__(self):
    self.stack = []
  def push(self,d):
    self.stack += [d]
  def pop(self):
    t = self.stack[-1]
    self.stack = self.stack[:-1]
    return t

def EvaluateExpression(exp):
  opt = ['+','-','*','/','**']
  stk = create_stack()
  L = exp.split(' ')
  for i in L:
    if i not in opt:
      stk.push(i)
    else:
      b = stk.pop()
      a = stk.pop()
      res = eval(a + i + b)
      stk.push(str(res))
  return stk.pop()
print(float(EvaluateExpression(input())))

     
