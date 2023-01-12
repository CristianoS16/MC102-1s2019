#imprime uma matriz *, com + em i = j
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        d = 1
        if d < n+1:
            if i==j:
                print("+", end='')
                d = d + 1
            else:
                print("*", end='')
                d = d +1
    print("\n")
