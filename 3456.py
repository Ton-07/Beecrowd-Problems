X = int(input())
print(X)
while X >= 10:
    ud = X % 10
    X = X // 10
    nx = X * 3 + ud
    print(nx)
    X = nx