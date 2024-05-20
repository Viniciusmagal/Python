m = int(input("Quantas linhas vai ter na matriz: "))
n = int(input("Quantas colunas vai ter na matriz: "))

mat: [[int]] = [[0 for x in range(n)] for x in range(m)]

for i in range(0, m):
    for j in range (0, n):
        mat[i][j] = int(input(f"elemento[{i}, {j}]: "))
        print()
        print("matriz digitada: ")
        for i in range(0, m):
            for j in range(0, n):
                print(f"{mat[i][j]} ", end="")
            print()
