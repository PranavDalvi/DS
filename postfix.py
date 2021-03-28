def postfixEval(s):
    s = s.split()
    stk = []
    for i in range(len(s)):
        if s[i].isdigit():
            stk.append(s[i])
        elif s[i] == "+":
            a1 = stk.pop()
            a2 = stk.pop()

        elif s[i] == "-":
            a1 = stk.pop()
            a2 = stk.pop()

        elif s[i] == "*":
            a1 = stk.pop()
            a2 = stk.pop()
        elif s[i] == "/":
            a1 = stk.pop()
            a2 = stk.pop()
    
    return(stk.pop())

print(postfixEval("23+5*"))
