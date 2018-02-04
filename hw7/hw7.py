def read_f(title):
   with open (title, encoding='utf-8') as f:
       text = f.read()
       splited = text.split()
       return splited
   
def ous_f(splited):
    ous = {'количество:': 0, 'средняя длина:': 0}
    for word in splited:
         if word[-3:] == 'ous':
             ous['количество:'] += 1
             ous['средняя длина:'] += len(word)
    return ous

def res(ous):
    if ous['количество:'] != 0:
        mid_length = int(ous['средняя длина:'])//int(ous['количество:'])
        ous['средняя длина:'] = mid_length
        for key, value in ous.items():
            print (key, value)
    else:
        print ('Нет слов, заканчивающихся на -ous.')


def main():
    title = str(input('Напишите название:'))
    if title != '':
        title = title + '.txt'
        print(res(ous_f(read_f(title))))
    else: print('Вы ничего не ввели.')

if __name__ == '__main__':
    main()
