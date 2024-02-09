import pickle
import random

f = open('graph.pickle', 'rb')
chars = pickle.load(f)
f.close()


def generate_word():
    word = random.choice(list(chars.keys()))
    for _ in range(random.randint(3, 8)):
        num = random.random()
        letter = '?'
        for l in chars.keys():
            num -= chars[word[0]][l]
            if num <= 0:
                letter = l
                break

        word += letter
    return word


for _ in range(10):
    print(generate_word())
