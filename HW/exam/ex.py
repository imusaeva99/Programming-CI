import re
import os

##with open('table.csv', 'w', encoding='utf-8') as csv_f:
##    heading_string = 'Файл' + ' ' + 'Автор' + ' ' + 'Тема'
##    csv_f.write(heading_string)

def openfile():
    for root, dirs, files in os.walk('.\\news2'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='Windows-1251') as text:
                file_text = text.read()
                file_text = re.sub('<.*?>', '', file_text)
                file_text2 = file_text.split('.')
                count = len(file_text2)
                print(f, '  ', count)
    return

def meta():
    for root, dirs, files in os.walk('.\\news2'):
        for f in files:
            with open(os.path.join(root, f), 'r', encoding='Windows-1251') as text:
                file_text = text.read()
                writer = re.match('<meta content="(.*?)" name="author"/>', file_text).group(1)
                topic = re.match('<meta content="(.*?)" name="topic"/>', file_text).group(1)
            with open('.\\table.csv', 'w', encoding='utf-8') as csv_f:
                heading_string = 'Файл' + ' ' + 'Автор' + ' ' + 'Тема'
                csv_f.write(heading_string)

            with open('.\\table.csv', 'a', encoding='utf-8') as csv_writer:
                string = f + '  ' + writer + '  ' + topic
                csv_writer.write(string)
    return

print(openfile())
print(meta())
