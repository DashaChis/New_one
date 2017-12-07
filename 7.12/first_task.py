with open("C:/Python33/freq.txt", encoding="utf-8") as f:
    text = f.read()

    string = text.split()
    word = 0
    while string[word]!= "ящик":
        if string[word] == "перех":
            print(string[int(word)-4])
            word = word+1
        else:
            word = word+1
