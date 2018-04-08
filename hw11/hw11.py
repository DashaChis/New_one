import re 

def zavr():
    with open ('dino.txt', encoding='utf-8') as f:
        words = f.read()
    return words

def change(words):
    words = re.sub(r'\bДинозавр([ауеыо]?[мвх]?и?)\b', r'Кот\1', zavr())
    words = re.sub(r'\bдинозавр([иауео]?[хмв]?и?)\b', r'кот\1', words)
    return words

def write(words):
    with open ('kotozavr.txt', 'w', encoding='utf-8') as f:
        f.write(words)

def main():
    write(change(zavr()))   

if __name__ == '__main__':
    main()
    return words
