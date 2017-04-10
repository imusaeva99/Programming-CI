import re

fname = input('Введите название файла: ')

def openfile(fname):
    with open(fname,'r', encoding='utf-8') as f:
        text = f.read()
        return text

def sentences():
    text = openfile(fname)
    text = text.strip()
    se = re.split('\\b[.!?\\n]+(?=\\s)', text)
    return se

def find8():
    se = sentences()
    greater7 = []
    for i in se:
        words = i.split(' ')
        words = [str(w).strip('?!&(),.:;«»\n”“ ') for w in words]
        greater = []
        greater += [w for w in words if len(w) > 7]
        template = '{} {:->10}'
        for g in greater:
            print(template.format(g,len(g)))
    return 

print(find8())

## я не понимаю, почему в выдачу попали The (два раза – один раз длиной 14, другой 9), ashes, In, hell
