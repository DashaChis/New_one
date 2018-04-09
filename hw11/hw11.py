import re 

def zavr():
    with open ('dino.txt', encoding='utf-8') as f:
        words = f.read()
    return words

def change(words):
    words = re.sub(r'\bДинозавр([аыуе]?)\b', r'Кот\1', zavr())
    words = re.sub(r'\bдинозавр([ыауе]?)\b', r'кот\1', words)
    words = re.sub(r'\bДинозавр(ах)\b', r'кот\1', words)
    words = re.sub(r'\bдинозавр(ах)\b', r'кот\1', words)
    words = re.sub(r'\bДинозавр(ов)\b', r'Кот\1', words)
    words = re.sub(r'\bдинозавр(ов)\b', r'кот\1', words)
    words = re.sub(r'\bДинозавр(ами)\b', r'Кот\1', words)
    words = re.sub(r'\bдинозавр(ами)\b', r'кот\1', words)
    words = re.sub(r'\bДинозавр(ам)\b', r'Кот\1', words)
    words = re.sub(r'\bдинозавр(ам)\b', r'кот\1', words)
    words = re.sub(r'\bДинозавр(ом)\b', r'Кот\1', words)
    words = re.sub(r'\bдинозавр(ом)\b', r'кот\1', words)
    return words

def write(words):
    with open ('kotozavr.txt', 'w', encoding='utf-8') as f:
        f.write(words)

def main():
    write(change(zavr()))   

if __name__ == '__main__':
    main()
