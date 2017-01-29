import re

fname = input('Введите название файла: ')

def openfile(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        text = text.strip()

        words = []
        words = text.split(' ')                 
    return words

def words(fname):
    words = openfile(fname)
    a = []
    for word in words:
        word = word.strip('?!@#%&*(),.''""<>:;«» \n')
        a.append(word)
    return a

regex = r'\bоткр(ыл[аи]?|о(ют?|е(шь|т|м|те))|ыть)\b'

def formsearch(regex):
    wordlist = words(fname)
    match = []
    for i in wordlist:
        i1 = str(i)
        m = re.search(regex, i1)
        if m != None:
            match.append(i)
        strmatch = '\n'.join(match)
    return strmatch

print(formsearch(regex))
