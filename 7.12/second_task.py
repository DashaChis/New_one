with open("C:/Python33/freq.txt", encoding="utf-8") as f:
    text = f.read()

    string = text.split()
    word = 0
    s = 0
    while string[word]!= "ящик":
        if string[word] == "част":
            print(string[int(word)-2])
            ipm = float(string[int(word)+2])
            s = s + ipm
            word = word+1
        else:
            word = word+1
print(s)
