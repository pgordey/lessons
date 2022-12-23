n = int(input("Введите N:"))

for i in range(1, 101):
    if i % n == 0:
        print(i)