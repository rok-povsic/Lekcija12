x = int(raw_input("Vnesi stevilo: "))

for i in range(2, x/2 + 1):
    if x % i == 0:
        print i
