# считаем tf, потом idf, tf-idf, tf-idf для каждого слова в каждом тексте
# берем 5 слов с минимальным значением

import os
import re
from math import log

punct = '[.,!«»?&@"$\[\]\(\):;%#&\'—-]'
tabs = '[\t\n]'

def preprocessing(text): # функция предобработки текста
    text_wo_punct = re.sub(punct, '', text.lower()) # удаляем пунктуацию, приводим в нижний регистр
    text_wo_punct = re.sub(tabs, ' ', text_wo_punct)
    words = text_wo_punct.strip().split() # делим по пробелам
    return words

def count_tf(word, text):
    n = text.count(word)
    return n / len(text)

def count_df(word, texts):
##    i = 0
##    for text in texts:
##        if word in text:
##            i += 1
    i = [1 for text in texts if word in text]
    i = sum(i)
    return i

def count_idf(word, texts):
    df = count_df(word, texts)
    try:
        idf = len(texts) / df
    except ZeroDivisionError:
        return 0
    return idf

def count_tfidf(word, text, texts):
    tf = count_tf(word, text)
    idf = count_idf(word, texts)
    tfidf = log(tf, 10)*log(idf, 10)
    return tfidf

def keywords(text, texts):
    keywords = {}
    dic_tfidf = {}
    for word in text:
        if word in dic_tfidf:
                continue
        tfidf = count_tfidf(word, text, texts)
        dic_tfidf[word] = tfidf
    i = 0
    for el in sorted(dic_tfidf, key= lambda x: dic_tfidf[x]):
        if i > 5:
            break
        i += 1
        keywords[el] = dic_tfidf[el]
    return keywords

def main():
    texts = {}
    for root, dirs, files in os.walk('wikipedia'):
        for f in files:
            with open(os.path.join(root,f), 'r', encoding='utf-8') as t:
                content = t.read()
                text = preprocessing(content)
                texts[f] = text
    raw_texts = list(texts.values())
    for t in texts:
        print('\nИзвлекаем ключевые слова для текста {}'.format(t))
        kwords = keywords(texts[t], raw_texts)
        for key in kwords:
            print(key, kwords[key])

if __name__ == '__main__':
    main()       
