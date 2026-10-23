number = int(input())

for n1 in range(1, number + 1):
    print(" " * (number - n1) + " ".join("*" * n1))

for n2 in range(number - 1, 0, -1):
    print(" " * (number - n2) + " ".join("*" * n2))
