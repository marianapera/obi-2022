idade1 = int(input("Idade 1: "))
idade2 = int(input("Idade 1: "))


def ingresso(var1, var2):
    total = 0

    if 1 <= var1 <= 100 and 1 <= var2 <= 100:
        if var1 <= 17 or var2 <= 17:
            total += 15

        if 59 >= var1 >= 18 or 59 >= var2 >= 18:
            total += 30

        if var1 >= 60 or var1 >= 60:
            total += 20
        print(f"Total: {total}")


ingresso(idade1, idade2)
