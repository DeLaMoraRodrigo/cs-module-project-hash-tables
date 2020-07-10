import random

# Read in all the words in one go
with open('markov/input.txt') as f:
    words = f.read()
    split_words = words.split()

capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"']
ends = ['.', '?', '!', '"']

# TODO: analyze which words can follow other words
# Your code here
markov = dict()
start_words = list()
end_words = list()

for i in range(len(split_words) - 1):
    if split_words[i][0] in capitals:
        start_words.append(split_words[i])
    if split_words[i][-1] in ends:
        end_words.append(split_words[i])
    markov[split_words[i]] = markov.get(split_words[i], [])
    markov[split_words[i]].append(split_words[i + 1])

# TODO: construct 5 random sentences
# Your code here
for i in range(5):
    sentence = ""
    start = random.choice(start_words)
    sentence += start + " "
    new_word = random.choice(markov[start])

    while start not in end_words:
        if new_word in end_words:
            sentence += new_word
            break
        sentence += new_word + " "
        new_word = random.choice(markov[new_word])

    print(sentence)

