import pickle
import random

f = open('graph.pickle', 'rb')
heads = pickle.load(f)
f.close()


def generate_word():
    head = heads
    word = ''
    while True:
        letter = random.choice(list(head.keys()))
        if letter == '\r':
            return word
        word += letter
        head = head[letter]


print(generate_word())
