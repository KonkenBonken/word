res = ''

with open('ord.txt', 'r', encoding='utf8') as f:
    words = f.readlines()
    for i, word in enumerate(words):
        for c in word:
            if c.lower() not in 'abcdefghijklmnopqrstuvwxyzåäö\n ':
                del words[i]
                break
    res = ''.join(words)

with open('ord.txt', 'w', encoding='utf8') as f:
    f.write(res)
