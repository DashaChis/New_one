import random  

def read_f():
    d = {}
    with open ('words.csv') as d:
        word = d.read()
        word_s = word.split()
    d = {word_s[i]:word_s[i+1] for i in range(0, len(word_s), 2)}
    return d


def quest(d):
    attempt = 0
    keys = list(d.keys())
    quest = random.choice(keys)
    print ('Угадай слово: ')
    guess = input(quest+'... ')
    while guess !=d[quest]:
        attempt +=1
        guess = input('Неверно. Попробуй еще раз: ')
    attempt +=1
    print ('Правильно! Ты угадал слово с', attempt, 'попытки')   
    
def main():
    quest(read_f())

if __name__ == '__main__':
    main()
