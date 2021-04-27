def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possible_words(lwords, charSet):
    for word in lwords:
        flag = 1
        chars = charCount(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
  
while True:
    with open('dictionary.txt', 'r') as f:
        lines = f.read().splitlines()
        charSet = input("Enter Scrambled Word Here -->: ")
        print("-----------------------")
        possible_words(lines, charSet)
        print("-----------------------")
        print("Press CTRL + C to exit!")
        print("-----------------------")
