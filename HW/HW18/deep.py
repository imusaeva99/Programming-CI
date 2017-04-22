import os

##Программа должна обходить всё дерево папок, начинающееся с той папки,
##где она находится, и сообщать: 
##какова максимальная глубина папки в этом дереве
##(глубину папки с программой нужно считать равной 0); 

def greatestway():
    depth = []
    for root, dirs, files in os.walk('.', topdown=False):
        a = str(root).count('/')
        if a not in depth:
            depth.append(a)
    return max(depth)
print(greatestway())
