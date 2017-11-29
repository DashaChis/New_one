a=str(input("Введите латинские слова:"))
with open("mytxt.txt", "w", encoding="utf-8") as f:
        f.write('')
while a!='':
    if a[len(a)-3:]=="tur":
        with open("mytxt.txt", "a", encoding="utf-8") as f:
                f.write(a)
                f.write('\n')
    a=str(input())
