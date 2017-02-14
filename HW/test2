import re

def openf():
    with open('F.xml', 'r', encoding='utf=8') as f:
        lines = f.readlines()
    return lines

def countli():
    lines = openf()
    linecount = 0
    for line in lines:
        linecount += 1
    results = 'result.txt'
    with open(results, 'w', encoding='utf-8') as n:
        n.write(str(linecount))
    return results

def dicfreq():
    lines = openf()
    types = []
    for line in lines:
        l = str(line)
        if 'lemma' in l:
            reg = re.search(r'<w lemma="(.*?)" type="(.*?)">', l)
            types.append(reg.group(2))

    freq = {}
    for i in range(len(types)):
        if types[i] not in freq:
            freq[types[i]] = 1
        else:
            freq[types[i]] += 1

    with open('keys.txt', 'w', encoding='utf-8') as te:
        te.write('\n'.join(freq.keys()))
    return freq

print(countli(), dicfreq())
