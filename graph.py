import pickle

chars = dict(
    [a, dict([b, 0] for b in 'abcdefghijklmnopqrstuvwxyzåäö ')]
    for a in 'abcdefghijklmnopqrstuvwxyzåäö ')


with open('ord.txt', 'r', encoding='utf8') as f:
    while True:
        word = f.readline()[:-1].lower()
        if not word:
            break
        for i in range(len(word)-1):
            chars[word[i]][word[i+1]] += 1

with open('graph.pickle', 'wb') as f:
    pickle.dump(chars, f)
