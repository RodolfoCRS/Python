name = str(input("Digit your name. \n -> ")).strip()
count = int(0)
counts = int(0)
uppername = name.upper()
print(f'Name in uppercase: {uppername}')
lowername = name.lower()
print(f'Name in lowercase: {lowername}')
cutname = name.replace(" ", "")
for i in cutname:
    count += 1
print(f'The full name has {count} characters ')
namesplit = name.split()
print(f'The first name has {len(namesplit[0])} characters')

