



def readFile():
    f = open("/data/source/dict.txt", 'r')
    lines = f.readlines()
    for line in lines:
        words = line.split('\t')
        eng = words[0]
        kor = words[1]
        if " " in eng and " " not in  kor:
            
    

def main():
    pass

if __name__ == "__main__":
    main()

