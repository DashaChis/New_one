import re
def first():
    d1 = {}
    d2 = {}
    l = []
    a = 0
    with open('var1.xml', encoding='utf-8') as f:
        for line in f:
            word = re.findall('type="[^"]*">', line)
            word = str(word)
            word = re.sub('type[=">]*', '', word)
            word = str(word)
            word = re.sub('[">]*', '', word)
            l.append(word)
    n = len(l)
    for i in range (n):
        b = l[i]
        c = l.count(b)
        d2 = {b : c}
        d1.update(d2)
    for key, value in d1.items():
        print(key, value)
    return d1

def main():
    first()
                
if __name__ == '__main__':
    main()
