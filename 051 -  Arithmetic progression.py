print('-=' * 22)
print(' ' * 10 + 'Arithmetic progression')
print('-=' * 22)

first = int(input("First Element: "))
reason = int(input("Reason: "))
n = int(input("How many elements to show?: "))

last = first + (n-1)*reason
last = last + 1

for i in range(first, last, reason):
    print(i)
