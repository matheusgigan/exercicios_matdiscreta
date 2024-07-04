def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)

num = int(input("Digite um número para calcular o fatorial: "))
print("O fatorial de", num, "é", fatorial(num))
