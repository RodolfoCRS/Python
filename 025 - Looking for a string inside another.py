a = str(input('Digit your full name: ')).upper().strip()
b = a.split()
count = 0
for i in b:
    if i == "SILVA":
        print('Your name contains "SILVA" ')
        count += 1
        if count != 0:
            break
if count == 0:
    print('Your name does not contain "SILVA" ')
