import os

def check():
    start_path = '.'
    words = []
    for root, dirs, files in os.walk("."):
        for name in files:
            print(os.path.join(name))
            words.extend(name)
        for name in dirs:
            print(os.path.join(name))
            words.extend(name)
    return len(words)

def main():
    check()

if __name__ == '__main__':
    main()
