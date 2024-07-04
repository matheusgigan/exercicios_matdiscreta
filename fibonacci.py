def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

termos = int(input("Digite o número de termos da sequência de Fibonacci: "))
print("Sequência de Fibonacci:")
for i in range(termos):
    print(fibonacci(i), end=" ")
