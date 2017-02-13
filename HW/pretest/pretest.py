fname = input('Введите название файла: ')

def openfile(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
        text = text.lower()
        text = text.strip()

        words = []
        words = text.split(' ')
    return words

def count_words(fname):
    words = openfile(fname)
    n = 0
    for word in words:
        word = word.strip('?!@#%&*(),.''""<>:;«» \n')
        n += 1
    return n

def dicff(fname):
    words = openfile(fname)
    words.sort()
    fr = dict()
    for index in range(len(words)):
        if words[index] in fr:
            fr[words[index]] += 1
        else:
            fr[words[index]] = 1
    return fr

##with open('results.txt', 'w', encoding='utf-8') as n:
##    n.write(fr)

print(count_words(fname), dicff(fname))
