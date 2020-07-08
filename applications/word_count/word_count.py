def word_count(s):
    # Your code here
    count = dict()
    words = s.split()

    for word in words:
        lower_case = word.lower().translate({ord(i):None for i in '":;,.-+=/\|[]{}()*^&'})
        if lower_case != '':
            count[lower_case] = count.get(lower_case, 0) + 1

    return count


if __name__ == "__main__":
    print(word_count(""))
    # print(word_count("Hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
