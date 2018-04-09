import re

def count():
    a = 0
    with open('var1.xml', encoding='utf-8') as f:
        for line in f:
            a += 1
            word = re.search('</teiHeader>', line)
            if word:
                word.group()
                break
    a = str(a)
    print (a)
    return a

def main():
    with open('answer.txt', 'w', encoding='utf-8') as w:
        w.write(count())
                
if __name__ == '__main__':
    main()
