def no_dups(s):
    # Your code here

    # Using Set
    # string_arr = s.split()
    # set_arr = set()
    # for i in range(len(string_arr)):
    #     set_arr.add(string_arr[i])
    # print(set_arr)
    
    # Using List
    string_arr = s.split()
    unique_arr = list()
    for i in range(len(string_arr)):
        if string_arr[i] not in unique_arr:
            unique_arr.append(string_arr[i])
    unique_string = ' '.join(unique_arr)
    return unique_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))