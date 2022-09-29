a = str(input('Type a sentence: ')).upper().strip()
print('The letter "A" appears {} times in the sentence'.format(a.count("A")))
print('The first letter "A" appears in the {}º position.'.format(a.find("A")+1))
print('The last letter "A" appears in the {}º position.'.format(a.rfind("A")+1))