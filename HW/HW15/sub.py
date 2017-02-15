import re

fname = input('Введите название файла: ')

def open_html(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    te = re.sub(u'<.*?(".*?")?.*?>', u'', text, flags = re.U)
    te2 = re.sub(u'<script>.*?</script>', u'', te, flags = re.U)
    te3 = re.sub(u'<style>.*?</style>', u'', te2, flags = re.U)
    te4 = re.sub(u'<head>.*?</head>', u'', te3, flags = re.U)
    return te4

def changeform(fname):
    te = open_html(fname)
    change1 = re.sub(u'комар(у|е|ы|а(х|м|ми)?|о(м|в))?', u'слон\\1', te, flags = re.U)
    change2 = re.sub(u'Комар(у|е|ы|а(х|м|ми)?|о(м|в))?', u'Слон\\1', change1, flags = re.U)
    with open('results.txt', 'w', encoding='utf-8') as n:
        n.write(change2)
    return 'Готово! Результаты в файле results.txt .'

print(changeform(fname))
