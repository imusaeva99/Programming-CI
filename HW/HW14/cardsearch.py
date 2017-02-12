import re

fname = input('Введите название файла: ')

def open_html(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def find_capital(fname):
    text = open_html(fname)
    card = re.search(r'<table class="infobox">', text)
    if card != None:
        capital = re.search(r'data-wikidata-property-id="P36"(.*?)<a href=(.*?)>(.*?)</a>', text)
        if capital != None:
            return capital.group(3)

def find_country(fname):
    text = open_html(fname)
    card = re.search(r'<table class="infobox">', text)
    if card != None:
        country = re.search(r'>(.*?)</h1>', text)
        if country != None:
            return country.group(1)

print('Страна: ', find_country(fname), 'Столица: ', find_capital(fname))


