import pickle

chars = dict([c, set()] for c in 'abcdefghijklmnopqrstuvwxyzåäö ')

with open('ord.txt', 'r', encoding='utf8') as f:
    while True:
        word = f.readline()[:-1].lower()
        if not word:
            break
        for i in range(len(word)-1):
            chars[word[i]].add(word[i+1])

with open('graph.pickle', 'wb') as f:
    pickle.dump(chars, f)
