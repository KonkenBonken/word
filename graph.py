import pickle

heads = dict()


def rec(d: 'dict[str,str]', head: str, tail: str):
    if head not in d:
        d[head] = dict()
    if tail:
        rec(d[head], tail[0], tail[1:])
    else:
        d[head] = {'\r': dict()}


with open('ord.txt', 'r', encoding='utf8') as f:
    while True:
        word = f.readline()[:-1].lower()
        if not word:
            break
        rec(heads, word[0], word[1:])

with open('graph.pickle', 'wb') as f:
    pickle.dump(heads, f)
