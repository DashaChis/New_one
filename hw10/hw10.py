import re 

with open ('platan1.html', encoding='utf-8') as f:
    words = f.read().lower()
match = re.findall('семейство:.*\(<', words)
match = ''.join(match) 
res = re.findall('[^семейство:].*', match)
res = ''.join(res) 
res = re.findall('[а-я]', res)
res = str(res)
with open('Семейство.txt', 'w', encoding='utf-8') as f:
    f.write(res) 
print (res)

