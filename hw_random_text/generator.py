import random


def verb(number):
    with open("verbSg.txt") as vs:
     text = vs.read()  
     sing_verb = text.split()
    with open("verbPl.txt", encoding=('utf-8')) as vp:
     text = vp.read()  
     plur_verb = text.split()
#  sing_verb = ['видел', 'шептал', 'слышал', 'не понимал','знал', 'думал','верил','читал','рассказывал','писал','кричал','пел','бормотал','бредил']
#  plur_verb = ['плакали','пели','смеялись','танцевали','падали','взлетали','горели','дышали','манили','ускользали']
    if number == 's':
     return random.choice(sing_verb)
    return random.choice(plur_verb)

def noun(number):
    with open("nounSg.txt", encoding=('utf-8')) as f:
     text = f.read()  
     singular_nouns = text.split()
    with open("nounPl.txt") as np:
     text = np.read()  
     plural_nouns = text.split()  
#  singular_nouns = ['зверь', 'Снусмумрик', 'вереск', 'город', 'ветер','герой','я','свет','снег','голос','странник','друг','старик','тот','он', 'рыбак','конь','лес','Пушкин']
#  plural_nouns = ['глаза', 'люди', 'крыши', 'дома','деревья','руки','дожди','лестницы','корабли','огни','шелка','взгляды','вещи','чувства','печали']
    if number == 's':
     return random.choice(singular_nouns)
    return random.choice(plural_nouns)

def adverb():
    with open("adverbs.txt") as f:
     text = f.read()  
     adverbs1 = text.split()
   #adverbs = ['плоско','тихо','звонко','медленно','нежно','кучеряво','протяжно','странно','уютно','скрипуче','ласково', 'безмятежно']
     return random.choice(adverbs1)

def compar_adjective():
    with open("compare.txt", encoding=('utf-8')) as c:
     text = c.read()  
     compar_adj = text.split()
 #    compar_adj = ['ярче','чище','больше','выше','чернее','смешнее','глубже','красивее','легче','светлее']
     return random.choice(compar_adj)

def question():
    with open("question.txt", encoding=('utf-8')) as q:
     text = q.read()  
     quest = text.split()
#  quest = ['разве','неужели','отчего же','почему']
     return random.choice(quest)

def infinitive():
    with open("infinitive.txt", encoding=('utf-8')) as i:
     text = i.read()  
     inf = text.split()
#  inf = ['убегать','идти','падать','улетать','прыгать','уходить','ползти','уезжать','стремиться','удалиться','спускаться']
     return random.choice(inf)


def conjunction():
    with open("conjunction.txt", encoding=('utf-8')) as con:
     text = con.read()  
     conjunctions = text.split()
#  conjunctions = ['что','когда','как']
    return random.choice(conjunctions)

def adjective():
    with open("adjective.txt", encoding=('utf-8')) as ad:
     text = ad.read()  
     adj = text.split()
 # adj = ['сини','деревянны','маленьки','стеклянны','механически','левы','чайны','прозрачны','холодны','мокры', 'безымянны']
    return random.choice(adj)

def just_conj():
    with open("just_conj.txt", encoding=('utf-8')) as j:
     text = j.read()  
     conj = text.split()
 # conj = ['а', 'и', 'но']
    return random.choice(conj)

def time():
    with open("time.txt", encoding=('utf-8')) as t:
     text = t.read()  
     words = text.split()
#  words = ['когда-то','вчера','в пять часов вечера','утром','раньше','ночью','днем','тогда']
    return random.choice(words)

def preposition():
    with open("prepos.txt", encoding=('utf-8')) as pr:
     text = pr.read()  
     prepos = text.split()
#  prepos = ['из','от','из-под']
    return random.choice(prepos)

def gen_noun():
    with open("gen.txt", encoding=('utf-8')) as g:
     text = g.read()  
     gen = text.split()
#  gen = ['дверей','полей','морей','лесов','комнат','окон','людей','мира','себя']
     return preposition() +' ' + random.choice(gen)
  

def clause():
  clauses = random.choice(['s', 'p'])
  if clauses == 's':
    return noun('s') + ' ' + verb('s')
  else:
    return noun('p') + ' ' + verb('p')

def rand_noun():
  rand_nouns = random.choice(['s', 'p'])
  if rand_nouns == 's':
    return adjective() + 'й ' + noun('s')
  else:
    return adjective()+'е '+ noun('p')

def cause_conjunction():
    with open("cause.txt", encoding=('utf-8')) as cc:
     text = cc.read()  
     cause_conj = text.split()
#  cause_conj = ['потому что','из-за того, что','так как ', 'хотя', 'несмотря на то что']
    return random.choice(cause_conj)

def random_sentence1():
  return noun('s') + ' ' + verb('s') + ', ' + conjunction() + ' ' + adjective() + 'е ' + noun('p') + ' ' + verb('p') + '. '


def random_sentence2():
  return just_conj() + ' ' + time() + ' ' + clause() + ' ' + compar_adjective() + ', ' + 'чем' + ' ' + rand_noun() + '. '

def random_sentence3():
  return clause() + ' ' + adverb() + ', ' + cause_conjunction() + ' ' + time() + ' ' + clause() + '. '

def random_sentence4():
  return just_conj() + ' ' + question() + ' ' + noun('s') + ' ' + verb('s') + ', что' + ' ' + infinitive() + ' ' + gen_noun() + ' - ' + 'это так ' + adverb() + '? '

def random_sentence5():
  return gen_noun() + ' ' + verb('p') + ' ' + adjective() + 'е ' + noun('p')  + ', ' + just_conj() + ' ' +clause()+ ' ' +adverb() + '. '

def random_text():
  return random_sentence3() + random_sentence5() + random_sentence1() +  random_sentence2() + random_sentence4()

print(random_text())
