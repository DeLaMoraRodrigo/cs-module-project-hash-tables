# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
with open('crack_caesar/ciphertext.txt') as f:
    words = f.read()
    split_words = words.split()

capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
norm_freq = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
letters = dict()
decode_table = dict()
decoded_message = list()

for word in split_words:
    for letter in word:
        if letter in capitals:
            letters[letter] = letters.get(letter, 0) + 1

pairs = list(letters.items())
pairs.sort(key = lambda e: e[1], reverse = True)

for i in range(len(norm_freq)):
    decode_table[pairs[i][0]] = norm_freq[i]

for word in split_words:
    new_word = ""
    for letter in word:
        if letter not in capitals:
            new_word += letter
        if letter in capitals:
            new_letter = decode_table[letter]
            new_word += new_letter
    decoded_message.append(new_word)            


print(' '.join(decoded_message))
