import os, re

def all_f():
    file_list = str(os.listdir())
    return file_list

def choose():
    ans = re.findall(r'\'\b(\w*)([_ ](\w*)){1,}\b\'', all_f())
    return ans

def main():
    names = choose()
    amount = len(names)
    print ('Всего папок: ', amount)
    print (names)
    return amount

if __name__ == '__main__':
    main()
