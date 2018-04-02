import re 

with open ('platan.html', encoding='utf-8') as f:
    words = f.read().lower()
match = re.sub('<.*?>|[&#;\d]|[a-z]', '', words)
match = re.findall('семейство:.*род:', match)
match = ''.join(match)
match = str(match)
res = re.search('[^семейство:][\S]*', match)
res = ''.join(res.group())
with open('Семейство.txt', 'w', encoding='utf-8') as f:
    f.write(res)



