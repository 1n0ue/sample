while True:
    a,op,b = input().split()
    a,b = map(int,[a,b])
    if op == "?":
        break
    elif op == "+":
        print(a+b)
    elif op == "-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        print(a//b)