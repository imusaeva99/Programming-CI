fname = input('Введите название файла: ')

def openfile(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        text = text.strip()

        words = []
        words = text.split(' ')
    return words
        
def ingform(fname):
    words = openfile(fname)
    a = []
    for word in words:
        word = word.strip('?!@#%&*(),.''""<>:;«» \n')
        if word.endswith('ing'):
            a.append(word)
        else:
            continue
    return a

theword = input('Введите слово: ')
def searching(theword):
    s = ingform(fname)
    b = 0
    for i in s:
        if i == theword:
            b += 1
        else:
            continue
    return b

print(ingform(fname))
print(searching(theword))
