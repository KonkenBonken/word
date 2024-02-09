heads = []

with open('ord.txt', 'r', encoding='utf8') as f:
    while True:
        word = f.readline()[:-1].lower()
        if not word:
            break
        if word[0] not in heads:
            heads.append(word[0])

print(heads)
