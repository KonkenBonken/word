import pickle
import random

f = open('graph.pickle', 'rb')
chars = pickle.load(f)
f.close()


def generate_word():
    letters = list(chars.keys())
    word = ''
    for _ in range(random.randint(3, 8)):
        letter = random.choice(letters)
        word += letter
        letters = list(chars[letter])
    return word


for _ in range(10):
    print(generate_word())
