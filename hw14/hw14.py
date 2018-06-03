import re

def get_data(filename):
    raw = ''
    with open(filename, encoding='cp1251') as f:
        raw = f.read()
    print(raw[:50])
    return raw


def preprocess(text):
    tokens = re.split('[^\w-]+', text)
    tokens = [word.lower() for word in tokens]
    tokens = [re.sub(word, word+' ', word) for word in tokens]
    return tokens


def replace_letters(tokens):
    replet = [re.sub(letter, letter*word.count(letter), letter) for word in tokens for letter in word]
    replet = ''.join(replet)  
    print(replet)


raw_text = get_data('sample.txt')
clean_tokens = preprocess(raw_text)
replace_letters(clean_tokens)
