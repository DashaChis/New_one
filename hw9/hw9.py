import re
with open ('eda.txt', encoding='utf-8') as f:
    words = f.read().lower()
    first_step = re.findall('съе[влш][а-я,-]*|съемс?[ я]|съеден[аоы|н][\S]*|съеден[\W]|съед[яи][\w]{1,2}|съест[^н][\S]*|съест\b', words)
answer = ' '.join(first_step)
answer = re.sub('[^-\w\s]', '', answer)
print (answer)
