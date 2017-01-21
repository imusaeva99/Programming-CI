with open('dict.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    a = dict()
    for line in lines:
        line = line.strip('\n')
        key, value = line.split(':', 1)
        a[key] = value
    for key in a:
        b = input('Угадай слово. Вот подсказка: '+a[key])
        if b == key:
            print('Правильно!')
        else:
            t = 0
            while b != key and t <= (len(key)-1):
                    b = input('Неправильно, попробуй еще раз: ')
                    t += 1
            else:
                print('Правильно!')
