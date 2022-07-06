diaria = int(input())
aumento = int(input())
dia = int(input())


def calculo(d, a, n):
    total = 0

    if 1 <= d <= 1000 and 1 <= a <= 1000 and 1 <= n <= 31:
        valor = d + (n - 1) * a
        total = (32 - n) * valor

        if n >= 16:
            total = (32 - n) * (d + (14 * a))
    print(int(total))


calculo(diaria, aumento, dia)